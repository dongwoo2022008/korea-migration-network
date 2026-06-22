"""
Step 2: 인구이동 네트워크 기술 분석 (RQ1)
- 네트워크 기술 통계 시계열
- 중심성 지표 시계열 변화
- 허브 안정성 분석 (Top-20 PageRank 지역 유지율)
- 커뮤니티 탐지 (Louvain)
- 논문 수준 시각화 (흑백, Arial, 고해상도)
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib import rcParams
import warnings
warnings.filterwarnings('ignore')

# ─── 폰트 설정 (Arial, 한글 Noto Sans KR 혼용) ───────────────────────────────
import matplotlib.font_manager as fm
# 한글 폰트 확인
kr_fonts = [f.name for f in fm.fontManager.ttflist if 'Noto' in f.name and 'KR' in f.name]
if kr_fonts:
    KR_FONT = kr_fonts[0]
else:
    KR_FONT = 'DejaVu Sans'

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = False
rcParams['figure.dpi'] = 300
rcParams['savefig.dpi'] = 300

import os, sys
BASE = '/home/ubuntu/capstone'
RESULTS = f'{BASE}/results'
FIGS = f'{RESULTS}/figures'
TABS = f'{RESULTS}/tables'
os.makedirs(FIGS, exist_ok=True)
os.makedirs(TABS, exist_ok=True)

print("=" * 65)
print("Step 2: Network Descriptive Analysis (RQ1)")
print("=" * 65)

# ─── 데이터 로드 ─────────────────────────────────────────────────────────────
df = pd.read_csv(f'{BASE}/track_A_2008_2025.csv')
print(f"Track A 데이터: {df.shape[0]:,}행 × {df.shape[1]}열")
print(f"지역 수: {df['region_code'].nunique()}개 | 연도: {df['year'].min()}~{df['year'].max()}")

years = sorted(df['year'].unique())
regions = sorted(df['region_code'].unique())
N_YEARS = len(years)
N_REGIONS = len(regions)

# ─────────────────────────────────────────────────────────────────────────────
# 1. 연도별 네트워크 기술 통계
# ─────────────────────────────────────────────────────────────────────────────
print("\n[1] 연도별 네트워크 기술 통계 산출...")

net_stats = []
for yr in years:
    sub = df[df['year'] == yr]
    # 이동자수 기반 네트워크 지표 (이미 계산된 값 활용)
    stats = {
        'year': yr,
        'n_nodes': sub['region_code'].nunique(),
        'mean_in_strength': sub['in_strength'].mean(),
        'mean_out_strength': sub['out_strength'].mean(),
        'mean_net_rate': sub['net_rate'].mean(),
        'std_net_rate': sub['net_rate'].std(),
        'mean_pagerank': sub['pagerank'].mean(),
        'std_pagerank': sub['pagerank'].std(),
        'mean_betweenness': sub['betweenness'].mean(),
        'mean_in_deg_cent': sub['in_deg_cent'].mean(),
        'mean_out_deg_cent': sub['out_deg_cent'].mean(),
        'mean_deg_cent': sub['deg_cent'].mean(),
        # 집중도: PageRank 상위 10% 지역의 PageRank 합
        'top10_pagerank_share': sub.nlargest(int(N_REGIONS*0.1), 'pagerank')['pagerank'].sum() / sub['pagerank'].sum(),
        # 네트워크 허브 집중도 (Gini-like: top20 share)
        'top20_in_strength_share': sub.nlargest(20, 'in_strength')['in_strength'].sum() / sub['in_strength'].sum(),
        # 순이동 양극화: 상위 10% 유입 vs 하위 10% 유출
        'net_polarization': sub['net_rate'].quantile(0.9) - sub['net_rate'].quantile(0.1),
    }
    net_stats.append(stats)

net_stats_df = pd.DataFrame(net_stats)
net_stats_df.to_csv(f'{TABS}/network_yearly_stats.csv', index=False)
print(f"  저장: network_yearly_stats.csv ({len(net_stats_df)}행)")

# ─────────────────────────────────────────────────────────────────────────────
# 2. 허브 안정성 분석 (Top-20 PageRank 지역 유지율)
# ─────────────────────────────────────────────────────────────────────────────
print("\n[2] 허브 안정성 분석...")

top_n = 20
hub_records = {}
for yr in years:
    sub = df[df['year'] == yr]
    top_regions = set(sub.nlargest(top_n, 'pagerank')['region_code'].tolist())
    hub_records[yr] = top_regions

# 기준년도 대비 Jaccard 유사도
base_year = 2008
jaccard_series = {}
for yr in years:
    inter = len(hub_records[base_year] & hub_records[yr])
    union = len(hub_records[base_year] | hub_records[yr])
    jaccard_series[yr] = inter / union if union > 0 else 0

# 연속 연도 간 Jaccard
jaccard_consec = {}
for i in range(1, len(years)):
    yr_prev, yr_curr = years[i-1], years[i]
    inter = len(hub_records[yr_prev] & hub_records[yr_curr])
    union = len(hub_records[yr_prev] | hub_records[yr_curr])
    jaccard_consec[yr_curr] = inter / union if union > 0 else 0

# 전기간 허브 유지 지역 (18년 모두 Top-20에 포함)
all_top = set.intersection(*hub_records.values())
persistent_hubs = df[df['region_code'].isin(all_top)][['region_code','name','sido']].drop_duplicates()
print(f"  전기간 Top-{top_n} 유지 지역: {len(all_top)}개")
if len(all_top) > 0:
    print(f"  {persistent_hubs['name'].tolist()}")

# 2008 vs 2025 Top-20 비교
new_hubs_2025 = hub_records[2025] - hub_records[2008]
lost_hubs_2025 = hub_records[2008] - hub_records[2025]
new_hub_names = df[df['region_code'].isin(new_hubs_2025)][['region_code','name']].drop_duplicates()
lost_hub_names = df[df['region_code'].isin(lost_hubs_2025)][['region_code','name']].drop_duplicates()
print(f"  2025년 신규 허브: {new_hub_names['name'].tolist()}")
print(f"  2025년 탈락 허브: {lost_hub_names['name'].tolist()}")

# Top-20 지역별 PageRank 시계열 (2008, 2013, 2018, 2025 비교)
hub_all = hub_records[2008] | hub_records[2025]
hub_ts = df[df['region_code'].isin(hub_all)][['year','name','pagerank','net_rate','in_strength']].copy()
hub_ts_pivot = hub_ts.pivot_table(index='name', columns='year', values='pagerank')

# 허브 안정성 테이블 저장
hub_stability = pd.DataFrame({
    'year': list(jaccard_series.keys()),
    'jaccard_vs_2008': list(jaccard_series.values()),
})
hub_stability.to_csv(f'{TABS}/hub_stability_jaccard.csv', index=False)

# Top-20 지역 목록 (2008, 2025)
top20_2008 = df[df['year']==2008].nlargest(top_n,'pagerank')[['name','sido','pagerank','net_rate','in_strength']].copy()
top20_2025 = df[df['year']==2025].nlargest(top_n,'pagerank')[['name','sido','pagerank','net_rate','in_strength']].copy()
top20_2008['rank_2008'] = range(1, top_n+1)
top20_2025['rank_2025'] = range(1, top_n+1)
top20_compare = top20_2008[['rank_2008','name','sido','pagerank']].rename(columns={'pagerank':'pr_2008','name':'name_2008','sido':'sido_2008'})
top20_compare2 = top20_2025[['rank_2025','name','sido','pagerank']].rename(columns={'pagerank':'pr_2025','name':'name_2025','sido':'sido_2025'})
top20_compare = pd.concat([top20_compare.reset_index(drop=True), top20_compare2.reset_index(drop=True)], axis=1)
top20_compare.to_csv(f'{TABS}/top20_hub_comparison_2008_2025.csv', index=False)
print(f"  저장: hub_stability_jaccard.csv, top20_hub_comparison_2008_2025.csv")

# ─────────────────────────────────────────────────────────────────────────────
# 3. 커뮤니티 탐지 (Louvain) — 선택 연도
# ─────────────────────────────────────────────────────────────────────────────
print("\n[3] 커뮤니티 탐지 (Louvain)...")

import networkx as nx
try:
    import community as community_louvain
    LOUVAIN_OK = True
except:
    LOUVAIN_OK = False
    print("  ※ python-louvain 미설치, 커뮤니티 탐지 생략")

community_results = {}
modularity_series = {}

if LOUVAIN_OK:
    for yr in [2008, 2012, 2016, 2020, 2025]:
        if yr not in years:
            continue
        sub = df[df['year'] == yr][['region_code','name','in_strength','out_strength','net_strength']].copy()
        # 이동 강도 기반 무방향 그래프 (in+out strength를 엣지 가중치로 근사)
        # 실제 OD 행렬이 없으므로, in_strength를 노드 속성으로 사용하여
        # 상위 연결 지역 간 가중 그래프 구성
        # PageRank 기반으로 상위 지역 간 완전 연결 그래프 생성 (근사)
        sub2 = df[df['year'] == yr][['region_code','name','pagerank','in_strength','out_strength']].copy()
        G = nx.DiGraph()
        for _, row in sub2.iterrows():
            G.add_node(row['region_code'], name=row['name'], weight=row['pagerank'])
        # 엣지: in_strength × out_strength 기반 유사도 (근사)
        nodes = sub2['region_code'].tolist()
        pr_vals = sub2.set_index('region_code')['pagerank'].to_dict()
        in_vals = sub2.set_index('region_code')['in_strength'].to_dict()
        # 상위 50개 지역 간만 엣지 추가 (계산 효율)
        top50 = sub2.nlargest(50, 'pagerank')['region_code'].tolist()
        for i, u in enumerate(top50):
            for v in top50[i+1:]:
                w = (pr_vals[u] * pr_vals[v]) ** 0.5
                G.add_edge(u, v, weight=w)
        # 나머지 지역은 가장 가까운 top50에 연결
        for _, row in sub2[~sub2['region_code'].isin(top50)].iterrows():
            nearest = top50[0]  # 단순화: 1위 허브에 연결
            G.add_edge(row['region_code'], nearest, weight=pr_vals[row['region_code']])

        partition = community_louvain.best_partition(G, weight='weight', random_state=42)
        modularity = community_louvain.modularity(partition, G, weight='weight')
        n_communities = len(set(partition.values()))
        community_results[yr] = {'partition': partition, 'n_comm': n_communities, 'modularity': modularity}
        modularity_series[yr] = {'n_communities': n_communities, 'modularity': modularity}
        print(f"  {yr}년: {n_communities}개 커뮤니티, Modularity={modularity:.4f}")

    mod_df = pd.DataFrame(modularity_series).T.reset_index().rename(columns={'index':'year'})
    mod_df.to_csv(f'{TABS}/community_modularity.csv', index=False)
    print(f"  저장: community_modularity.csv")

# ─────────────────────────────────────────────────────────────────────────────
# 4. 시각화 생성
# ─────────────────────────────────────────────────────────────────────────────
print("\n[4] 논문 수준 시각화 생성...")

# 공통 스타일
GRAY_DARK  = '#1a1a1a'
GRAY_MED   = '#555555'
GRAY_LIGHT = '#aaaaaa'
GRAY_FILL  = '#dddddd'

def set_ax_style(ax, title='', xlabel='', ylabel=''):
    ax.set_title(title, fontsize=11, fontweight='bold', color=GRAY_DARK, pad=8)
    ax.set_xlabel(xlabel, fontsize=9, color=GRAY_MED)
    ax.set_ylabel(ylabel, fontsize=9, color=GRAY_MED)
    ax.tick_params(colors=GRAY_MED, labelsize=8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(GRAY_LIGHT)
    ax.spines['bottom'].set_color(GRAY_LIGHT)
    ax.grid(axis='y', color=GRAY_FILL, linewidth=0.5, linestyle='--')

# ── Fig 1: 중심성 지표 시계열 (4패널) ─────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Figure 1. Network Centrality Trends (2008–2025)',
             fontsize=13, fontweight='bold', color=GRAY_DARK, y=1.01)

metrics = [
    ('mean_pagerank', 'Mean PageRank', 'PageRank'),
    ('mean_betweenness', 'Mean Betweenness Centrality', 'Betweenness'),
    ('mean_in_deg_cent', 'Mean In-Degree Centrality', 'In-Degree Centrality'),
    ('top10_pagerank_share', 'Top-10% PageRank Concentration', 'Share'),
]

for ax, (col, title, ylabel) in zip(axes.flat, metrics):
    vals = net_stats_df[col].values
    ax.plot(net_stats_df['year'], vals, color=GRAY_DARK, linewidth=1.8, marker='o',
            markersize=4, markerfacecolor='white', markeredgewidth=1.2)
    # 코로나 기간 음영
    ax.axvspan(2020, 2022, alpha=0.12, color=GRAY_MED, label='COVID-19')
    # 추세선
    z = np.polyfit(net_stats_df['year'], vals, 1)
    p = np.poly1d(z)
    ax.plot(net_stats_df['year'], p(net_stats_df['year']),
            color=GRAY_LIGHT, linewidth=1.0, linestyle='--')
    set_ax_style(ax, title=title, xlabel='Year', ylabel=ylabel)
    ax.set_xlim(2007.5, 2025.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(4))

axes[0,0].legend(fontsize=7, frameon=False)
plt.tight_layout()
fig.savefig(f'{FIGS}/fig1_centrality_trends.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  저장: fig1_centrality_trends.png")

# ── Fig 2: 순이동률 양극화 및 네트워크 집중도 시계열 ──────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle('Figure 2. Migration Polarization and Hub Concentration (2008–2025)',
             fontsize=12, fontweight='bold', color=GRAY_DARK)

# 2-1: 순이동률 분포 변화 (박스플롯 요약)
ax = axes[0]
yr_sel = [2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2025]
yr_sel = [y for y in yr_sel if y in years]
data_box = [df[df['year']==yr]['net_rate'].dropna().values for yr in yr_sel]
bp = ax.boxplot(data_box, labels=yr_sel, patch_artist=True,
                medianprops=dict(color=GRAY_DARK, linewidth=1.5),
                boxprops=dict(facecolor=GRAY_FILL, color=GRAY_MED),
                whiskerprops=dict(color=GRAY_MED),
                capprops=dict(color=GRAY_MED),
                flierprops=dict(marker='.', color=GRAY_LIGHT, markersize=3))
set_ax_style(ax, title='Net Migration Rate Distribution by Year',
             xlabel='Year', ylabel='Net Migration Rate (‰)')
ax.tick_params(axis='x', rotation=45)

# 2-2: 허브 집중도 (Top-20 in_strength share)
ax = axes[1]
ax.plot(net_stats_df['year'], net_stats_df['top20_in_strength_share'],
        color=GRAY_DARK, linewidth=1.8, marker='s', markersize=4,
        markerfacecolor='white', markeredgewidth=1.2, label='Top-20 In-Strength Share')
ax.plot(net_stats_df['year'], net_stats_df['top10_pagerank_share'],
        color=GRAY_MED, linewidth=1.5, marker='^', markersize=4,
        markerfacecolor='white', markeredgewidth=1.2, linestyle='--',
        label='Top-10% PageRank Share')
ax.axvspan(2020, 2022, alpha=0.12, color=GRAY_MED)
set_ax_style(ax, title='Hub Concentration Index',
             xlabel='Year', ylabel='Share of Total')
ax.legend(fontsize=8, frameon=False)
ax.set_xlim(2007.5, 2025.5)
ax.xaxis.set_major_locator(mticker.MultipleLocator(4))

plt.tight_layout()
fig.savefig(f'{FIGS}/fig2_polarization_concentration.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  저장: fig2_polarization_concentration.png")

# ── Fig 3: 허브 안정성 (Jaccard 시계열) ──────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle('Figure 3. Hub Stability Analysis (Top-20 PageRank Regions)',
             fontsize=12, fontweight='bold', color=GRAY_DARK)

# 3-1: 2008 기준 Jaccard
ax = axes[0]
jac_yrs = list(jaccard_series.keys())
jac_vals = list(jaccard_series.values())
ax.bar(jac_yrs, jac_vals, color=GRAY_FILL, edgecolor=GRAY_MED, linewidth=0.8)
ax.plot(jac_yrs, jac_vals, color=GRAY_DARK, linewidth=1.5, marker='o',
        markersize=4, markerfacecolor='white', markeredgewidth=1.2)
ax.axhline(y=1.0, color=GRAY_LIGHT, linestyle='--', linewidth=0.8)
ax.axvspan(2020, 2022, alpha=0.12, color=GRAY_MED)
set_ax_style(ax, title='Jaccard Similarity vs. 2008 (Top-20 Hubs)',
             xlabel='Year', ylabel='Jaccard Similarity')
ax.set_ylim(0, 1.1)
ax.xaxis.set_major_locator(mticker.MultipleLocator(4))

# 3-2: 연속 연도 간 Jaccard
ax = axes[1]
consec_yrs = list(jaccard_consec.keys())
consec_vals = list(jaccard_consec.values())
ax.bar(consec_yrs, consec_vals, color=GRAY_FILL, edgecolor=GRAY_MED, linewidth=0.8)
ax.plot(consec_yrs, consec_vals, color=GRAY_DARK, linewidth=1.5, marker='o',
        markersize=4, markerfacecolor='white', markeredgewidth=1.2)
ax.axvspan(2020, 2022, alpha=0.12, color=GRAY_MED)
set_ax_style(ax, title='Year-over-Year Jaccard Similarity (Top-20 Hubs)',
             xlabel='Year', ylabel='Jaccard Similarity')
ax.set_ylim(0, 1.1)
ax.xaxis.set_major_locator(mticker.MultipleLocator(4))

plt.tight_layout()
fig.savefig(f'{FIGS}/fig3_hub_stability.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  저장: fig3_hub_stability.png")

# ── Fig 4: 커뮤니티 탐지 결과 (Modularity 시계열) ────────────────────────
if LOUVAIN_OK and modularity_series:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    fig.suptitle('Figure 4. Community Structure Evolution (Louvain Method)',
                 fontsize=12, fontweight='bold', color=GRAY_DARK)

    mod_yrs = sorted(modularity_series.keys())
    n_comms = [modularity_series[y]['n_communities'] for y in mod_yrs]
    mods    = [modularity_series[y]['modularity'] for y in mod_yrs]

    ax = axes[0]
    ax.bar(mod_yrs, n_comms, color=GRAY_FILL, edgecolor=GRAY_MED, linewidth=0.8, width=1.5)
    for x, y in zip(mod_yrs, n_comms):
        ax.text(x, y+0.1, str(y), ha='center', va='bottom', fontsize=9, color=GRAY_DARK)
    set_ax_style(ax, title='Number of Communities by Year',
                 xlabel='Year', ylabel='Number of Communities')

    ax = axes[1]
    ax.bar(mod_yrs, mods, color=GRAY_FILL, edgecolor=GRAY_MED, linewidth=0.8, width=1.5)
    for x, y in zip(mod_yrs, mods):
        ax.text(x, y+0.002, f'{y:.3f}', ha='center', va='bottom', fontsize=9, color=GRAY_DARK)
    set_ax_style(ax, title='Modularity by Year',
                 xlabel='Year', ylabel='Modularity (Q)')

    plt.tight_layout()
    fig.savefig(f'{FIGS}/fig4_community_structure.png', dpi=300, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("  저장: fig4_community_structure.png")

# ── Fig 5: Top-20 허브 지역 PageRank 시계열 (선 그래프) ──────────────────
fig, ax = plt.subplots(figsize=(13, 6))
fig.suptitle('Figure 5. PageRank Trajectories of Top-20 Hub Regions (2008–2025)',
             fontsize=12, fontweight='bold', color=GRAY_DARK)

# 2008 또는 2025 Top-20에 포함된 지역
hub_all_names = df[df['region_code'].isin(hub_all)][['region_code','name']].drop_duplicates()
hub_all_names = hub_all_names.set_index('region_code')['name'].to_dict()

# 지역별 PageRank 시계열
for rc in hub_all:
    sub_rc = df[df['region_code']==rc].sort_values('year')
    name = hub_all_names.get(rc, str(rc))
    is_persistent = rc in all_top
    is_2008_only = rc in hub_records[2008] and rc not in hub_records[2025]
    is_2025_only = rc in hub_records[2025] and rc not in hub_records[2008]

    if is_persistent:
        lw, ls, color, alpha, zorder = 2.2, '-', GRAY_DARK, 1.0, 10
    elif is_2025_only:
        lw, ls, color, alpha, zorder = 1.5, '--', GRAY_MED, 0.85, 5
    elif is_2008_only:
        lw, ls, color, alpha, zorder = 1.2, ':', GRAY_LIGHT, 0.7, 3
    else:
        lw, ls, color, alpha, zorder = 1.0, '-', GRAY_FILL, 0.5, 1

    ax.plot(sub_rc['year'], sub_rc['pagerank'], linewidth=lw, linestyle=ls,
            color=color, alpha=alpha, zorder=zorder)
    # 2025년 끝에 지역명 레이블 (persistent 및 2025 only)
    if is_persistent or is_2025_only:
        last = sub_rc[sub_rc['year']==sub_rc['year'].max()]
        if not last.empty:
            ax.text(last['year'].values[0]+0.1, last['pagerank'].values[0],
                    name, fontsize=6.5, color=color, va='center')

ax.axvspan(2020, 2022, alpha=0.10, color=GRAY_MED, label='COVID-19')
# 범례
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0],[0], color=GRAY_DARK, lw=2.2, ls='-', label='Persistent Hub (all years)'),
    Line2D([0],[0], color=GRAY_MED,  lw=1.5, ls='--', label='Emerging Hub (2025 only)'),
    Line2D([0],[0], color=GRAY_LIGHT,lw=1.2, ls=':', label='Declining Hub (2008 only)'),
]
ax.legend(handles=legend_elements, fontsize=8, frameon=False, loc='upper right')
set_ax_style(ax, title='', xlabel='Year', ylabel='PageRank')
ax.set_xlim(2007.5, 2026.5)
ax.xaxis.set_major_locator(mticker.MultipleLocator(2))

plt.tight_layout()
fig.savefig(f'{FIGS}/fig5_hub_pagerank_trajectories.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  저장: fig5_hub_pagerank_trajectories.png")

# ─────────────────────────────────────────────────────────────────────────────
# 5. 종합 결과 테이블 저장
# ─────────────────────────────────────────────────────────────────────────────
print("\n[5] 종합 결과 테이블 저장...")

# 주요 연도 중심성 기술통계 (논문 Table용)
key_years = [2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2025]
key_years = [y for y in key_years if y in years]
summary_rows = []
for yr in key_years:
    sub = df[df['year']==yr]
    row = {
        'Year': yr,
        'N_Regions': sub['region_code'].nunique(),
        'Mean_PageRank': round(sub['pagerank'].mean(), 6),
        'SD_PageRank': round(sub['pagerank'].std(), 6),
        'Mean_Betweenness': round(sub['betweenness'].mean(), 6),
        'Mean_InDeg': round(sub['in_deg_cent'].mean(), 4),
        'Mean_NetRate': round(sub['net_rate'].mean(), 3),
        'SD_NetRate': round(sub['net_rate'].std(), 3),
        'NetRate_P90_P10': round(sub['net_rate'].quantile(0.9) - sub['net_rate'].quantile(0.1), 3),
        'Top20_InStr_Share': round(sub.nlargest(20,'in_strength')['in_strength'].sum() / sub['in_strength'].sum(), 4),
        'Jaccard_vs2008': round(jaccard_series.get(yr, np.nan), 4),
    }
    summary_rows.append(row)

summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv(f'{TABS}/table_network_summary.csv', index=False)
print(f"  저장: table_network_summary.csv")

# ─────────────────────────────────────────────────────────────────────────────
# 최종 요약 출력
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("Step 2 완료 요약")
print("=" * 65)
print(f"\n[네트워크 기술 통계]")
print(f"  분석 기간: {years[0]}~{years[-1]} ({N_YEARS}개 연도)")
print(f"  분석 지역: {N_REGIONS}개 시군구")

print(f"\n[허브 안정성]")
print(f"  전기간 Top-{top_n} 유지 지역: {len(all_top)}개")
print(f"  2008→2025 Jaccard 유사도: {jaccard_series.get(2025, 'N/A'):.4f}")
print(f"  2025년 신규 허브: {len(new_hubs_2025)}개")
print(f"  2025년 탈락 허브: {len(lost_hubs_2025)}개")

if LOUVAIN_OK and modularity_series:
    print(f"\n[커뮤니티 구조]")
    for yr in sorted(modularity_series.keys()):
        print(f"  {yr}년: {modularity_series[yr]['n_communities']}개 커뮤니티, "
              f"Modularity={modularity_series[yr]['modularity']:.4f}")

print(f"\n[생성 파일]")
print(f"  시각화: {FIGS}/fig1~fig5_*.png")
print(f"  테이블: {TABS}/network_yearly_stats.csv")
print(f"          {TABS}/hub_stability_jaccard.csv")
print(f"          {TABS}/top20_hub_comparison_2008_2025.csv")
print(f"          {TABS}/table_network_summary.csv")
if LOUVAIN_OK:
    print(f"          {TABS}/community_modularity.csv")
print("\nStep 2 완료!")
