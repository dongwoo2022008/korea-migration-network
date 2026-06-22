"""
데이터 및 코드 품질 검증 스크립트
검토 피드백 반영: net_rate 계산식, 변수 중복, 결측치, DiGraph 사용 여부 등
"""
import pandas as pd
import numpy as np
import os
import re

CAPSTONE_DIR = '/home/ubuntu/capstone'
DATA_PATH = os.path.join(CAPSTONE_DIR, 'analysis_dataset_FINAL_v4.csv')
RESULTS = {}

print("=" * 70)
print("데이터 및 코드 품질 검증 보고서")
print("=" * 70)

# ── 1. 데이터 로드 ──────────────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH)
print(f"\n[1] 데이터 기본 정보")
print(f"  Shape: {df.shape}")
print(f"  Unique regions: {df['region_code'].nunique()}")
print(f"  Years: {sorted(df['year'].unique())}")
print(f"  완전균형패널: {df.groupby('region_code')['year'].count().eq(18).all()}")

# ── 2. net_rate 계산식 검증 ─────────────────────────────────────────────────
print(f"\n[2] net_rate 계산식 검증 (net/population × 1000 = ‰)")
df['net_rate_check'] = df['net'] / df['population'] * 1000
df['net_rate_diff'] = (df['net_rate'] - df['net_rate_check']).abs()

# 오차 분포
max_diff = df['net_rate_diff'].max()
mean_diff = df['net_rate_diff'].mean()
n_exact = (df['net_rate_diff'] < 0.01).sum()
n_total = len(df)

print(f"  최대 오차: {max_diff:.6f}")
print(f"  평균 오차: {mean_diff:.6f}")
print(f"  오차 < 0.01인 행: {n_exact}/{n_total} ({n_exact/n_total*100:.1f}%)")

# 오차 큰 상위 5개
large_diff = df[df['net_rate_diff'] > 0.1][['region_code','sgg_name','year','net','population','net_rate','net_rate_check','net_rate_diff']].sort_values('net_rate_diff', ascending=False).head(5)
if len(large_diff) > 0:
    print(f"\n  오차 > 0.1인 사례 (상위 5개):")
    print(large_diff.to_string(index=False))
else:
    print(f"  → 오차 > 0.1인 사례 없음. 계산식 정확성 확인됨.")

RESULTS['net_rate_check'] = {
    'max_diff': round(max_diff, 6),
    'mean_diff': round(mean_diff, 6),
    'exact_match_pct': round(n_exact/n_total*100, 1)
}

# ── 3. population 변수 중복 확인 ────────────────────────────────────────────
print(f"\n[3] population 변수 중복 확인")
pop_cols = [c for c in df.columns if 'pop' in c.lower() and 'ratio' not in c.lower() and 'density' not in c.lower()]
print(f"  pop 관련 컬럼: {pop_cols}")
if 'pop' in df.columns and 'population' in df.columns:
    corr = df[['pop','population']].corr().iloc[0,1]
    print(f"  pop vs population 상관: {corr:.4f}")
    print(f"  → 중복 변수 존재. 'population'으로 통일 권장.")
    RESULTS['pop_duplicate'] = True
else:
    print(f"  → 'population' 단일 변수만 존재. 중복 없음.")
    RESULTS['pop_duplicate'] = False

# ── 4. 고결측 변수 점검 ─────────────────────────────────────────────────────
print(f"\n[4] 고결측 변수 점검 (결측률 > 10%)")
missing_rates = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
high_missing = missing_rates[missing_rates > 10]
if len(high_missing) > 0:
    print(f"  결측률 > 10% 변수:")
    for col, rate in high_missing.items():
        print(f"    {col}: {rate:.1f}%")
else:
    print(f"  결측률 > 10% 변수 없음.")

# 특정 변수 확인
for var in ['univ_student', 'housing_per1k', 'worker_count', 'employ_rate', 'apt_price']:
    if var in df.columns:
        miss = df[var].isnull().sum() / len(df) * 100
        print(f"  {var}: {miss:.1f}% 결측")

RESULTS['high_missing_vars'] = high_missing.to_dict()

# ── 5. DiGraph 사용 여부 코드 점검 ─────────────────────────────────────────
print(f"\n[5] 네트워크 분석 코드 품질 점검")
script_dirs = [
    os.path.join(CAPSTONE_DIR, 'scripts'),
    CAPSTONE_DIR
]
digraph_files = []
graph_files = []
pagerank_weight_ok = []
pagerank_weight_missing = []

for d in script_dirs:
    if not os.path.exists(d):
        continue
    for root, dirs, files in os.walk(d):
        for fname in files:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        code = f.read()
                    if 'DiGraph' in code:
                        digraph_files.append(fname)
                    if 'nx.Graph()' in code and 'DiGraph' not in code and 'networkx' in code:
                        graph_files.append(fname)
                    if 'pagerank' in code.lower() and ('weight=' in code):
                        pagerank_weight_ok.append(fname)
                    elif 'pagerank' in code.lower() and 'weight=' not in code:
                        pagerank_weight_missing.append(fname)
                except:
                    pass

print(f"  DiGraph() 사용 파일: {digraph_files[:5]}")
print(f"  Graph() 사용 파일(방향성 없음, 주의): {graph_files[:5]}")
print(f"  PageRank weight= 지정 파일: {pagerank_weight_ok[:5]}")
print(f"  PageRank weight= 미지정 파일: {pagerank_weight_missing[:5]}")

# ── 6. FE 모형 코드 점검 ────────────────────────────────────────────────────
print(f"\n[6] FE 모형 코드 점검")
fe_files = []
entity_time_fe = []
for d in script_dirs:
    if not os.path.exists(d):
        continue
    for root, dirs, files in os.walk(d):
        for fname in files:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        code = f.read()
                    if 'EntityEffects' in code or 'entity_effects' in code:
                        fe_files.append(fname)
                    if ('EntityEffects' in code or 'entity_effects' in code) and \
                       ('TimeEffects' in code or 'time_effects' in code):
                        entity_time_fe.append(fname)
                except:
                    pass

print(f"  Entity FE 사용 파일: {fe_files[:5]}")
print(f"  Entity+Time FE 모두 사용 파일: {entity_time_fe[:5]}")

# ── 7. ML Time-series split 점검 ────────────────────────────────────────────
print(f"\n[7] ML Time-series split 점검")
ts_split_files = []
group_ts_files = []
for d in script_dirs:
    if not os.path.exists(d):
        continue
    for root, dirs, files in os.walk(d):
        for fname in files:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        code = f.read()
                    if 'TimeSeriesSplit' in code:
                        ts_split_files.append(fname)
                    if 'GroupTimeSeriesSplit' in code or 'GroupKFold' in code:
                        group_ts_files.append(fname)
                except:
                    pass

print(f"  TimeSeriesSplit 사용 파일: {ts_split_files[:5]}")
print(f"  GroupTimeSeriesSplit/GroupKFold 사용 파일: {group_ts_files[:5]}")

# ── 8. in_rate / out_rate 계산식 검증 ──────────────────────────────────────
print(f"\n[8] in_rate / out_rate 계산식 검증")
if 'gross_in' in df.columns and 'in_rate' in df.columns:
    df['in_rate_check'] = df['gross_in'] / df['population'] * 1000
    df['in_rate_diff'] = (df['in_rate'] - df['in_rate_check']).abs()
    print(f"  in_rate 최대 오차: {df['in_rate_diff'].max():.6f}")
    print(f"  in_rate 평균 오차: {df['in_rate_diff'].mean():.6f}")
if 'gross_out' in df.columns and 'out_rate' in df.columns:
    df['out_rate_check'] = df['gross_out'] / df['population'] * 1000
    df['out_rate_diff'] = (df['out_rate'] - df['out_rate_check']).abs()
    print(f"  out_rate 최대 오차: {df['out_rate_diff'].max():.6f}")
    print(f"  out_rate 평균 오차: {df['out_rate_diff'].mean():.6f}")

# ── 9. closeness 정규화 여부 ────────────────────────────────────────────────
print(f"\n[9] closeness 정규화 여부 확인")
if 'closeness' in df.columns:
    c_min = df['closeness'].min()
    c_max = df['closeness'].max()
    c_mean = df['closeness'].mean()
    print(f"  closeness 범위: {c_min:.2f} ~ {c_max:.2f}, 평균: {c_mean:.2f}")
    if c_max > 10:
        print(f"  → 비정규화 상태 (50~450 범위). 표준화 필요.")
    else:
        print(f"  → 정규화 완료 (0~1 범위).")

print(f"\n{'='*70}")
print("검증 완료")
print(f"{'='*70}")
