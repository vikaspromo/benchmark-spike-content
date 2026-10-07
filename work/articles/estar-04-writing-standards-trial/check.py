#!/usr/bin/env python3
"""Reproducible deterministic checks for this trial. Editorial checks are separate."""
import re, json, hashlib, argparse
from pathlib import Path
from urllib.parse import urlparse
P=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--article',type=Path,default=P/'article.md')
parser.add_argument('--output',type=Path,default=P/'checks.json')
args=parser.parse_args()
s=args.article.read_text()
r=json.loads((P/'rules.json').read_text())
plain=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',s)
body='\n'.join(line for line in plain.splitlines() if not line.startswith('#') and not line.startswith('[NEEDS INFORMATION:'))
words=re.findall(r"\b[\w]+(?:['’\-][\w]+)*\b",body)
headings=re.findall(r'^(#+) (.+)$',s,re.M)
links=re.findall(r'\[([^]]+)\]\(([^)]+)\)',s)
internal=[(a,u) for a,u in links if urlparse(u).hostname=='estarmedspa.com']
cta=[(a,u) for a,u in internal if u=='https://estarmedspa.com/contact/']
content=[(a,u) for a,u in internal if (a,u) not in cta]
external=[(a,u) for a,u in links if urlparse(u).hostname!='estarmedspa.com']
paragraphs=[p for p in body.split('\n\n') if p.strip() and not p.lstrip().startswith('-')]
def sentences(t):
    t=re.sub(r'\bDr\.', 'Dr', t)
    t=re.sub(r'\bP\.', 'P', t)
    return [v for v in re.split(r'[.!?]+(?:\s|$)',t) if v.strip()]
sent=sentences(body)
def syllables(w):
    w=re.sub('[^a-z]','',w.lower())
    if len(w)<4:return 1
    n=len(re.findall('[aeiouy]+',w))
    if w.endswith('e') and not w.endswith(('le','ye')):n-=1
    return max(1,n)
syll=sum(syllables(w) for w in words)
fk=.39*len(words)/len(sent)+11.8*syll/len(words)-15.59
phrases=next(v['phrases'] for v in r['rules'] if v['id']=='generic_phrases')
checks={
 'title':{'status':'pass' if headings[0][1]==r['assignment']['title'] else 'fail'},
 'word_count':{'status':'pass' if len(words)>=1200 else 'fail','body_words_excluding_headings':len(words),'limitation':'Count does not establish substance'},
 'headings':{'status':'pass' if sum(len(h)==1 for h,t in headings)==1 and all(len(h)<=3 for h,t in headings) else 'fail','headings':headings},
 'internal_content_links':{'status':'pass' if len(content)==4 and len({u for a,u in internal})==len(internal) else 'fail','count':len(content),'destinations':content,'cta_excluded':cta},
 'first_content_link':{'status':'pass' if content[0][1].endswith('botox-lip-flip-olney-maryland/') else 'fail'},
 'external_links':{'status':'pass' if 1<=len(external)<=2 and all(urlparse(u).hostname in ['www.fda.gov','www.rxabbvie.com'] for a,u in external) else 'fail','destinations':external},
 'generic_phrases':{'status':'pass' if not any(p.lower() in s.lower() for p in phrases) else 'fail','hits':[p for p in phrases if p.lower() in s.lower()]},
 'phone':{'status':'pass' if re.findall(r'\b\d{3}-\d{3}-\d{4}\b',s)==['301-917-3870'] else 'fail','evidence':'Estar home/contact and service pages'},
 'primary_keyword':{'status':'unknown_input_not_passed','input':None,'placements_not_evaluated':next(v['locations'] for v in r['rules'] if v['id']=='primary_keyword')},
 'metadata':{'status':'scope_unknown_not_passed','reason':'Customer metadata deliverable and keywords unknown; no proposed metadata treated as final'},
 'short_paragraphs':{'status':'pass' if sum(len(sentences(p))<=2 for p in paragraphs)>len(paragraphs)/2 else 'fail','paragraphs':len(paragraphs),'one_or_two_sentence':sum(len(sentences(p))<=2 for p in paragraphs)},
 'readability':{'status':'measurement_only','flesch_kincaid_estimate':round(fk,2),'average_sentence_words':round(len(words)/len(sent),2),'limitation':'Regex syllable approximation; editorial reading required'},
 'numeric_tokens_for_editorial_review':{'status':'review','tokens':re.findall(r'\b\d+\b',plain)},
 'business_name':{'status':'scan_only','Estar_occurrences':s.count('Estar'),'forbidden_variants_found':re.findall(r'\b(?:EStar|ESTAR|estar)\b(?!medspa)',plain)},
 'unresolved_markers':{'status':'measurement_only','matches':re.findall(r'\[(?:TODO|NEEDS|INSERT)[^]]*\]',s)}
}
out={'draft_sha256':hashlib.sha256(s.encode()).hexdigest(),'rule_catalog_sha256':hashlib.sha256((P/'rules.json').read_bytes()).hexdigest(),'checks':checks,'limitations':'Deterministic checks measure syntax/counts only; no clinical validation, SEO prediction, or customer acceptance.'}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
