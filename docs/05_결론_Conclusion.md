# 제5장 결론 (Conclusion)

## 5.1 연구 결과 요약

본 연구는 2006~2025년 대한민국 시군구 인구이동 패널데이터(네트워크 분석: 2006~2025, 패널 회귀: 2009~2024, ML·SHAP: 2017~2024)를 활용하여 인구이동 네트워크의 진화 과정을 추적하고, 지역 흡인력(Regional Attractiveness)의 결정요인을 실증적으로 분석하였다. 네트워크 분석, 공간 패널모형, 머신러닝 및 SHAP 해석기법을 통합적으로 적용하여 도출한 핵심 연구결과는 다음과 같다.

**첫째, 인구이동 네트워크의 거시적 진화와 허브 교체(RQ1)**
대한민국 인구이동 네트워크는 분석 기간(2006~2025년) 동안 거시적 연결망(밀도, 상호성) 측면에서는 포화 상태의 소규모 세상(Small-world) 특성을 유지하며 안정화되어 있었다. 그러나 내부적으로는 PageRank 상위 허브로의 집중도(HHI)가 지속적으로 상승하였으며, 기존 전통적 거점(지방 광역시 중심구)들이 쇠퇴하고 수도권 신도시를 품은 새로운 지역(화성시, 용인시 등)들이 허브로 부상하는 역동적인 재편 과정이 확인되었다. 커뮤니티 탐지 결과, 국토 공간은 수도권 단일 중심이 아니라 6개의 광역 권역 중심 다층적 순환 이동 구조를 형성하고 있었다.

**둘째, 지역 흡인력의 핵심 앵커로서의 네트워크 허브 효과(RQ2)**
패널 양방향 고정효과(Two-way FE) 모형 추정 결과, 이전 연도의 PageRank 중심성이 높을수록 당해 연도의 순이동률(인구 유입)이 유의하게 증가하는 강력한 허브 효과가 확인되었다(Coef. 3,119***). 반면 단순 유입량(In-degree)은 오히려 부(-)의 효과를 보여, 단순한 양적 유입보다는 전체 네트워크에서 '중요한 노드로부터의 질적 연결'을 의미하는 네트워크 위상(PageRank)이 실질적인 인구 흡인력의 핵심 동인임을 입증하였다.

**셋째, 공간 파급효과의 한계와 내부화(RQ3)**
공간더빈모형(SDM)을 통한 직·간접 효과 분해 결과, PageRank 중심성이 인구 유입에 미치는 영향은 거의 전적으로 직접효과(3,519***)에 기인하였으며, 인접 지역으로의 공간적 파급(Spillover)은 통계적으로 유의하지 않거나 미미한 수준의 빨대효과(Straw effect)로 나타났다. 이는 허브 지위가 창출하는 흡인력이 주변 지역으로 확산되기보다는 해당 지역 내부에서 독점적으로 작동함을 의미한다.

**넷째, 생애주기에 따른 네트워크 구조의 이질성(RQ4)**
연령집단별 네트워크 분석 결과, 인구이동은 단일한 흐름이 아니라 연령에 따라 분화된 다층 네트워크임이 규명되었다. 청년층 이동은 총이동량을 압도하며 소수의 수도권 거점(수원, 관악, 화성)으로 극도로 집중(HHI 0.0079)되는 단극화 경향을 보인 반면, 중·고령층은 이동 규모가 상대적으로 작고 권역 내 근거리 이동 중심의 다극적·분산적 군집 구조(Modularity 0.43~0.44)를 보였다. 이는 비수도권 청년 유출과 지방소멸이 청년 네트워크의 구조적 집중성에 기인함을 시사한다.

**다섯째, 머신러닝(CatBoost) 및 SHAP 기반 비선형 결정요인 규명(RQ5)**
트리 기반 앙상블 모형(CatBoost)이 전통적 선형 패널모형(LR) 대비 압도적으로 우수한 예측력(Test R² 0.293 vs 0.001)을 보임으로써, 인구이동 결정요인에 강한 비선형성과 복잡한 상호작용이 존재함을 확인하였다. SHAP 기법을 통해 변수 중요도를 해석한 결과, 보육시설과 노후주택비율이 각각 1, 2위를 차지하였으며 근접 중심성이 3위를 기록하였다. 이는 최근의 인구이동이 단순한 경제적 기회(고용률 등)보다는 주거 쾌적성, 생활SOC, 네트워크 접근성 등 복합적 정주 여건 중심으로 재편되고 있음을 시사한다. 

**여섯째, 결정구조의 시간적 항상성과 팬데믹 충격(RQ6)**
기간분할 패널모형 및 연도별 계수 추이 분석 결과, 네트워크 중심성(PageRank)의 인구 흡인력은 분석 전 기간에 걸쳐 구조적 안정성을 유지하였다. 점진적인 장기 약화 추세는 발견되지 않았으나, COVID-19 팬데믹 기간(2020~2021)에 허브 결정력이 일시적으로 저점을 기록한 후 엔데믹 이후(2022~2024) 다시 회복되는 U자형 궤적을 보였다. 이는 결정구조가 장기적 항상성(resilience)을 가지며, 외생적 충격이 일시적 교란을 가했음을 의미한다.

**일곱째, 지역 흡인력 지수(RAI) 산출 및 매핑**
SHAP 변수 중요도를 기반으로 산출된 지역 흡인력 지수(RAI)는 수도권-비수도권 간의 명확한 이분법적 구조를 공간적으로 시각화하였다. 서비스·주거 영역(36.4%)과 인프라·접근성 영역(27.0%)이 흡인력 격차를 주도하는 것으로 나타났다. RAI와 실제 순이동률 간의 약한 상관(r=0.119)은 RAI가 단기적 이동(부동산 등)보다는 지역의 구조적·잠재적 매력도를 측정하는 지표로서 기능함을 입증한다.

## 5.2 논의 (Discussion)

본 연구의 분석 결과는 기존 연구와 비교하여 다음과 같은 논의점을 제공한다.

첫째, 인구이동 네트워크의 구조적 고착화와 수도권 쏠림이다. 네트워크 분석(RQ1) 결과, 지난 20년간 대한민국 인구이동 네트워크는 수도권 중심의 강한 '허브 앤 스포크(Hub-and-Spoke)' 구조로 고착화되었음을 확인하였다. PageRank 상위 허브 지역의 Jaccard 유사도(2025년 기준 0.379)는 지속적으로 하락하여 허브 교체가 일어났으나, 그 교체의 방향은 화성시, 용인시 등 경기 남부권 거점 도시들이 새로운 핵심 허브로 부상하는 수도권 내부의 재편이었다. 이는 인구이동 네트워크의 불평등 심화를 지적한 선행연구의 주장을 장기 패널 데이터로 입증한 것이다.

둘째, 지역 흡인력의 핵심 앵커로서의 네트워크 위치(RQ2)이다. 패널 양방향 고정효과(Two-way FE) 모형 분석 결과, 지역의 네트워크 중심성(PageRank)은 지역 고유 특성과 연도 효과를 통제한 상태에서도 미래의 인구 순유입을 결정하는 핵심 앵커 요인으로 나타났다(직접효과 3,119***). 이는 단순한 경제·인프라 변수뿐만 아니라, 지역이 인구이동 네트워크 내에서 차지하는 구조적 위치 자체가 일종의 '보이지 않는 인프라'로 작동하여 추가적인 인구 유입을 유발함을 의미한다. 대체 지표 분석에서 In-degree 중심성이 오히려 부(-)의 효과를 보인 점은, 단순한 유입량보다 네트워크 상의 '질적 위상(PageRank)'이 지역 흡인력의 실체임을 방증한다.

셋째, 공간 파급효과의 한계와 내부화(RQ3)이다. 공간 패널모형(SDM) 분석 결과, PageRank의 인접 지역 파급(Spillover)은 통계적으로 유의하지 않거나 미미한 수준의 경쟁·빨대 효과(Straw effect)로 나타났다. 즉 허브 지위의 인구 흡인력은 주로 해당 지역 내부에서 작동하며, 공간적 누출은 약하다. 이러한 발견은 인구 감소 시대의 지역 정책이 개별 지자체 단위의 파편적 접근을 넘어, 네트워크 구조를 고려한 광역적 접근으로 전환되어야 함을 시사한다.

넷째, 생애주기별 이질성과 연령대별 정책의 필요성(RQ4)이다. 연령집단별 분석 결과, 청년 집단의 수도권 초집중은 전연령 네트워크에서 관찰된 집중 패턴을 견인하는 핵심 기제로서, 비수도권 청년 유출과 지방소멸의 네트워크적 토대를 이룬다. 반면 중·고령 이동은 권역 내에서 분산적으로 이루어져, 연령에 따라 차별화된 지역정책(청년: 수도권 집중 완화·지방 정주여건, 고령: 권역 내 의료·복지 접근성)의 필요성을 지지한다.

다섯째, 머신러닝(CatBoost) 및 SHAP 기반 비선형 결정요인의 새로운 해석(RQ5)이다. SHAP 분석 결과, 보육시설과 노후주택비율이 1, 2위를 차지하였다. 이는 최근의 인구이동이 단순한 경제적 기회(고용률 등)보다는 정주 여건(주거환경·보육·의료)과 네트워크 접근성을 포괄하는 영역 수준(Domain-level)의 복합적 환경 중심으로 재편되고 있음을 강력히 시사한다. 이는 머신러닝을 활용하여 인구이동의 비선형적 동인을 분석한 최근의 연구들과 맥락을 같이하며, 한국적 상황에 맞는 변수 중요도를 도출했다는 점에서 학술적 기여가 크다.

여섯째, 결정구조의 시간적 항상성과 팬데믹 충격(RQ6)이다. 네트워크 중심성(PageRank)의 효과는 분석 전 기간에 걸쳐 구조적으로 안정적이었으나, 팬데믹 기간에 일시적 저점을 기록한 후 엔데믹 이후 뚜렷하게 회복되는 U자형 패턴을 보였다. 이는 팬데믹이라는 외생적 충격에 의한 일시적 교란과 그 이후의 복원력(resilience)을 반영한다. 즉, 지역 흡인력의 핵심 동력인 정주 여건과 네트워크 접근성은 장기적 항상성을 유지하는 가운데, 팬데믹을 거치며 인구이동 동기가 삶의 질을 종합적으로 고려하는 방향으로 다원화되고 있다.

일곱째, 지역 흡인력 지수(RAI)의 정책적 활용 가능성이다. RAI는 순이동률과 약한 유의 상관(r=0.119, p<0.05, N=228)을 보였는데, 이는 RAI가 단기 인구 유입률이 아닌 지역의 장기적·구조적 매력도(잠재력)를 측정하는 지표이기 때문이다. 높은 지가·임대료로 인한 전출 압력이 구조적 매력도를 상쇄하는 '매력도-실현 괴리'가 작동하기 때문이다. 따라서 RAI는 중앙정부 차원에서 재원 배분 시 '잠재적 흡인력 개선 가능성'이 높은 지역에 집중 투자하는 보조 지표로 활용될 수 있다.

## 5.3 학술적 및 정책적 기여

**1. 학술적 기여**
본 연구는 20년(2006~2025)에 걸친 시군구 단위 장기 패널데이터를 구축(네트워크 분석 전기간, 패널 회귀 2009~2024, ML 2017~2024)하여 대한민국 인구이동의 거시적 궤적을 실증했다는 점에서 데이터적 기여를 지닌다. 특히, 단순한 유출입량 중심의 기존 연구 한계를 극복하고, PageRank, Modularity, 연령별 다층 네트워크 등 **네트워크 과학(Network Science)의 방법론을 공간계량경제학(Spatial Econometrics)과 결합**하여 지역의 질적 위상(Hub status)이 인구 흡인력의 독립적이고 인과적인 앵커로 작용함을 입증하였다. 아울러, 전통적 선형 모형이 포착하지 못하는 복잡한 결정구조를 **최신 머신러닝 앙상블(CatBoost)과 XAI(SHAP) 기법을 통해 비선형적으로 규명**함으로써, 인구이동 연구의 방법론적 지평을 확장하였다.

**2. 정책적 시사점**
분석 결과는 향후 지방소멸 대응 및 균형발전 정책 수립에 다음과 같은 실천적 시사점을 제공한다.
첫째, 지역 발전 정책의 패러다임 전환이 필요하다. SHAP 분석에서 확인되었듯, 단순한 일자리 창출(경제 요인)만으로는 인구를 유인하기 어렵다. 보육시설, 노후주택 개선, 노인복지시설 등 **생활 밀착형 정주 여건(서비스·주거 영역)의 획기적 개선**이 선행되어야 한다.
둘째, 네트워크 위상을 고려한 거점 육성 전략이 요구된다. PageRank의 강력한 흡인력과 공간 파급효과의 한계(내부화)는, 모든 지역에 예산을 균등 분배하는 '나눠주기식' 정책보다는 **권역별 핵심 허브(초광역권 거점도시)를 집중 육성하여 실질적인 네트워크 중심성을 확보**하는 '압축적 거점 전략(Compact Network Strategy)'이 효과적임을 시사한다.
셋째, 연령대별 타겟팅된 공간 정책이 필요하다. 수도권으로 초집중하는 청년층을 위해서는 지방 거점도시 내 혁신 생태계 조성 및 대학-산업 연계가 시급하며, 권역 내 이동 중심인 중·고령층을 위해서는 근거리 의료·복지 인프라(노인복지시설, 의사수 등) 확충을 통한 '지역사회 계속 거주(Aging in Place)' 지원이 강화되어야 한다.

## 5.4 연구의 한계 및 향후 과제

본 연구는 다음과 같은 한계를 지니며, 이는 향후 후속 연구를 통해 보완되어야 한다.

첫째, 데이터의 공간적 해상도 한계이다. 본 연구는 시군구 단위의 거시적 이동을 분석하였으나, 실제 주거 이동의 의사결정은 읍면동 또는 근린 단위의 미시적 환경(학군, 대중교통 접근성 등)에 크게 좌우된다. 향후 읍면동 단위의 마이크로 데이터를 활용한 다층적(Multi-level) 분석이 요구된다.
둘째, 독립변수 구축의 제약이다. 20년 장기 패널을 구축하는 과정에서 과거 연도의 세부 생활SOC 데이터(예: 스타벅스, 올리브영 등 민간 편의시설)나 미시적 부동산 가격 데이터를 충분히 확보하지 못해 Track C(2017~2024) 등 부분 패널로 분할 분석을 수행하였다. 향후 비정형 데이터(웹 크롤링, 카드 매출 등)를 융합한 변수 확장이 필요하다.
셋째, 인과관계 규명의 한계이다. 시차변수(Lag)와 고정효과(FE)를 통해 내생성을 통제하고자 하였으나, 동적 패널모형(GMM)에서 약한 도구변수 문제가 발생하여 완벽한 인과성(Causality) 입증에는 한계가 있다. 향후 정책 충격(예: 혁신도시 이전, GTX 개통 등)을 활용한 이중차분법(DiD) 등 준실험적(Quasi-experimental) 설계가 보완되어야 할 것이다.
넷째, 지역 흡인력 지수(RAI)의 동태적 활용성이다. 본 연구에서 개발된 RAI는 구조적 잠재력을 평가하는 데 그쳤으나, 향후 시계열 예측 모형과 결합하여 지역별 소멸 위험 시점을 조기 경보하는 모니터링 시스템으로 발전시킬 수 있을 것이다.

## References

<div style="padding-left: 2em; text-indent: -2em;">

이상현, 오윤경. (2017). 시계열 인구이동 자료를 활용한 네트워크 연결중심성 분석. *국토계획*, 52(4), 115-131.

이찬영, 이흥후. (2016). 청년층의 지역 간 인구이동 결정요인 분석. *지역연구*, 32(3), 3-21.

이희연, 황명화. (2011). 전국 시군구의 인구이동 패턴과 공간적 상호작용. *한국경제지리학회지*, 23(4), 605-625.

전명진. (2014). 수도권 인구이동의 결정요인에 관한 연구: 공간계량경제모형의 적용. *국토계획*, 49(5), 97-111.

Abel, G. J., & Sander, N. (2014). Quantifying global international migration flows. *Science*, 343(6178), 1520-1522. https://doi.org/10.1126/science.1248676

Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A next-generation hyperparameter optimization framework. In *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining* (pp. 2623-2631). https://doi.org/10.1145/3292500.3330701

Almquist, Z. W., Brelsford, C., & Jones, J. H. (2024). Uncovering migration systems through spatio-temporal tensor co-clustering. *Scientific Reports*, 14, 26861. https://doi.org/10.1038/s41598-024-78018-8

Anselin, L. (1988). *Spatial Econometrics: Methods and Models*. Kluwer Academic Publishers.

Anselin, L. (1995). Local indicators of spatial association—LISA. *Geographical Analysis*, 27(2), 93-115. https://doi.org/10.1111/j.1538-4632.1995.tb00338.x

Arellano, M., & Bond, S. (1991). Some tests of specification for panel data: Monte Carlo evidence and an application to employment equations. *The Review of Economic Studies*, 58(2), 277-297. https://doi.org/10.2307/2297968

Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509-512. https://doi.org/10.1126/science.286.5439.509

Blondel, V. D., Guillaume, J. L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. *Journal of Statistical Mechanics: Theory and Experiment*, 2008(10), P10008. https://doi.org/10.1088/1742-5468/2008/10/P10008

Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324

Castles, S., de Haas, H., & Miller, M. J. (2014). *The Age of Migration: International Population Movements in the Modern World* (5th ed.). Guilford Press.

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785-794). https://doi.org/10.1145/2939672.2939785

Chen, Y., Tao, R., Ma, Q., & Wang, M. (2025). Shrinking cities in China's urban network: a data-driven exploration of migration and investment flows. *Applied Geography*, 180, 103596. https://doi.org/10.1016/j.apgeog.2025.103596

Danchev, V., & Porter, M. A. (2020). Migration networks: Applications of network analysis to macroscale migration patterns. *Journal of Complex Networks*, 8(1), cnaa018. https://doi.org/10.1093/comnet/cnaa018

Elhorst, J. P. (2014). *Spatial Econometrics: From Cross-Sectional Data to Spatial Panels*. Springer. https://doi.org/10.1007/978-3-642-40340-8

Freeman, L. C. (1978). Centrality in social networks conceptual clarification. *Social Networks*, 1(3), 215-239. https://doi.org/10.1016/0378-8733(78)90021-7

Gürsoy, S., & Badur, D. (2022). Network analysis of internal migration in Turkey. *Physica A: Statistical Mechanics and its Applications*, 596, 127138. https://doi.org/10.1016/j.physa.2022.127138

Haase, A., Haase, A., & Rink, D. (2021). Conceptualizing place attractiveness for migration. *Population, Space and Place*, 27(6), e2427. https://doi.org/10.1002/psp.2427

Im, K. S., Pesaran, M. H., & Shin, Y. (2003). Testing for unit roots in heterogeneous panels. *Journal of Econometrics*, 115(1), 53-74. https://doi.org/10.1016/S0304-4076(03)00092-7

Jeong, S., Kim, Y., & Yoon, J. (2025). Analyzing the Influences of Economic Opportunity and Residential Substitutability on Population Migration by Age Group. *Journal of Korea Planning Association*, 60(4), 38-59.

LeSage, J., & Pace, R. K. (2009). *Introduction to Spatial Econometrics*. CRC Press. https://doi.org/10.1201/9781420064254

Lee, E. S. (1966). A theory of migration. *Demography*, 3(1), 47-57. https://doi.org/10.2307/2060063

Lee, J., Kim, H., & Park, S. (2025). Disaggregating Multifaceted Destination Effects on Residential Migration. *Land*, 14(9), 1833. https://doi.org/10.3390/land14091833

Lee, L. F., & Yu, J. (2010). Estimation of spatial autoregressive panel data models with fixed effects. *Journal of Econometrics*, 154(2), 165-185. https://doi.org/10.1016/j.jeconom.2009.08.001

Levin, A., Lin, C. F., & Chu, C. S. J. (2002). Unit root tests in panel data: asymptotic and finite-sample properties. *Journal of Econometrics*, 108(1), 1-24. https://doi.org/10.1016/S0304-4076(01)00098-7

Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In *Advances in Neural Information Processing Systems* (Vol. 30).

Mabogunje, A. L. (1970). Systems approach to a theory of rural‐urban migration. *Geographical Analysis*, 2(1), 1-18. https://doi.org/10.1111/j.1538-4632.1970.tb00140.x

Massey, D. S., Arango, J., Hugo, G., Kouaouci, A., Pellegrino, A., & Taylor, J. E. (1993). Theories of international migration: A review and appraisal. *Population and Development Review*, 19(3), 431-466. https://doi.org/10.2307/2938462

Niedomysl, T. (2010). Towards a conceptual framework of place attractiveness: A migration perspective. *Geografiska Annaler: Series B, Human Geography*, 92(1), 97-109. https://doi.org/10.1111/j.1468-0467.2010.00335.x

Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). *The PageRank citation ranking: Bringing order to the web*. Stanford InfoLab.

Pitoski, D., Thomas, M. L., & Rozenblat, C. (2021). Migration networks: A PageRank-based approach to internal migration. *Computational Social Networks*, 8(1), 10. https://doi.org/10.1186/s40649-021-00088-2

Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: unbiased boosting with categorical features. In *Advances in Neural Information Processing Systems* (Vol. 31).

Pu, Y., Zhao, X., & Chi, G. (2019). Spatial dynamic panel model of internal migration in China. *Demographic Research*, 41(31), 873-904. https://doi.org/10.4054/DemRes.2019.41.31

Ravenstein, E. G. (1885). The laws of migration. *Journal of the Statistical Society of London*, 48(2), 167-227. https://doi.org/10.2307/2979181

Roberts, M. E., Stewart, B. M., & Tingley, D. (2017). stm: An R package for structural topic models. *Journal of Statistical Software*, 10(2), 1-40.

Sahin, S., Karaman, M. M., & Ozden, C. (2026). Analysing the impact of migration flows on regional per capita GDP in Türkiye: a spatial panel data approach. *Public Sector Economics*, 50(2), 259-286. https://doi.org/10.3326/pse.50.2.4

Sarra, A., D'Ingiullo, D., Evangelista, A., Nissi, E., Quaglione, D., & Di Battista, T. (2025). A network analysis of skill-specific internal migration flows in Italy. *Socio-Economic Planning Sciences*, 100, 102225. https://doi.org/10.1016/j.seps.2025.102225

Shangguan, Z. (2025). An Explainable Machine-Learning Framework Based on XGBoost-SHAP and Big Data for Revealing the Socioeconomic Drivers of Population Urbanization in China. *Systems*, 13(8), 679. https://doi.org/10.3390/systems13080679

Tranos, E., Gheasi, M., & Nijkamp, P. (2015). International migration: A global complex network analysis. *Regional Studies*, 49(1), 4-22. https://doi.org/10.1080/00343404.2014.964666

Wu, J., & Liu, Y. (2022). Stability and change in China's geography of intercity migration. *Population, Space and Place*, 28(6), e2570. https://doi.org/10.1002/psp.2570

Xu, X., Hu, Y., & Wang, F. (2025). Unraveling the COVID-19 impact on spatiotemporal dynamics of U.S. domestic migration: A network perspective. *The Professional Geographer*, 77(2), 104-120. https://doi.org/10.1080/00330124.2025.2455188

de Haas, H. (2010). Migration and development: A theoretical perspective. *International Migration Review*, 36(1), 227-264. https://doi.org/10.1111/j.1747-7379.2010.00804.x

</div>
