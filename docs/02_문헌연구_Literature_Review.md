## 2. 선행연구 검토

### 2.1. 인구이동 이론과 시스템적 접근

인구이동에 관한 이론적 논의는 Ravenstein(1885)의 '이동의 법칙(Laws of Migration)'에서 출발하여, Lee(1966)의 배출-흡인(Push-Pull) 이론으로 정교화되었다. 전통적 이론들은 주로 출발지의 열악한 조건(배출 요인)과 도착지의 매력적인 조건(흡인 요인) 간의 상호작용, 그리고 그 사이에 존재하는 개입 장애물(Intervening obstacles)을 통해 이동의 원인을 설명하였다 [1] [2]. 그러나 이러한 미시적이고 정태적인 접근은 시간이 지남에 따라 이동 흐름이 어떻게 변화하고 스스로를 강화하는지 설명하는 데 한계가 있었다.

이에 대한 대안으로 Mabogunje(1970)는 인구이동을 하나의 복잡한 시스템(Systems approach)으로 파악하고, 농촌-도시 간 이동이 환경과의 상호작용을 통해 자기강화적인 피드백 루프(Feedback loop)를 형성한다고 주장하였다 [3]. 나아가 Massey 등(1993)은 누적인과(Cumulative Causation) 이론을 통해, 선발 이주자들이 형성한 네트워크가 후속 이주자들의 비용과 위험을 낮춤으로써 이동이 지속적으로 확대되는 메커니즘을 강조하였다 [4]. Castles 등(2014)은 현대 이동연구의 종합적 관점에서 이동을 단순한 경제적 합리성의 산물이 아니라, 사회적 네트워크와 구조적 맥락이 복합적으로 작용하는 다층적 과정으로 이해해야 함을 역설하였다 [5]. 최근 de Haas(2010) 역시 이동 과정의 내부 동학(Internal dynamics)을 강조하며, 이주 네트워크 자체가 독립적인 구조적 요인으로 작용하여 초기 이동의 원인이 소멸된 후에도 이동을 지속시키는 동력임을 역설하였다 [6]. 본 연구는 이러한 시스템적 관점과 누적인과 이론을 바탕으로, 지역 간 인구이동 흐름이 단순한 일회성 사건이 아니라 상호 연결된 네트워크 구조 속에서 진화하며 자기강화 메커니즘을 형성하는 과정임을 전제로 한다.

### 2.2. 인구이동의 네트워크 분석

최근 데이터 가용성의 증가와 복잡계 네트워크(Complex Networks) 이론의 발전에 힘입어, 인구이동을 노드(지역)와 엣지(이동량)로 구성된 네트워크로 모델링하는 연구가 활발히 진행되고 있다 [7]. 네트워크 분석은 전체 시스템의 위상적(Topological) 구조를 파악하고, 개별 지역이 네트워크 내에서 차지하는 구조적 중요성(Centrality)을 정량화할 수 있다 [8]. 특히, Brin과 Page(1998)가 고안한 PageRank 알고리즘은 노드의 단순한 연결 수를 넘어, 연결된 이웃 노드들의 중요성까지 가중 반영하여 해당 노드의 실질적인 영향력을 평가하는 데 유용하다 [9]. 

국제적으로 Tranos 등(2015)은 유럽 내 이동 네트워크를 분석하여 전통적 중력모형이 포착하지 못하는 네트워크의 군집성(Clustering)과 집중도를 규명하였다 [10]. 단일 국가 단위의 내부 이동에 관한 연구도 활발한데, Gürsoy와 Badur(2022)는 터키의 2008~2020년 내부 이동 네트워크를 분석하여 경제적 중심지들이 강력한 허브 역할을 수행하며, 네트워크의 거시적 구조가 시간에 따라 높은 안정성을 보임을 확인하였다 [11]. 최근 Xu 등(2025)은 미국 카운티 간 이동 네트워크 분석을 통해 COVID-19 팬데믹 충격에도 불구하고 주요 허브들의 구조적 지위가 안정적으로 유지되는 네트워크 회복탄력성(Resilience)을 실증하였다 [12]. 또한, 이탈리아 주 간 이동을 분석한 Sarra 등(2025)은 고숙련 이주자의 이동이 전통적인 남북 이동 경로를 넘어 새로운 지역 흡인력을 창출하며 네트워크를 다변화시키고 있음을 밝혔다 [13].

쇠퇴도시(Shrinking cities)의 관점에서 네트워크를 분석한 연구들도 주목받고 있다. Chen 등(2025)은 중국의 인구 및 투자 네트워크를 분석하여, 쇠퇴도시들이 이동 네트워크에서 주변부(Peripheral)로 전락하고 있으며, 인접한 지역 허브들이 이들 쇠퇴도시의 인구를 흡수하는 재편 과정을 정량적으로 규명하였다 [14]. 국내의 경우 이상현과 오윤경(2017)이 네트워크 지표를 통해 수도권 집중 현상을 확인한 바 있다 [15]. 그러나 기존 연구들은 대부분 연결중심성(Degree Centrality) 등 기술적(Descriptive) 분석에 머물러 있으며, 이동 허브의 동태적 진화(Dynamic evolution)와 이러한 구조적 지위가 실제 지역의 인구 유입에 미치는 인과적 효과(Causal implications)를 계량경제학적으로 검증한 연구는 여전히 부족하다.

### 2.3. 공간 패널 모형과 인구이동 결정요인

인구이동은 공간적 상호작용의 결과물이므로, 인접 지역 간의 공간적 의존성(Spatial Dependence)을 고려하지 않은 전통적 회귀분석은 추정의 편의(Bias)를 초래할 수 있다 [16]. 공간계량경제학(Spatial Econometrics)의 발전과 함께, LeSage와 Pace(2009)는 공간 더빈 모형(Spatial Durbin Model, SDM)을 통해 지역 간의 파급효과를 직접효과(Direct Effect), 간접효과(Indirect Effect), 총효과(Total Effect)로 분해하는 방법론을 제시하였다 [17]. 

최근 공간 패널 모형을 적용한 연구들은 이동 결정요인의 복잡성을 실증하고 있다. 중국의 내부 이동을 분석한 Pu 등(2021)은 공간 동적 패널 모형을 적용하여 특정 지역의 인구 유입이 인접 지역 유입과 유의미한 상관관계가 있음을 밝혔다 [18]. Sahin 등(2026)은 튀르키예 지역 패널 분석을 통해 이주자의 인적자본 수준에 따라 지역 경제에 미치는 파급효과가 상이함을 SDM과 SARAR 모형으로 입증하였다 [19]. 

한국의 경우 전명진(2014)과 이희연 등(2011)이 인구이동 결정요인을 분석하였고 [20] [21], 이찬영과 이흥후(2016)는 패널 모형을 통해 청년층의 고용 기회와 주거 여건이 핵심 요인임을 확인하였다 [22]. 최근 Jeong 등(2025)은 공간 자기회귀 패널(SAR panel) 모형을 적용하여 연령대별 인구이동 결정요인의 이질성을 분석하였다. 이 연구는 20대 청년층은 경제적 기회에 의해 주로 이동하는 반면, 30~40대는 주거 대체가능성과 경제적 기회의 복합적 상호작용에 크게 영향받음을 실증하였다 [23]. 이처럼 최신 연구들은 연령대별 특성과 공간적 파급효과의 중요성을 강조하고 있으나, 지역 간의 관계적 속성을 나타내는 네트워크 지표를 설명변수로 통합하여 공간 패널 모형으로 검증한 연구는 여전히 부재하다.

### 2.4. 머신러닝과 지역 흡인력(XAI) 예측

전통적인 계량경제 모형은 변수 간의 평균적인 선형 관계를 추정하는 데 유용하지만, 인구이동과 같이 복잡하고 비선형적인 상호작용이 존재하는 현상을 예측하는 데에는 한계를 지닌다. 최근 머신러닝(Machine Learning) 기법의 발전은 이러한 한계를 극복하고 예측의 정확도를 획기적으로 향상시켰다. Random Forest, XGBoost, LightGBM 등의 트리 기반 앙상블(Tree-based Ensemble) 모델은 변수 간의 복잡한 교호작용(Interaction)과 비선형성을 자동으로 포착할 수 있어 도시 성장 및 쇠퇴 예측에 널리 활용되고 있다 [24] [25].

그러나 머신러닝 모델이 일반적으로 우수한 예측 성능을 보임에도 불구하고, 모델의 복잡성으로 인한 해석 가능성의 한계(Black-box problem)는 정책적 활용에 큰 장애물이 되어왔다. 이를 극복하기 위해 최근 설명 가능한 인공지능(Explainable AI, XAI), 특히 SHAP(SHapley Additive exPlanations) 기법이 필수적인 분석 도구로 부상하고 있다 [26]. Shangguan(2025)은 XGBoost와 SHAP을 결합하여 중국 인구 도시화의 사회경제적 결정요인을 분석하였으며, 특정 변수가 일정 수준을 넘어서면 효과가 급변하는 임계효과(Threshold effect)를 밝혀내어 선형모형이 포착하지 못하는 비선형적 정책 시사점을 도출하였다 [27].

그럼에도 불구하고, 한국의 시군구 단위 장기 패널 데이터에 머신러닝과 SHAP 분석을 적용하여 지역 흡인력의 결정요인을 규명한 연구는 아직 초기 단계에 머물러 있다. 특히 패널 데이터의 특성상 발생할 수 있는 시계열적 정보 누수(Data Leakage)를 완벽히 통제한 상태에서 모델을 검증하고, 전통적인 사회경제적 변수와 함께 인구이동 네트워크의 구조적 지표를 통합하여 지역 흡인력을 모델링한 연구는 찾아보기 어렵다. 나아가 이러한 비선형적 결정구조가 시간에 따라, 특히 COVID-19 팬데믹과 같은 외생적 충격 전후로 어떻게 변화하는지(시간적 항상성)를 규명한 연구 역시 부재하다.

### 2.5. 선행연구의 한계와 본 연구의 차별성

위에서 검토한 선행연구들을 종합하면, 인구이동과 지역쇠퇴에 관한 학술적 논의는 점차 네트워크 분석, 공간 패널 모형, 머신러닝 등 고도화된 방법론으로 진화하고 있다. 그러나 기존 연구들은 이들 방법론을 개별적으로 적용하는 데 그쳤으며, 특히 한국의 장기 패널 데이터를 대상으로 이를 통합한 연구는 부재하다. 기존 연구의 주요 한계와 본 연구의 차별성을 요약하면 다음 표와 같다.

| 연구 공백 (Research Gaps) | 기존 연구의 한계 | 본 연구의 기여 및 차별성 |
| :--- | :--- | :--- |
| **1. 장기 패널 기반 네트워크 동학 부재** | 특정 연도나 단기 시계열 분석에 국한, 허브의 동태적 진화 추적 한계 | 20년(2006~2025) 장기 패널을 구축하여 네트워크 허브의 진화와 안정성(Resilience) 분석 |
| **2. 네트워크 지표의 인과효과 검증 미흡** | 중심성 등 기술적(Descriptive) 분석에 치중, 순이동에 미치는 인과성 검증 부족 | PageRank 등 구조적 지위를 독립변수화하여 공간 더빈 모형(SDM)으로 직접·간접효과 검증 |
| **3. 연령별/생애주기별 네트워크 구조 차이** | 총인구 중심의 거시적 분석에 치중, 청년층 등 특정 연령대 네트워크 특성 간과 | 연령대별(20대, 30~40대 등) 이동 네트워크를 분리 구축하여 구조적 이질성 비교 분석 |
| **4. 비선형 예측 및 정책 해석 가능성 부재** | 선형모형 중심, 머신러닝의 블랙박스 한계로 정책적 시사점 도출의 제약 | 정보 누수를 통제한 CatBoost와 SHAP을 결합하여 지역 흡인력의 비선형적 결정요인을 투명하게 규명 |
| **5. 결정구조의 시간적 항상성 검증 부족** | 특정 시점의 단면적 결정요인 분석에 머무름, 충격(팬데믹 등)에 따른 변화 추적 한계 | 기간분할 및 연도별 계수 추적을 통해 결정구조의 장기적 항상성과 팬데믹 충격 효과 검증 |

결론적으로, 본 연구는 대한민국 시군구 인구이동이라는 극단적 집적과 지역쇠퇴 현상을 대상으로, **네트워크 분석(구조 파악) → 공간 패널 모형(인과 검증) → 머신러닝/XAI(비선형 예측 및 해석)**로 이어지는 다층적·통합적 방법론을 적용함으로써, 기존 연구의 공백을 메우고 지방소멸 대응을 위한 정교한 정책적 함의를 도출하고자 한다.

---

## References

[1] Ravenstein, E. G. (1885). The laws of migration. *Journal of the Statistical Society of London*, 48(2), 167-227. https://doi.org/10.2307/2979181
[2] Lee, E. S. (1966). A theory of migration. *Demography*, 3(1), 47-57. https://doi.org/10.2307/2060063
[3] Mabogunje, A. L. (1970). Systems approach to a theory of rural‐urban migration. *Geographical Analysis*, 2(1), 1-18. https://doi.org/10.1111/j.1538-4632.1970.tb00140.x
[4] Massey, D. S., Arango, J., Hugo, G., Kouaouci, A., Pellegrino, A., & Taylor, J. E. (1993). Theories of international migration: A review and appraisal. *Population and Development Review*, 19(3), 431-466. https://doi.org/10.2307/2938462
[5] Castles, S., de Haas, H., & Miller, M. J. (2014). *The Age of Migration: International Population Movements in the Modern World* (5th ed.). Guilford Press.
[6] de Haas, H. (2010). Migration and development: A theoretical perspective. *International Migration Review*, 36(1), 227-264. https://doi.org/10.1111/j.1747-7379.2010.00804.x
[7] Danchev, V., & Porter, M. A. (2020). Migration networks: Applications of network analysis to macroscale migration patterns. *Journal of Complex Networks*, 8(1), cnaa018. https://doi.org/10.1093/comnet/cnaa018
[8] Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509-512. https://doi.org/10.1126/science.286.5439.509
[9] Brin, S., & Page, L. (1998). The anatomy of a large-scale hypertextual web search engine. *Computer Networks and ISDN Systems*, 30(1-7), 107-117. https://doi.org/10.1016/S0169-7552(98)00110-X
[10] Tranos, E., Gheasi, M., & Nijkamp, P. (2015). International migration: A global complex network analysis. *Regional Studies*, 49(1), 4-22. https://doi.org/10.1080/00343404.2014.964666
[11] Gürsoy, S., & Badur, D. (2022). Network analysis of internal migration in Turkey. *Physica A: Statistical Mechanics and its Applications*, 596, 127138. https://doi.org/10.1016/j.physa.2022.127138
[12] Xu, A., Hu, Y., & Wang, F. (2025). Unraveling the COVID-19 impact on spatiotemporal dynamics of US domestic migration: a network perspective. *The Professional Geographer*. https://doi.org/10.1080/00330124.2025.2455188
[13] Sarra, A., Di Caro, P., & Nissi, E. (2025). A network analysis of skill-specific internal migration flows in Italy. *Socio-Economic Planning Sciences*, 102000. https://doi.org/10.1016/j.seps.2025.102000
[14] Chen, Y., Tao, R., Ma, Q., & Wang, M. (2025). Shrinking cities in China's urban network: a data-driven exploration of migration and investment flows. *Applied Geography*, 176, 103596. https://doi.org/10.1016/j.apgeog.2025.103596
[15] 이상현, 오윤경. (2017). 시계열 인구이동 자료를 활용한 네트워크 연결중심성 분석. *국토계획*, 52(4), 115-131.
[16] Anselin, L. (1988). *Spatial Econometrics: Methods and Models*. Kluwer Academic Publishers.
[17] LeSage, J., & Pace, R. K. (2009). *Introduction to Spatial Econometrics*. CRC Press. https://doi.org/10.1201/9781420064254
[18] Pu, Y., Zhao, X., & Chi, G. (2021). Spatial dynamic panel model of internal migration in China. *Population, Space and Place*, 27(6), e2429. https://doi.org/10.1002/psp.2429
[19] Sahin, S., et al. (2026). Analysing the impact of migration flows on regional per capita GDP in Türkiye: a spatial panel data approach. *Post-Soviet Economics*.
[20] 전명진. (2014). 수도권 인구이동의 결정요인에 관한 연구: 공간계량경제모형의 적용. *국토계획*, 49(5), 97-111.
[21] 이희연, 황명화. (2011). 전국 시군구의 인구이동 패턴과 공간적 상호작용. *한국경제지리학회지*, 23(4), 605-625.
[22] 이찬영, 이흥후. (2016). 청년층의 지역 간 인구이동 결정요인 분석. *지역연구*, 32(3), 3-21.
[23] Jeong, S., et al. (2025). Analyzing the Influences of Economic Opportunity and Residential Substitutability on Population Migration by Age Group. *Journal of the Korea Planning Association*, 60(1), 46343.
[24] Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324
[25] Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785-794). https://doi.org/10.1145/2939672.2939785
[26] Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In *Advances in Neural Information Processing Systems* (Vol. 30).
[27] Shangguan, Z. (2025). An Explainable Machine-Learning Framework Based on XGBoost-SHAP and Big Data for Revealing the Socioeconomic Drivers of Population Urbanization in China. *Systems*, 13(8), 679. https://doi.org/10.3390/systems13080679
