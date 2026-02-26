#!/usr/bin/env python3
import re, sys, pathlib

if len(sys.argv) < 2:
    print('Usage: article_score.py <draft.md>')
    sys.exit(1)

text = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
words = len(re.findall(r"\b\w+\b", text))
h2 = len(re.findall(r"^## ", text, flags=re.M))
faq = '## FAQ' in text
sources = '## Sources' in text
checklist_like = bool(re.search(r'checklist|SOP|steps|what to do', text, re.I))

density = min(25, 8 + words//120)
readability = 14 if words > 1200 else 10
structure = min(20, 8 + h2*2)
trust = 18 if sources else 8
conversion = 12 if checklist_like else 6
if faq: conversion += 2
score = min(100, density+readability+structure+trust+conversion)

print(f"score={score}")
print(f"words={words} h2={h2} faq={faq} sources={sources} checklist={checklist_like}")
if words < 1200:
    print('hard_fail=thin_content')
