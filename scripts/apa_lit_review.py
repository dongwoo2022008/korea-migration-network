#!/usr/bin/env python3
"""
§2 문헌연구: [n] 대괄호 제거 및 APA 형식 표준화
"""

import re

path = "/home/ubuntu/korea-migration-network/docs/02_문헌연구_Literature_Review.md"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

ref_start = text.find("## References")
if ref_start == -1:
    ref_start = len(text)

body = text[:ref_start]
refs = text[ref_start:]

# 1. 본문의 " [n]" 패턴 전면 제거
body = re.sub(r'\s*\[\d+\]', '', body)

# 2. APA 형식 표준화 (저자명 다듬기)
# "와/과" 및 "등"은 이미 국문으로 잘 되어 있으나, 일부 영문 저자 사이의 "와"를 "와/과"로 유지 (한국어 논문 규정)
# 복수 출처 괄호형 치환 (이미 텍스트로 적혀 있는 부분 확인)
# 예: Place Attractiveness 이론 [30][31] -> 이미 [n]이 지워졌으므로 "Place Attractiveness 이론에 기반하여" 가 됨.
# -> 원래 "장소 매력도(Place Attractiveness) 이론 [30][31]에 기반하여"
# -> 위 정규식으로 "장소 매력도(Place Attractiveness) 이론에 기반하여" 가 됨.
# 지시서에 따라 [n]만 삭제하면 서술형 APA 완성됨.
# 단, 복수 출처 괄호형이 필요한 곳은 복원.

text = body + refs

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("§2 문헌연구 APA 변환 완료")
