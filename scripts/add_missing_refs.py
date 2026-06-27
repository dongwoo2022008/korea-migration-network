#!/usr/bin/env python3
import re
import os

ARCHIVE_REFS = "/home/ubuntu/korea-migration-network/docs/_archive/05_결론_Conclusion_archived.md"
LIT_REVIEW = "/home/ubuntu/korea-migration-network/docs/02_문헌연구_Literature_Review.md"

# ─── 1. Pu 2021 잔재 교정 ──────────────────────────────────────────────────
with open(LIT_REVIEW, encoding='utf-8') as f:
    lit_text = f.read()

lit_text = lit_text.replace("(Pu et al., 2021)", "(Pu et al., 2019)")

with open(LIT_REVIEW, "w", encoding='utf-8') as f:
    f.write(lit_text)
print("Pu et al., 2021 -> 2019 교정 완료")

# ─── 2. 미등재 서지 8편 준비 ───────────────────────────────────────────────
missing_refs = [
    # 국문 3편
    "마강래. (2017). *지방도시 살생부: 압축도시만이 살길이다*. 개마고원.",
    "이광원. (2023). 위계적 다중 회귀분석을 활용한 지방소멸 요인이 핵심생산가능인구의 순이동에 미치는 영향 분석. *지역산업과 고용*, 10(1), 1-25.",
    "이상호. (2018). 주요 고용이슈 심층 분석: 한국의 지방소멸 2018. *고용동향브리프*, 2018(8), 1-32.",
    
    # 영문 5편
    "Brin, S., & Page, L. (1998). The anatomy of a large-scale hypertextual Web search engine. *Computer Networks and ISDN Systems*, 30(1-7), 107-117. https://doi.org/10.1016/S0169-7552(98)00110-X",
    "Fujita, M., Krugman, P., & Venables, A. J. (1999). *The Spatial Economy: Cities, Regions, and International Trade*. MIT Press.",
    "Kim, Y., Lee, J., & Park, S. (2025). Machine learning prediction of depression in culturally diverse families. *Frontiers in Public Health*, 13, 1666084. https://doi.org/10.3389/fpubh.2025.1666084",
    "Krugman, P. (1991). Increasing returns and economic geography. *Journal of Political Economy*, 99(3), 483-499. https://doi.org/10.1086/261763",
    "OECD. (2023). *OECD Regional Outlook 2023: The Longstanding Geography of Inequalities*. OECD Publishing. https://doi.org/10.1787/3a6174ba-en"
]

# ─── 3. 아카이브 파일에 서지 추가 및 정렬 ──────────────────────────────────
refs = []
in_refs = False
other_content = []

with open(ARCHIVE_REFS, encoding='utf-8') as f:
    for line in f:
        if re.match(r'^(##|#)\s*(참고문헌|References)', line):
            in_refs = True
            other_content.append(line)
            continue
        if in_refs and line.startswith('#'):
            in_refs = False
            other_content.append(line)
            continue
            
        if in_refs:
            if line.strip() and re.match(r'^[A-Z가-힣이전김박오]', line):
                refs.append(line.strip())
        else:
            other_content.append(line)

# 기존 목록에 새 서지 추가
refs.extend(missing_refs)

# 국문/영문 분리 후 정렬
korean_refs = sorted([r for r in refs if re.match(r'^[가-힣이전김박오]', r)])
english_refs = sorted([r for r in refs if not re.match(r'^[가-힣이전김박오]', r)], key=lambda x: x.lower())

# 아카이브 파일 재작성 (목록 업데이트)
with open(ARCHIVE_REFS, "w", encoding='utf-8') as f:
    for line in other_content:
        if re.match(r'^(##|#)\s*(참고문헌|References)', line):
            f.write(line)
            f.write("\n")
            for r in korean_refs:
                f.write(r + "\n\n")
            for r in english_refs:
                f.write(r + "\n\n")
        else:
            if not in_refs: # 기존 목록 부분 제외하고 나머지 쓰기
                f.write(line)

print(f"총 {len(korean_refs) + len(english_refs)}편으로 목록 업데이트 완료")
