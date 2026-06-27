#!/usr/bin/env python3
"""
§4 Table 재번호 스크립트
매핑 (현재 → 신규):
  4-8  → 4-6   (FE 결정요인)
  4-11 → 4-7   (수도권/비수도권 이질성)
  4-12 → 4-8   (도시 규모별 이질성)
  4-13 → 4-9   (Chow 구조변화)
  4-14 → 4-10  (대체 중심성 강건성)
  4-9  → 4-11  (SDM 추정)
  4-10 → 4-12  (SDM 직·간접효과)
  4-15 → 4-13  (대체 공간가중치 강건성)
  4-6  → 4-14  (연령집단 네트워크 구조)
  4-7  → 4-15  (연령집단 PageRank 허브)

전략: 충돌 방지를 위해 먼저 임시 번호(4-T01~T10)로 바꾼 뒤 최종 번호로 교체
"""

import re

path = '/home/ubuntu/korea-migration-network/docs/04_연구결과_Results.md'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1단계: 현재 번호 → 임시 번호 ─────────────────────────────────────────────
# 표 헤더(| **Table 4-X** | 또는 **Table 4-X**), 본문 인라인(Table 4-X) 모두 처리
# 순서 중요: 두 자리 숫자 먼저 처리 (4-15 > 4-1)

step1 = [
    ('Table 4-15', 'Table 4-T13'),  # 대체W → T13
    ('Table 4-14', 'Table 4-T10'),  # 대체중심성 → T10
    ('Table 4-13', 'Table 4-T09'),  # Chow → T09
    ('Table 4-12', 'Table 4-T08'),  # 도시규모 → T08
    ('Table 4-11', 'Table 4-T07'),  # 수도권 → T07
    ('Table 4-10', 'Table 4-T12'),  # SDM 분해 → T12
    ('Table 4-9',  'Table 4-T11'),  # SDM 추정 → T11
    ('Table 4-8',  'Table 4-T06'),  # FE → T06
    ('Table 4-7',  'Table 4-T15'),  # 연령허브 → T15
    ('Table 4-6',  'Table 4-T14'),  # 연령구조 → T14
]

for old, tmp in step1:
    content = content.replace(old, tmp)

# ── 2단계: 임시 번호 → 최종 번호 ─────────────────────────────────────────────
step2 = [
    ('Table 4-T06', 'Table 4-6'),
    ('Table 4-T07', 'Table 4-7'),
    ('Table 4-T08', 'Table 4-8'),
    ('Table 4-T09', 'Table 4-9'),
    ('Table 4-T10', 'Table 4-10'),
    ('Table 4-T11', 'Table 4-11'),
    ('Table 4-T12', 'Table 4-12'),
    ('Table 4-T13', 'Table 4-13'),
    ('Table 4-T14', 'Table 4-14'),
    ('Table 4-T15', 'Table 4-15'),
]

for tmp, new in step2:
    content = content.replace(tmp, new)

# ── 3단계: §4.7.1 Chow 검정 참조 수정 ────────────────────────────────────────
# "Chow 검정(§4.3.4, Table 4-13)" → "Table 4-9"
content = content.replace(
    'Chow 검정(§4.3.4, Table 4-13)',
    'Chow 검정(§4.3.4, Table 4-9)'
)
content = content.replace(
    'Chow 검정(§4.3.4, **Table 4-13**)',
    'Chow 검정(§4.3.4, **Table 4-9**)'
)

# ── 4단계: §4.4 본문 "이는 Table 4-11에서 세 가지 W 모두" → Table 4-13 ────────
# (대체W 표를 지칭하는 오참조)
content = content.replace(
    '이는 Table 4-11에서 세 가지 W 모두',
    '이는 Table 4-13에서 세 가지 W 모두'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Table 재번호 완료")

# 검증
with open(path, 'r', encoding='utf-8') as f:
    verify = f.read()

# 임시 번호 잔존 확인
import re
tmp_remaining = re.findall(r'Table 4-T\d+', verify)
if tmp_remaining:
    print(f"❌ 임시 번호 잔존: {set(tmp_remaining)}")
else:
    print("✅ 임시 번호 잔존 없음")

# 주요 번호 확인
checks = [
    ('Table 4-6 (FE)', 'Table 4-6'),
    ('Table 4-7 (수도권)', 'Table 4-7'),
    ('Table 4-9 (Chow)', 'Table 4-9'),
    ('Table 4-11 (SDM)', 'Table 4-11'),
    ('Table 4-13 (대체W)', 'Table 4-13'),
    ('Table 4-14 (연령구조)', 'Table 4-14'),
    ('Table 4-15 (연령허브)', 'Table 4-15'),
]
print("\n번호 확인:")
for label, text in checks:
    found = text in verify
    print(f"  {'✅' if found else '❌'} {label}: {'발견' if found else '미발견'}")
