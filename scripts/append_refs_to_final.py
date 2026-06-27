#!/usr/bin/env python3
import os
import re

FINAL_DOC = "/home/ubuntu/korea-migration-network/docs/대한민국_시군구_인구이동_네트워크_진화와_지역_흡인력_분석_최종논문.md"
ARCHIVE_REFS = "/home/ubuntu/korea-migration-network/docs/_archive/05_결론_Conclusion_archived.md"

# 1. 아카이브에서 참고문헌 목록 추출
refs_text = []
in_refs = False

with open(ARCHIVE_REFS, encoding='utf-8') as f:
    for line in f:
        if re.match(r'^(##|#)\s*(참고문헌|References)', line):
            in_refs = True
            refs_text.append(line)
            continue
        if in_refs and line.startswith('#'):
            break
        if in_refs:
            refs_text.append(line)

# 2. 최종본 말미에 참고문헌이 이미 있는지 확인 후 제거/교체
with open(FINAL_DOC, encoding='utf-8') as f:
    final_lines = f.readlines()

new_final_lines = []
in_final_refs = False

for line in final_lines:
    if re.match(r'^(##|#)\s*(참고문헌|References)', line):
        in_final_refs = True
    if in_final_refs and line.startswith('#') and not re.match(r'^(##|#)\s*(참고문헌|References)', line):
        in_final_refs = False
    
    if not in_final_refs:
        new_final_lines.append(line)

# 3. 추출한 참고문헌을 맨 끝에 추가
with open(FINAL_DOC, "w", encoding='utf-8') as f:
    f.writelines(new_final_lines)
    if not new_final_lines[-1].endswith('\n'):
        f.write('\n')
    f.write('\n')
    f.writelines(refs_text)

print("최종통합본 말미에 참고문헌 목록 재배치 완료")
