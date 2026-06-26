# _archive — 비정본 파일 보관소

> **이 폴더의 파일은 편집하지 마십시오.**
> 정본 파일은 `docs/` 루트의 장별 파일(03~06)입니다.

## 정본 파일 위치

| 장 | 정본 파일 |
|:---:|:---|
| 방법론 | `docs/03_방법론_Methodology.md` |
| 결과 | `docs/04_연구결과_Results.md` |
| 논의 | `docs/05_논의_Discussion.md` |
| 결론 | `docs/06_결론_Conclusion.md` |

## 아카이브 파일 목록

| 파일 | 비고 |
|:---|:---|
| `04_05_06_결과_논의_결론_Results_Discussion_Conclusion.md` | 통합본 — §5·§6은 단독 파일로 분리됨 |
| `paper_final_v2.md` | 초기 통합 원고 v2 — 정본 수치 일부 반영됨 |
| `paper_final_v3.md` | 영문 초록 스텁 v3 — **옛 수치(SHAP=14.38 등) 포함, 사용 금지** |

## 최종 정본 수치 요약 (2025-06-26 기준)

| 항목 | 정본 값 |
|:---|:---|
| SDM 직접효과 (PageRank) | 3,519\*\*\* |
| SDM 간접효과 | −511 (비유의) |
| SDM ρ (Queen W) | −0.070 (비유의, p=0.186) |
| SHAP 1위 | 노후주택비율 house_age (3.662) |
| SHAP 2위 | PageRank (3.434) |
| ML 최고 Test R² | XGBoost 0.454 |
| Moran's I 최고점 | 2011년 0.147\*\*\* |
