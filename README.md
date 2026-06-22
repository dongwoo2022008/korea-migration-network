# 대한민국 시군구 인구이동 네트워크 진화와 지역 흡인력 분석

**부제**: 2006~2025 전국 시군구 패널데이터를 중심으로

---

## 연구 개요

본 연구는 대한민국 229개 시군구를 대상으로 2006~2025년 인구이동 네트워크의 구조적 변화를 분석하고, 지역 흡인력(Regional Attractiveness Index, RAI)의 결정요인을 규명하는 것을 목적으로 한다.

---

## 핵심 연구질문

| RQ | 내용 | 분석 방법 |
|---|---|---|
| RQ1 | 인구이동 네트워크는 2008~2025년 어떻게 변화하였는가? | 네트워크 기술 분석, 시계열 시각화 |
| RQ2 | 네트워크 위치(PageRank)는 미래 인구 유입에 영향을 미치는가? | Two-way FE, SDM, Dynamic FE-GMM |
| RQ3 | 지역 특성(경제·인구·서비스)은 인구 흡인력에 어떤 영향을 미치는가? | 패널 계량모형 |
| RQ4 | 공간 파급효과(Spatial Spillover)는 존재하는가? | SDM 직접·간접효과 분해 |

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
Track A: 네트워크 기술 분석  (2008~2025, 18년)
  → RQ1: 중심성 변화, 커뮤니티 탐지, 허브 안정성

Track B: 패널 계량모형  (2009~2024, 16년)
  → RQ2~4: Two-way FE → SDM → Dynamic FE-GMM

Track C: ML 확장 분석  (2017~2024, 8년)
  → RQ5: RF/XGB/LGBM + SHAP → RAI 지수 구축
```

---

## 디렉토리 구조

```
korea-migration-network/
├── data/                          # 데이터셋
│   ├── analysis_dataset_FINAL_v4.csv   # 최종 분석 데이터 (메인)
│   └── 분석데이터셋_최종_v2.xlsx         # 엑셀 버전 (메타데이터 포함)
├── docs/                          # 연구 문서
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
- [x] 행정구역 개편 크로스워크 적용 (창원·미추홀·여주·당진·군위)
- [x] 이동률 단위 통일 (‰, 천분율)
- [x] 최종 변수 데이터셋 구축 (64개 변수)
- [x] 분석 방법론 설계 완료
- [ ] Step 1: 파생변수 생성 및 전처리
- [ ] Step 2: 기술통계 및 EDA
- [ ] Step 3: 네트워크 분석 (Track A)
- [ ] Step 4: 공간 가중치 행렬 구성
- [ ] Step 5: 패널 계량모형 (Track B)
- [ ] Step 6: ML + SHAP (Track C)
- [ ] Step 7: RAI 지수 구축
- [ ] Step 8: 논문 작성

---

## 참고

본 연구는 SSCI급 지역·도시·인구 분야 저널 투고를 목표로 한다.
