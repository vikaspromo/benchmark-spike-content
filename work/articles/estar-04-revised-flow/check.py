"""Reproduce limited mechanical measurements; editorial/factual judgment stays separate."""
from pathlib import Path
import re, json, hashlib
from urllib.parse import urlparse
root=Path(__file__).resolve().parent
p=root/'article.md'; s=p.read_text()
text=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',s)
words=lambda t: re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b",t)
body='\n'.join(line for line in text.splitlines() if not line.startswith('#'))
links=re.findall(r'\[([^]]+)\]\(([^)]+)\)',s)
internal=[u for a,u in links if urlparse(u).netloc=='estarmedspa.com']
cta='https://estarmedspa.com/contact/'
content=[u for u in internal if u!=cta]
external=[u for a,u in links if urlparse(u).netloc!='estarmedspa.com']
paragraphs=[p for p in body.split('\n\n') if p.strip() and not p.strip().startswith('-')]
sentences=[x for x in re.split(r'[.!?]+(?:\s|$)',body.replace('Dr.','Dr')) if x.strip()]
# Transparent approximation; count final e conservatively, not a pronunciation lexicon.
def syllables(w):
    w=re.sub('[^a-z]','',w.lower()); n=len(re.findall('[aeiouy]+',w))
    if w.endswith('e') and not w.endswith(('le','ye')) and n>1:n-=1
    return max(1,n)
ws=words(body); syll=sum(syllables(w) for w in ws)
grade=0.39*(len(ws)/len(sentences))+11.8*(syll/len(ws))-15.59
comments=json.loads((root/'comments.json').read_text())
paragraph_sentences=[len([x for x in re.split(r'[.!?]+(?:\s|$)',p.replace('Dr.','Dr').replace('Mimi P.','Mimi P')) if x.strip()]) for p in paragraphs]
checks={
 'exact_title':s.splitlines()[0]=='# What Is the Difference Between a Lip Flip and Lip Filler?',
 'minimum_body_words':len(ws)>=1200,
 'one_h1':len(re.findall(r'^# ',s,re.M))==1,
 'logical_heading_hierarchy':not re.search(r'^#{3,}',s,re.M),
 'four_internal_content_links':len(content)==4,
 'cta_excluded_from_content_count':internal.count(cta)==1,
 'no_repeated_destinations':len({u for a,u in links})==len(links),
 'first_internal_primary_service':content[0]=='https://estarmedspa.com/services/botox-lip-flip-olney-maryland/',
 'one_or_two_external_links':1<=len(external)<=2,
 'no_competitor_external_links':all(urlparse(u).netloc in {'my.clevelandclinic.org','www.fda.gov'} for u in external),
 'verified_phone_format':re.findall(r'\b\d{3}-\d{3}-\d{4}\b',s)==['301-917-3870'],
 'no_forbidden_generic_phrases':not any(x.lower() in s.lower() for x in ["In today's fast-paced world","When it comes to","Unlock the secrets","Delve into","Game-changing"]),
 'no_required_markers':not re.search(r'\[(?:TBD|NEEDS|MISSING)',s,re.I),
 'most_paragraphs_one_or_two_sentences':sum(n<=2 for n in paragraph_sentences)>len(paragraph_sentences)/2,
 'unique_comment_anchors':all(s.count(c['anchor'])==1 for c in comments),
 'no_fabricated_quotes_or_reviews':not re.search(r'“[^”]+”\s*(?:says|said)',s),
}
result={'article':'article.md','article_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'word_count_including_headings':len(words(text)), 'body_word_count_excluding_headings_urls':len(ws),'headings':re.findall(r'^#+ .+$',s,re.M),'internal_content_links':content,'cta':cta,'external_links':external,'paragraph_count':len(paragraphs),'paragraphs_one_or_two_sentences':sum(n<=2 for n in paragraph_sentences),'longest_prose_paragraph_words':max(len(words(p)) for p in paragraphs),'approximate_reading_grade':round(grade,2),'readability_method':'Flesch-Kincaid with vowel-group syllable approximation; nonauthoritative, no editorial pass implied','checks':checks,'all_mechanical_checks_pass':all(checks.values()),'limits':'Counts and string checks do not establish substantive coverage, accuracy, grammar, or reader usefulness. Separate assessments required.'}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
