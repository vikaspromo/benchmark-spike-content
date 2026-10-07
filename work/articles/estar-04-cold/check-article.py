"""Article-specific measurements. Editorial accuracy is assessed separately.

Retained to reproduce this prototype's final-version checks; not a production validator.
"""
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RULES = json.loads((ROOT / 'writing-rules.json').read_text())
RULE = {r['id']: r for r in RULES['rules']}


def words(text):
    return re.findall(r"\b[\w]+(?:['’][\w]+)*\b", text)


def prose(raw):
    raw = re.sub(r'^#{1,6} .*$', '', raw, flags=re.M)
    raw = re.sub(r'\[NEEDS INFORMATION:[^\]]+\]', '', raw)
    raw = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', raw)
    raw = re.sub(r'https?://\S+', '', raw)
    return raw


def sentence_parts(text):
    # Abbreviations and proper names must not inflate paragraph sentence counts.
    text = re.sub(r'\b(?:Dr|vs|P)\.', lambda m: m.group().replace('.', ''), text)
    return [x for x in re.split(r'[.!?]+(?:\s+|$)', text.strip()) if words(x)]


def syllables(word):
    # Transparent heuristic, not dictionary pronunciation or clinical readability proof.
    word = word.lower()
    count = len(re.findall(r'[aeiouy]+', word))
    if word.endswith('e') and not word.endswith(('le', 'ye')) and count > 1:
        count -= 1
    if word.endswith('ed') and not word.endswith(('ted', 'ded')) and count > 1:
        count -= 1
    return max(1, count)


def evaluate(path):
    raw = path.read_text()
    body = prose(raw)
    tokens = words(body)
    headings = re.findall(r'^(#{1,6}) (.+)$', raw, re.M)
    links = re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', raw)
    internal = [(a, u) for a, u in links if u.startswith('https://estarmedspa.com/')]
    content = [(a, u) for a, u in internal if '/services/' in u]
    external = [(a, u) for a, u in links if not u.startswith('https://estarmedspa.com/')]
    paragraphs = [x for x in body.split('\n\n') if words(x) and not x.lstrip().startswith('- ')]
    paragraph_sentence_counts = [len(sentence_parts(x)) for x in paragraphs]
    sentences = sentence_parts(body)
    grade = .39 * len(tokens) / len(sentences) + 11.8 * sum(syllables(w) for w in tokens) / len(tokens) - 15.59
    phrases = RULE['R18']['check']['banned_phrases']
    generic = [x for x in phrases if x.lower() in raw.lower()]
    duplicates = [u for u, n in collections.Counter(u for _, u in links).items() if n > 1]
    min_words = RULE['R02']['check']['minimum']
    min_external = RULE['R08']['check']['minimum']
    max_external = RULE['R08']['check']['maximum']
    allowed_external_hosts = ('https://www.fda.gov/', 'https://dailymed.nlm.nih.gov/')
    marker_count = len(re.findall(r'\[NEEDS INFORMATION:', raw))
    wrong_name = re.findall(r'\bEster\b|\bEstar Medspa\b|\bEstar Med Spa\b', raw)
    phone_matches = re.findall(r'(?<!\d)\d{3}[- .()]\d{3}[- .]\d{4}(?!\d)', raw)
    checks = {
        'substantive_word_count': {'status': 'PASS' if len(tokens) >= min_words else 'FAIL', 'words': len(tokens), 'minimum': min_words, 'limit': 'Prose token count; substantive value assessed separately.'},
        'assigned_title_and_headings': {'status': 'PASS' if headings and headings[0][1] == 'What Is the Difference Between a Lip Flip and Lip Filler?' and sum(len(h) == 1 for h, _ in headings) == 1 and all(len(headings[i][0]) <= len(headings[i-1][0]) + 1 for i in range(1, len(headings))) else 'FAIL', 'heading_count': len(headings)},
        'supplied_primary_keyword_placements': {'status': 'NOT_CHECKABLE_MISSING_INPUT', 'primary_keyword': RULES['primary_keyword'], 'placements': ['title', 'first_100_words', 'H2', 'meta_title', 'meta_description', 'URL_when_applicable'], 'metadata': 'not drafted; missing keyword and expectations'},
        'internal_content_links': {'status': 'PASS' if len(content) == RULE['R07']['check']['content_links'] and len(set(u for _, u in content)) == len(content) else 'FAIL', 'count': len(content), 'links': content, 'cta_excluded': [x for x in internal if x not in content]},
        'authoritative_external_links': {'status': 'PASS' if min_external <= len(external) <= max_external and all(u.startswith(allowed_external_hosts) for _, u in external) else 'FAIL', 'count': len(external), 'links': external},
        'repeated_destinations': {'status': 'PASS' if not duplicates else 'FAIL', 'duplicates': duplicates},
        'phone_format_and_known_number': {'status': 'PASS' if phone_matches == ['301-917-3870'] else 'FAIL', 'matches': phone_matches},
        'business_name_screen': {'status': 'PASS' if 'Estar MedSpa' in raw and not wrong_name else 'FAIL', 'unexpected_forms': wrong_name},
        'generic_phrase_screen': {'status': 'PASS' if not generic else 'FAIL', 'matches': generic, 'limit': 'Screens only catalog phrases.'},
        'short_paragraphs': {'status': 'PASS' if sum(x <= 2 for x in paragraph_sentence_counts) > len(paragraphs)/2 else 'FAIL', 'paragraphs': len(paragraphs), 'one_or_two_sentence_paragraphs': sum(x <= 2 for x in paragraph_sentence_counts), 'max_words': max(len(words(x)) for x in paragraphs)},
        'readability_estimate': {'status': 'WITHIN_TARGET_ESTIMATE' if 6 <= grade <= 9 else 'EDITORIAL_REVIEW_REQUIRED', 'flesch_kincaid_heuristic_grade': round(grade, 2), 'mean_sentence_words': round(len(tokens)/len(sentences), 2), 'limit': 'Heuristic syllables/sentence splitting; estimate is not a validated grade determination.'},
        'required_provider_markers': {'status': 'PASS' if marker_count == 2 else 'FAIL', 'count': marker_count},
        'numeric_style_flags': {'status': 'MANUAL_REVIEW', 'isolated_small_digits': re.findall(r'(?<![\w-])(?:[1-9])(?![\w-])', body)},
        'closing_cta': {'status': 'PASS' if all(x in raw.split('## Talk Through Your Lip Goals in Olney')[-1] for x in ['Estar MedSpa', 'Olney, MD', '301-917-3870', 'https://estarmedspa.com/contact/']) else 'FAIL'},
    }
    return {'file': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'checks': checks, 'limits': 'Automated counts and pattern checks measure only their stated properties. Medical, editorial, AP and proofreading assessments are agent judgments without validated judging reliability.'}


if __name__ == '__main__':
    result = evaluate(ROOT / sys.argv[1])
    if len(sys.argv) > 2:
        (ROOT / sys.argv[2]).write_text(json.dumps(result, indent=2) + '\n')
    else:
        print(json.dumps(result, indent=2))
