#!/usr/bin/env python3
"""
§4 Figure 재번호 스크립트
매핑 (현재 → 신규):
  4-6 (Freeman)   → 4-6  (유지)
  4-6 (Louvain08) → 4-7  ← 중복 해소
  4-7 (Louvain25) → 4-8
  4-8 (Moran)     → 4-9
  4-9 (LISA 2008) → 4-10
  4-10 (LISA 2025)→ 4-11
  4-11 (Jaccard)  → 4-12
  4-13 (COVID)    → 4-13 (유지)
  4-12 (연령시계열)→ 4-14
  4-14 (ML성능)   → 4-15
  4-15 (SHAP)     → 4-16
  4-16 (연도별PR) → 4-17

§4.2.4 중복 해소:
  - Freeman 그림 = Figure 4-6 (유지)
  - Louvain 2008 그림 헤더/캡션에서 "Figure 4-6" → "Figure 4-7"
  - Louvain 2025 Note "Same methodology as Figure 4-6" → "as Figure 4-7"

전략: 임시 번호(F-T06~F-T17) 경유
"""

results_path = '/home/ubuntu/korea-migration-network/docs/04_연구결과_Results.md'
conclusion_path = '/home/ubuntu/korea-migration-network/docs/05_결론_Conclusion.md'

def renumber_figures(content):
    # ── 1단계: 현재 → 임시 ─────────────────────────────────────────────────────
    # §4.2.4 Louvain 2008 그림: "Figure 4-6" 중 두 번째 등장만 F-T07로
    # 나머지 Figure 4-6 (Freeman)은 유지
    # 전략: Louvain 2008 캡션/헤더를 먼저 임시로 표시

    # Louvain 2008 캡션 식별 패턴 (Figure 4-6 Louvain 또는 커뮤니티 2008)
    import re

    # Louvain 2008 헤더 라인 (Figure 4-6 ... 2008 or Louvain Community 2008)
    content = re.sub(
        r'(Figure 4-6[^\n]*(?:Louvain|Community|커뮤니티)[^\n]*2008)',
        lambda m: m.group(0).replace('Figure 4-6', 'Figure 4-F07'),
        content
    )
    # Louvain 2008 Note "Same methodology as Figure 4-6"
    content = content.replace(
        'Same methodology as Figure 4-6',
        'Same methodology as Figure 4-F07_ref'
    )
    # §4.2.4 본문 "Figure 4-6와 Figure 4-7는 각각 2008·2025"
    content = content.replace(
        'Figure 4-6와 Figure 4-7는 각각 2008·2025',
        'Figure 4-F07와 Figure 4-F08는 각각 2008·2025'
    )
    content = content.replace(
        'Figure 4-6와 Figure 4-7은 각각 2008·2025',
        'Figure 4-F07와 Figure 4-F08은 각각 2008·2025'
    )

    # 나머지 번호 임시화 (두 자리 먼저)
    step1 = [
        ('Figure 4-16', 'Figure 4-F17'),
        ('Figure 4-15', 'Figure 4-F16'),
        ('Figure 4-14', 'Figure 4-F15'),
        ('Figure 4-13', 'Figure 4-F13'),  # 유지이지만 임시 경유
        ('Figure 4-12', 'Figure 4-F14'),
        ('Figure 4-11', 'Figure 4-F12'),
        ('Figure 4-10', 'Figure 4-F11'),
        ('Figure 4-9',  'Figure 4-F10'),
        ('Figure 4-8',  'Figure 4-F09'),
        ('Figure 4-7',  'Figure 4-F08'),
        # Figure 4-6 (Freeman) 유지 — 변환 안 함
    ]
    for old, tmp in step1:
        content = content.replace(old, tmp)

    # ── 2단계: 임시 → 최종 ─────────────────────────────────────────────────────
    step2 = [
        ('Figure 4-F07',     'Figure 4-7'),
        ('Figure 4-F07_ref', 'Figure 4-7'),
        ('Figure 4-F08',     'Figure 4-8'),
        ('Figure 4-F09',     'Figure 4-9'),
        ('Figure 4-F10',     'Figure 4-10'),
        ('Figure 4-F11',     'Figure 4-11'),
        ('Figure 4-F12',     'Figure 4-12'),
        ('Figure 4-F13',     'Figure 4-13'),
        ('Figure 4-F14',     'Figure 4-14'),
        ('Figure 4-F15',     'Figure 4-15'),
        ('Figure 4-F16',     'Figure 4-16'),
        ('Figure 4-F17',     'Figure 4-17'),
    ]
    for tmp, new in step2:
        content = content.replace(tmp, new)

    return content

# §4 Results 처리
with open(results_path, 'r', encoding='utf-8') as f:
    results = f.read()

results = renumber_figures(results)

with open(results_path, 'w', encoding='utf-8') as f:
    f.write(results)

print("✅ §4 Figure 재번호 완료")

# §5 Conclusion 처리 (Figure 4-16 → 4-17 동기화)
with open(conclusion_path, 'r', encoding='utf-8') as f:
    conclusion = f.read()

conclusion = conclusion.replace('Figure 4-16', 'Figure 4-17')

with open(conclusion_path, 'w', encoding='utf-8') as f:
    f.write(conclusion)

print("✅ §5 Figure 동기화 완료")

# 검증
with open(results_path, 'r', encoding='utf-8') as f:
    verify = f.read()

import re
tmp_remaining = re.findall(r'Figure 4-F\d+', verify)
if tmp_remaining:
    print(f"❌ 임시 번호 잔존: {set(tmp_remaining)}")
else:
    print("✅ 임시 번호 잔존 없음")

checks = [
    ('Figure 4-7 (Louvain08)', 'Figure 4-7'),
    ('Figure 4-9 (Moran)', 'Figure 4-9'),
    ('Figure 4-12 (Jaccard)', 'Figure 4-12'),
    ('Figure 4-14 (연령시계열)', 'Figure 4-14'),
    ('Figure 4-15 (ML성능)', 'Figure 4-15'),
    ('Figure 4-16 (SHAP)', 'Figure 4-16'),
    ('Figure 4-17 (연도별PR)', 'Figure 4-17'),
    ('Same methodology as Figure 4-7', 'Same methodology as Figure 4-7'),
]
print("\n번호 확인:")
for label, text in checks:
    found = text in verify
    print(f"  {'✅' if found else '❌'} {label}: {'발견' if found else '미발견'}")
