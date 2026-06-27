#!/usr/bin/env python3
"""
§3 방법론: [n] 번호식 → APA 괄호형 일괄 매핑 치환
"""

import re

path = "/home/ubuntu/korea-migration-network/docs/03_방법론_Methodology.md"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 매핑 테이블 (지시서 기반)
mapping = {
    "[1]": "(Page et al., 1999)",
    "[2]": "(Freeman, 1978)",
    "[3]": "(Blondel et al., 2008)",
    "[4]": "(Elhorst, 2014)",
    "[5]": "(LeSage & Pace, 2009)",
    "[6]": "(Roberts et al., 2017)",
    "[7]": "(Lundberg & Lee, 2017)",
    "[8]": "(Anselin, 1995)",
    "[9]": "(Arellano & Bond, 1991)",
    "[10]": "(Lee & Yu, 2010)",
    "[11]": "(Levin et al., 2002)",
    "[12]": "(Im et al., 2003)",
    "[13]": "(Prokhorenkova et al., 2018)",
    "[14]": "(Akiba et al., 2019)",
    "[15]": "(Niedomysl, 2010)",
    "[16]": "(Haase et al., 2021)",
}

# §3 본문의 [n] 치환 (References 섹션 이전까지만 치환)
ref_start = text.find("## References")
if ref_start == -1:
    ref_start = len(text)

body = text[:ref_start]
refs = text[ref_start:]

# " [n]" 형식 치환 (앞에 공백이 있는 경우)
for old, new in mapping.items():
    body = body.replace(f" {old}", f"{new}")

# "[n]" 형식 치환 (공백 없는 경우)
for old, new in mapping.items():
    body = body.replace(old, new)

# LLC [11], IPS [12] 같은 특수 케이스 처리 (위에서 LLC(Levin et al., 2002) 형태로 변환됨)
# 본문에서 LLC(Levin et al., 2002), IPS(Im et al., 2003) 형태로 다듬기
body = body.replace("LLC(Levin et al., 2002), IPS(Im et al., 2003)", "LLC(Levin et al., 2002)와 IPS(Im et al., 2003)")

# "CatBoost(Prokhorenkova et al., 2018)" → "CatBoost(Prokhorenkova et al., 2018)"
# "optuna 3.6(Akiba et al., 2019)" → "optuna 3.6(Akiba et al., 2019)"

text = body + refs

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("§3 방법론 APA 변환 완료")
