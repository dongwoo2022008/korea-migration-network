#!/usr/bin/env python3
"""
§1, §4, §5, §6(없음) 잔재 [n] 정리 및 APA 형식 일관성 확인
"""

import re
import glob

files = [
    "/home/ubuntu/korea-migration-network/docs/01_서론_Introduction.md",
    "/home/ubuntu/korea-migration-network/docs/04_연구결과_Results.md",
    "/home/ubuntu/korea-migration-network/docs/05_결론_Conclusion.md"
]

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # [n] 패턴 제거
    text = re.sub(r'\s*\[\d+\]', '', text)
    
    # 특수 케이스: §4 표 주석 등에서 저자명-연도 형식 확인
    # "LeSage & Pace (2009)" -> "LeSage와 Pace(2009)" 서술형, 괄호형은 "(LeSage & Pace, 2009)"
    text = text.replace("LeSage & Pace(2009)", "LeSage와 Pace(2009)")
    text = text.replace("Lundberg & Lee(2017)", "Lundberg와 Lee(2017)")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

print("§1, §4, §5 APA 잔재 정리 완료")
