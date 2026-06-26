# 그림·표 파일명 정합성 보고서

**작성일**: 2026-06-26  
**커밋**: f4859da  
**대상**: `results/figures/`, `results/tables/`

---

## 1. 그림 파일 정합성 (Figure 4-1 ~ 4-19)

| 논문 번호 | 새 파일명 | 설명 | 상태 |
|-----------|-----------|------|------|
| Figure 4-1 | `fig4_01_network_structure_2008_2025.png` | 네트워크 구조 변화 (2008·2025) | ✅ |
| Figure 4-2 | `fig4_02_pagerank_trends.png` | PageRank 상위 지역 추이 | ✅ |
| Figure 4-3 | `fig4_03_centrality_boxplot.png` | 중심성 지표 박스플롯 | ✅ |
| Figure 4-4 | `fig4_04_louvain_community_2008.png` | Louvain 커뮤니티 지도 (2008) | ✅ |
| Figure 4-5 | `fig4_05_louvain_community_2025.png` | Louvain 커뮤니티 지도 (2025) | ✅ |
| Figure 4-6 | `fig4_06_hhi_concentration_trend.png` | HHI 집중도 추이 | ✅ |
| Figure 4-7 | `fig4_07_freeman_centralization_trend.png` | Freeman 중심화 지수 추이 | ✅ |
| Figure 4-8 | `fig4_08_morans_i_scatter.png` | Moran's I 산점도 | ✅ |
| Figure 4-9 | `fig4_09_lisa_cluster_2008.png` | LISA 군집 지도 (2008) | ✅ |
| Figure 4-10 | `fig4_10_lisa_cluster_2025.png` | LISA 군집 지도 (2025) | ✅ |
| Figure 4-11 | `fig4_11_jaccard_hub_stability.png` | Jaccard 허브 안정성 추이 | ✅ |
| Figure 4-12 | `fig4_12_age_group_net_migration.png` | 연령대별 순이동률 추이 | ✅ |
| Figure 4-13 | `fig4_13_fe_panel_coef.png` | FE 패널 계수 그림 | ✅ |
| Figure 4-14 | `fig4_14_shap_summary.png` | SHAP Summary Plot | ✅ |
| Figure 4-15 | `fig4_15_shap_dependence.png` | SHAP Dependence Plot | ✅ |
| Figure 4-16 | `fig4_16_pagerank_annual_coef.png` | 연도별 PageRank 계수 추이 | ✅ |
| Figure 4-17 | `fig4_17_rai_choropleth.png` | RAI Choropleth 지도 | ✅ |
| Figure 4-18 | `fig4_18_rai_scatter.png` | RAI–순이동률 산점도 | ✅ |
| Figure 4-19 | `fig4_19_rai_subindex_radar.png` | RAI 하위지수 레이더 차트 | ✅ |

**문서 내 경로 전수 검증**: 19건 모두 실제 파일 존재 확인 ✅

---

## 2. 표 파일 정합성 (Table 4-A1~4-20)

| 논문 번호 | 새 파일명 | 설명 | 상태 |
|-----------|-----------|------|------|
| Table 4-A1 | `table4_A1_unit_root_fisher_adf.csv` | Fisher-ADF 패널 단위근 검정 | ✅ |
| Table 4-A2 | `table4_A2_gmm_diagnostics.csv` | GMM 진단 검정 (AR·Sargan·Hansen) | ✅ |
| Table 4-2 | `table4_02_network_yearly_stats.csv` | 연도별 네트워크 통계 | ✅ |
| Table 4-3 | `table4_03_top20_hub_2008_2025.csv` | 상위 20개 허브 비교 (2008·2025) | ✅ |
| Table 4-4 | `table4_04_louvain_community.csv` | Louvain 커뮤니티 모듈성 | ✅ |
| Table 4-5 | `table4_05_morans_i_trend.csv` | Moran's I 연도별 추이 | ✅ |
| Table 4-6 | `table4_06_fe_main_results.csv` | FE 패널 주모형 결과 | ✅ |
| Table 4-11 | `table4_11_age_group_network.csv` | 연령대별 네트워크 지표 | ✅ |
| Table 4-16 | `table4_16_ml_performance.csv` | ML 7모형 성능 비교 | ✅ |
| Table 4-17 | `table4_17_shap_importance.csv` | SHAP 변수 중요도 순위 | ✅ |
| Table 4-18 | `table4_18_period_fe_split.csv` | 기간분할 FE 결과 | ✅ |
| Table 4-19 | `table4_19_period_shap_split.csv` | 기간분할 SHAP 결과 | ✅ |
| Table 4-20 | `table4_20_rai_ranking.csv` | RAI 순위 (상위 10·하위 10) | ✅ |

---

## 3. 아카이브 이동 파일 (`results/figures/_archive/`)

구버전 번호 체계 파일 26건을 `_archive/` 폴더로 이동:

- `fig1_*`, `fig2_*`, `fig3_*` (구버전 장 번호 체계)
- `fig4_1_morans_i_trend.png`, `fig4_4c_*`, `fig4_5_concentration_*` 등 (구버전 번호)
- `fig5_*`, `fig6_*`, `fig7_*` (구버전 장 번호)
- `fig_map1~5_*`, `fig_std_*` (비정형 파일명)

---

## 4. 파일명 규칙 (확정)

```
그림: fig{장번호}_{순번:02d}_{영문설명}.png
표:   table{장번호}_{순번:02d}_{영문설명}.csv
부록: table{장번호}_A{순번}_{영문설명}.csv
```

**예시**: `fig4_01_network_structure_2008_2025.png`, `table4_A1_unit_root_fisher_adf.csv`
