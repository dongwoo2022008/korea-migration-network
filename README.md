# 대한민국 시군구 인구이동 네트워크 진화와 지역 흡인력 분석

**부제**: 2006~2025 전국 시군구 패널데이터를 중심으로

---

## 연구 개요

본 연구는 대한민국 229개 시군구를 대상으로 2006~2025년 인구이동 네트워크의 구조적 변화를 분석하고, 지역 흡인력(Regional Attractiveness Index, RAI)의 결정요인을 규명하는 것을 목적으로 한다.

---

## 핵심 연구질문

| RQ | 내용 | 분석 방법 |
|---|---|---|
| RQ1 | 인구이동 네트워크는 2006~2025년 동안 어떻게 변화하였는가? | 네트워크 중심성 분석, 동학 지표 산출 |
| RQ2 | 네트워크 위치(PageRank)는 지역 흡인력에 영향을 미치는가? | Two-way FE (패널 고정효과 모형) |
| RQ3 | 지역 간 인구이동에 공간 파급효과(Spatial Spillover)가 존재하는가? | SDM (공간더빈모형) 직·간접 효과 분해 |
| RQ4 | 연령대별 인구이동 네트워크는 구조적 이질성을 가지는가? | 연령집단별 네트워크 비교 분석 |
| RQ5 | 지역 흡인력 결정요인의 비선형적 구조는 무엇인가? | ML(CatBoost, Test R²=0.293) + SHAP 분석 (1위: 보육시설) |
| RQ6 | 지역 흡인력 결정요인은 시간에 따라 변화하는가? | 기간분할 FE, 연도별 횡단면 OLS |

---

## 데이터 현황

| 구분 | 내용 |
|---|---|
| 분석 단위 | 229개 시군구 × 연도 |
| 분석 기간 | 2008~2025년 (18개 연도) |
| 총 관측치 | 4,122행 |
| 변수 수 | 64개 (종속변수 7개, 네트워크 9개, 통제변수 48개) |
| 최종 데이터 파일 | `data/analysis_dataset_FINAL_v4.csv` |

---

## 3트랙 분석 구조

```
Track A: 네트워크 거시·미시 구조 분석 (2006~2025)
  → RQ1, RQ4: 중심성, 동학 지표, 연령별 네트워크 이질성

Track B: 공간 패널계량모형 (2009~2024)
  → RQ2, RQ3, RQ6: Two-way FE, SDM 효과 분해, 기간분할 추이

Track C: 머신러닝 예측 및 해석 (2017~2024)
  → RQ5: CatBoost + SHAP 기반 비선형 중요도, RAI 지수 구축
```

---

## 디렉토리 구조

```
korea-migration-network/
├── data/                          # 데이터셋
│   ├── analysis_dataset_FINAL_v4.csv   # 최종 분석 데이터 (메인)
│   └── 분석데이터셋_최종_v2.xlsx         # 엑셀 버전 (메타데이터 포함)
├── docs/                          # 연구 문서
│   ├── 01_서론_Introduction.md          # 서론
│   ├── 02_선행연구_Literature.md         # 선행연구 검토
│   ├── 03_방법론_Methodology.md          # 연구설계 및 분석방법
│   ├── 04_연구결과_Results.md            # 분석결과 및 해석
│   ├── 05_결론_Conclusion.md             # 결론 및 정책적 시사점
│   ├── 단계별_분석계획서.md              # 분석 실행 계획서
│   ├── 분석방법론_수정안_초안.md          # 방법론 설계 문서
│   └── 변수_수치_및_출처_검증보고서.md    # 변수 검증 보고서
├── scripts/                       # 분석 스크립트
│   ├── preprocessing/             # 전처리 스크립트
│   ├── network/                   # 네트워크 분석
│   ├── panel/                     # 패널 계량모형
│   └── ml/                        # 머신러닝 분석
├── results/                       # 분석 결과물
│   ├── figures/                   # 시각화 결과
│   └── tables/                    # 통계표
└── README.md
```

---

## 분석 환경

- **언어**: Python 3.11
- **주요 패키지**: pandas, numpy, networkx, scipy, scikit-learn, xgboost, lightgbm, shap, geopandas, matplotlib, seaborn, plotly
- **계량 패키지**: linearmodels, spreg (PySAL)

---

## 진행 현황

- [x] 데이터 수집 및 정제 완료
- [x] 행정구역 개편 크로스워크 적용
- [x] 최종 변수 데이터셋 구축
- [x] 분석 방법론 설계 및 전면 정합화 완료 (6-RQ 체계)
- [x] Step 1: 파생변수 생성 및 전처리
- [x] Step 2: 기술통계 및 EDA
- [x] Step 3: 네트워크 분석 (Track A)
- [x] Step 4: 공간 가중치 행렬 구성 및 LM 검정
- [x] Step 5: 공간 패널계량모형 (Track B)
- [x] Step 6: ML + SHAP (Track C, Time-series split 적용, 누수 제거 pagerank_lag1 기준)
- [x] Step 7: RAI 지수 산출
- [x] Step 8: 논문 초안 작성 완료

---


