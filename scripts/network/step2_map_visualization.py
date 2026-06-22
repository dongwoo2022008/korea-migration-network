"""
Step 2: RQ1 Map Visualization
- Choropleth Map: PageRank (2008, 2015, 2020, 2025)
- Choropleth Map: Net Migration Rate (2008, 2015, 2020, 2025)
- Hub Stability Map: 18-year persistent hubs
- Community Structure Map (2008 vs 2024)
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize, BoundaryNorm
from matplotlib.cm import ScalarMappable
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── 폰트 설정 (Arial / 영문) ──────────────────────────────────────────────────
from matplotlib import font_manager
font_manager.fontManager.addfont('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf')
plt.rcParams['font.family'] = 'Liberation Sans'
plt.rcParams['axes.unicode_minus'] = False

# ── 경로 설정 ─────────────────────────────────────────────────────────────────
DATA_PATH  = '/home/ubuntu/capstone/track_A_2008_2025.csv'
GEO_PATH   = '/home/ubuntu/capstone/data/shp/sgg_municipalities_2018.geojson'
OUT_DIR    = '/home/ubuntu/capstone/results/figures/'

import os; os.makedirs(OUT_DIR, exist_ok=True)

# ── 데이터 로드 ───────────────────────────────────────────────────────────────
df  = pd.read_csv(DATA_PATH)
gdf = gpd.read_file(GEO_PATH)

# ── GeoJSON 집계: 구 단위 → 시 단위 (수원시, 성남시 등) ─────────────────────
# 시 이름 추출 (예: '수원시장안구' → '수원시')
def extract_city(name):
    """시·군·구 이름에서 상위 행정구역 추출"""
    for suffix in ['시', '군']:
        idx = name.find(suffix)
        if idx != -1 and idx < len(name) - 1:
            # 뒤에 구가 붙어있으면 시 단위로 집계
            rest = name[idx+1:]
            if any(c in rest for c in ['구']):
                return name[:idx+1]
    return name

gdf['merge_name'] = gdf['name'].apply(extract_city)

# 구 단위 → 시 단위 geometry 집계 (dissolve)
gdf_city = gdf.dissolve(by='merge_name', as_index=False)[['merge_name', 'geometry']]
gdf_city.columns = ['sgg_name', 'geometry']

# 미추홀구: GeoJSON에는 '남구'로 등록 → 데이터셋 '미추홀구'와 매핑
gdf_city['sgg_name'] = gdf_city['sgg_name'].replace({'남구': '미추홀구'})
print(f"GeoJSON 집계 후 지역수: {len(gdf_city)}")

# ── 헬퍼 함수 ─────────────────────────────────────────────────────────────────
def get_year_data(year, var):
    sub = df[df['year'] == year][['sgg_name', var]].copy()
    merged = gdf_city.merge(sub, on='sgg_name', how='left')
    print(f"  {year}년 {var} 매핑: {merged[var].notna().sum()}/{len(gdf_city)}")
    return merged

def add_map_elements(ax, title, unit=''):
    ax.set_title(title, fontsize=11, fontweight='bold', pad=8)
    ax.set_axis_off()

# ── 그림 1: PageRank Choropleth (4개 연도) ───────────────────────────────────
print("\n[Fig Map1] PageRank Choropleth Map (4 years)")
years = [2008, 2015, 2020, 2025]
fig, axes = plt.subplots(1, 4, figsize=(20, 7))
fig.suptitle('Spatial Distribution of PageRank in Korean Municipal Migration Networks\n(2008, 2015, 2020, 2025)',
             fontsize=13, fontweight='bold', y=1.01)

# 전체 PageRank 범위로 공통 색상 스케일
all_pr = df[df['year'].isin(years)]['pagerank'].dropna()
vmin, vmax = all_pr.quantile(0.02), all_pr.quantile(0.98)
cmap = plt.cm.Greys

for ax, yr in zip(axes, years):
    merged = get_year_data(yr, 'pagerank')
    merged.plot(column='pagerank', ax=ax, cmap=cmap,
                vmin=vmin, vmax=vmax,
                edgecolor='white', linewidth=0.15, missing_kwds={'color':'lightgrey'})
    add_map_elements(ax, str(yr))

# 공통 컬러바
sm = ScalarMappable(cmap=cmap, norm=Normalize(vmin=vmin, vmax=vmax))
sm.set_array([])
cbar = fig.colorbar(sm, ax=axes, orientation='horizontal', fraction=0.02, pad=0.04, shrink=0.6)
cbar.set_label('PageRank Score', fontsize=10)

plt.tight_layout()
plt.savefig(f'{OUT_DIR}fig_map1_pagerank_choropleth.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  → Saved: fig_map1_pagerank_choropleth.png")

# ── 그림 2: 순이동률 Choropleth (4개 연도) ───────────────────────────────────
print("\n[Fig Map2] Net Migration Rate Choropleth Map (4 years)")
fig, axes = plt.subplots(1, 4, figsize=(20, 7))
fig.suptitle('Spatial Distribution of Net Migration Rate (‰) in South Korean Municipalities\n(2008, 2015, 2020, 2025)',
             fontsize=13, fontweight='bold', y=1.01)

all_nr = df[df['year'].isin(years)]['net_rate'].dropna()
vlim = max(abs(all_nr.quantile(0.02)), abs(all_nr.quantile(0.98)))
vlim = min(vlim, 30)  # 극단값 제한
cmap_div = plt.cm.RdGy_r  # 발산형: 빨강(유입) - 흰색 - 회색(유출)

for ax, yr in zip(axes, years):
    merged = get_year_data(yr, 'net_rate')
    merged.plot(column='net_rate', ax=ax, cmap=cmap_div,
                vmin=-vlim, vmax=vlim,
                edgecolor='white', linewidth=0.15, missing_kwds={'color':'lightgrey'})
    add_map_elements(ax, str(yr))

sm2 = ScalarMappable(cmap=cmap_div, norm=Normalize(vmin=-vlim, vmax=vlim))
sm2.set_array([])
cbar2 = fig.colorbar(sm2, ax=axes, orientation='horizontal', fraction=0.02, pad=0.04, shrink=0.6)
cbar2.set_label('Net Migration Rate (‰)', fontsize=10)

plt.tight_layout()
plt.savefig(f'{OUT_DIR}fig_map2_netrate_choropleth.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  → Saved: fig_map2_netrate_choropleth.png")

# ── 그림 3: 허브 안정성 지도 (18년 Top-20 유지 횟수) ─────────────────────────
print("\n[Fig Map3] Hub Stability Map")

# 연도별 Top-20 PageRank 지역 집계
hub_count = {}
for yr in df['year'].unique():
    top20 = df[df['year']==yr].nlargest(20, 'pagerank')['sgg_name'].tolist()
    for r in top20:
        hub_count[r] = hub_count.get(r, 0) + 1

hub_df = pd.DataFrame(list(hub_count.items()), columns=['sgg_name', 'hub_years'])
merged_hub = gdf_city.merge(hub_df, on='sgg_name', how='left')
merged_hub['hub_years'] = merged_hub['hub_years'].fillna(0)

fig, ax = plt.subplots(1, 1, figsize=(10, 12))

# 배경 (비허브 지역)
merged_hub[merged_hub['hub_years'] == 0].plot(
    ax=ax, color='#f0f0f0', edgecolor='white', linewidth=0.2)

# 허브 등급별 색상 (흑백 계열)
bins = [0, 5, 10, 14, 16, 18]
labels = ['1–5 yrs', '6–10 yrs', '11–14 yrs', '15–16 yrs', '17–18 yrs']
colors = ['#d9d9d9', '#969696', '#636363', '#252525', '#000000']

for i, (lo, hi) in enumerate(zip(bins[:-1], bins[1:])):
    sub = merged_hub[(merged_hub['hub_years'] > lo) & (merged_hub['hub_years'] <= hi)]
    if len(sub) > 0:
        sub.plot(ax=ax, color=colors[i], edgecolor='white', linewidth=0.3)

# 범례
patches = [mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(labels))]
patches.insert(0, mpatches.Patch(color='#f0f0f0', label='Non-hub'))
ax.legend(handles=patches, loc='lower right', fontsize=9, title='Hub Duration', title_fontsize=10)

ax.set_title('Hub Stability: Number of Years in Top-20 PageRank\n(2008–2025, N=18 years)',
             fontsize=12, fontweight='bold')
ax.set_axis_off()

plt.tight_layout()
plt.savefig(f'{OUT_DIR}fig_map3_hub_stability.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  → Saved: fig_map3_hub_stability.png")

# ── 그림 4: 순이동률 변화 (2008 → 2024 차이) ─────────────────────────────────
print("\n[Fig Map4] Net Migration Rate Change (2024 - 2008)")

df_2008 = df[df['year']==2008][['sgg_name','net_rate']].rename(columns={'net_rate':'nr_2008'})
df_2024 = df[df['year']==2024][['sgg_name','net_rate']].rename(columns={'net_rate':'nr_2024'})
df_change = df_2008.merge(df_2024, on='sgg_name')
df_change['nr_change'] = df_change['nr_2024'] - df_change['nr_2008']

merged_ch = gdf_city.merge(df_change, on='sgg_name', how='left')

fig, axes = plt.subplots(1, 3, figsize=(18, 8))
fig.suptitle('Net Migration Rate: 2008, 2024, and Change (2024 − 2008)',
             fontsize=13, fontweight='bold', y=1.01)

vlim2 = 25
# 2008
m1 = gdf_city.merge(df[df['year']==2008][['sgg_name','net_rate']], on='sgg_name', how='left')
m1.plot(column='net_rate', ax=axes[0], cmap='RdGy_r', vmin=-vlim2, vmax=vlim2,
        edgecolor='white', linewidth=0.2, missing_kwds={'color':'lightgrey'})
axes[0].set_title('2008', fontsize=11, fontweight='bold'); axes[0].set_axis_off()

# 2024
m2 = gdf_city.merge(df[df['year']==2024][['sgg_name','net_rate']], on='sgg_name', how='left')
m2.plot(column='net_rate', ax=axes[1], cmap='RdGy_r', vmin=-vlim2, vmax=vlim2,
        edgecolor='white', linewidth=0.2, missing_kwds={'color':'lightgrey'})
axes[1].set_title('2024', fontsize=11, fontweight='bold'); axes[1].set_axis_off()

# 변화량
vlim_ch = merged_ch['nr_change'].abs().quantile(0.95)
merged_ch.plot(column='nr_change', ax=axes[2], cmap='RdGy_r', vmin=-vlim_ch, vmax=vlim_ch,
               edgecolor='white', linewidth=0.2, missing_kwds={'color':'lightgrey'})
axes[2].set_title('Change (2024 − 2008)', fontsize=11, fontweight='bold'); axes[2].set_axis_off()

sm3 = ScalarMappable(cmap='RdGy_r', norm=Normalize(vmin=-vlim2, vmax=vlim2))
sm3.set_array([])
cbar3 = fig.colorbar(sm3, ax=axes[:2], orientation='horizontal', fraction=0.03, pad=0.04, shrink=0.8)
cbar3.set_label('Net Migration Rate (‰)', fontsize=9)

sm4 = ScalarMappable(cmap='RdGy_r', norm=Normalize(vmin=-vlim_ch, vmax=vlim_ch))
sm4.set_array([])
cbar4 = fig.colorbar(sm4, ax=axes[2], orientation='horizontal', fraction=0.03, pad=0.04, shrink=0.8)
cbar4.set_label('Change in Net Rate (‰)', fontsize=9)

plt.tight_layout()
plt.savefig(f'{OUT_DIR}fig_map4_netrate_change.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  → Saved: fig_map4_netrate_change.png")

# ── 그림 5: PageRank 변화 (2008 → 2024) ─────────────────────────────────────
print("\n[Fig Map5] PageRank Change (2024 - 2008)")

df_pr08 = df[df['year']==2008][['sgg_name','pagerank']].rename(columns={'pagerank':'pr_2008'})
df_pr24 = df[df['year']==2024][['sgg_name','pagerank']].rename(columns={'pagerank':'pr_2024'})
df_pr_ch = df_pr08.merge(df_pr24, on='sgg_name')
df_pr_ch['pr_change'] = df_pr_ch['pr_2024'] - df_pr_ch['pr_2008']

merged_pr = gdf_city.merge(df_pr_ch, on='sgg_name', how='left')

fig, axes = plt.subplots(1, 3, figsize=(18, 8))
fig.suptitle('PageRank Score: 2008, 2024, and Change (2024 − 2008)',
             fontsize=13, fontweight='bold', y=1.01)

pr_vmin = df[df['year'].isin([2008,2024])]['pagerank'].quantile(0.02)
pr_vmax = df[df['year'].isin([2008,2024])]['pagerank'].quantile(0.98)

m_pr08 = gdf_city.merge(df[df['year']==2008][['sgg_name','pagerank']], on='sgg_name', how='left')
m_pr08.plot(column='pagerank', ax=axes[0], cmap='Greys', vmin=pr_vmin, vmax=pr_vmax,
            edgecolor='white', linewidth=0.2, missing_kwds={'color':'lightgrey'})
axes[0].set_title('2008', fontsize=11, fontweight='bold'); axes[0].set_axis_off()

m_pr24 = gdf_city.merge(df[df['year']==2024][['sgg_name','pagerank']], on='sgg_name', how='left')
m_pr24.plot(column='pagerank', ax=axes[1], cmap='Greys', vmin=pr_vmin, vmax=pr_vmax,
            edgecolor='white', linewidth=0.2, missing_kwds={'color':'lightgrey'})
axes[1].set_title('2024', fontsize=11, fontweight='bold'); axes[1].set_axis_off()

pr_ch_lim = merged_pr['pr_change'].abs().quantile(0.95)
merged_pr.plot(column='pr_change', ax=axes[2], cmap='RdGy_r', vmin=-pr_ch_lim, vmax=pr_ch_lim,
               edgecolor='white', linewidth=0.2, missing_kwds={'color':'lightgrey'})
axes[2].set_title('Change (2024 − 2008)', fontsize=11, fontweight='bold'); axes[2].set_axis_off()

sm5 = ScalarMappable(cmap='Greys', norm=Normalize(vmin=pr_vmin, vmax=pr_vmax))
sm5.set_array([])
cbar5 = fig.colorbar(sm5, ax=axes[:2], orientation='horizontal', fraction=0.03, pad=0.04, shrink=0.8)
cbar5.set_label('PageRank Score', fontsize=9)

sm6 = ScalarMappable(cmap='RdGy_r', norm=Normalize(vmin=-pr_ch_lim, vmax=pr_ch_lim))
sm6.set_array([])
cbar6 = fig.colorbar(sm6, ax=axes[2], orientation='horizontal', fraction=0.03, pad=0.04, shrink=0.8)
cbar6.set_label('Change in PageRank', fontsize=9)

plt.tight_layout()
plt.savefig(f'{OUT_DIR}fig_map5_pagerank_change.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()
print("  → Saved: fig_map5_pagerank_change.png")

print("\n✅ All map visualizations completed!")
print(f"Output directory: {OUT_DIR}")
