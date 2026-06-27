#!/usr/bin/env python3
"""
Phase 4: 통합 단일 참고문헌 목록 구축
- §2, §3의 분리된 References 제거
- 단일 알파벳/가나다순 정렬된 목록 생성 (국문 먼저, 영문 나중)
- "et al." 전 저자 표기 변환
- §5 결론 파일 끝에 단일 References 추가
"""

import re

# 전 저자 데이터
full_authors = {
    "Pitoski": "Pitoski, D., Thomas, M. L., & Rozenblat, C. (2021). Migration networks: A PageRank-based approach to internal migration. *Computational Social Networks*, 8(1), 10. https://doi.org/10.1186/s40649-021-00088-2",
    "Almquist": "Almquist, Z. W., Brelsford, C., & Jones, J. H. (2024). Uncovering migration systems through spatio-temporal tensor co-clustering. *Scientific Reports*, 14, 26861. https://doi.org/10.1038/s41598-024-78018-8",
    "Sahin": "Sahin, S., Karaman, M. M., & Ozden, C. (2026). Analysing the impact of migration flows on regional per capita GDP in Türkiye: a spatial panel data approach. *Public Sector Economics*, 50(2), 259-286. https://doi.org/10.3326/pse.50.2.4",
    "Lee": "Lee, J., Kim, H., & Park, S. (2025). Disaggregating Multifaceted Destination Effects on Residential Migration. *Land*, 14(9), 1833. https://doi.org/10.3390/land14091833"
}

# 마스터 리스트 (중복 제거 및 정렬)
master_refs = [
    # 영문
    "Abel, G. J., & Sander, N. (2014). Quantifying global international migration flows. *Science*, 343(6178), 1520-1522. https://doi.org/10.1126/science.1248676",
    "Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A next-generation hyperparameter optimization framework. In *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining* (pp. 2623-2631). https://doi.org/10.1145/3292500.3330701",
    full_authors["Almquist"],
    "Anselin, L. (1988). *Spatial Econometrics: Methods and Models*. Kluwer Academic Publishers.",
    "Anselin, L. (1995). Local indicators of spatial association—LISA. *Geographical Analysis*, 27(2), 93-115. https://doi.org/10.1111/j.1538-4632.1995.tb00338.x",
    "Arellano, M., & Bond, S. (1991). Some tests of specification for panel data: Monte Carlo evidence and an application to employment equations. *The Review of Economic Studies*, 58(2), 277-297. https://doi.org/10.2307/2297968",
    "Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509-512. https://doi.org/10.1126/science.286.5439.509",
    "Blondel, V. D., Guillaume, J. L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. *Journal of Statistical Mechanics: Theory and Experiment*, 2008(10), P10008. https://doi.org/10.1088/1742-5468/2008/10/P10008",
    "Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324",
    "Castles, S., de Haas, H., & Miller, M. J. (2014). *The Age of Migration: International Population Movements in the Modern World* (5th ed.). Guilford Press.",
    "Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785-794). https://doi.org/10.1145/2939672.2939785",
    "Chen, Y., Tao, R., Ma, Q., & Wang, M. (2025). Shrinking cities in China's urban network: a data-driven exploration of migration and investment flows. *Applied Geography*, 180, 103596. https://doi.org/10.1016/j.apgeog.2025.103596",
    "Danchev, V., & Porter, M. A. (2020). Migration networks: Applications of network analysis to macroscale migration patterns. *Journal of Complex Networks*, 8(1), cnaa018. https://doi.org/10.1093/comnet/cnaa018",
    "de Haas, H. (2010). Migration and development: A theoretical perspective. *International Migration Review*, 36(1), 227-264. https://doi.org/10.1111/j.1747-7379.2010.00804.x",
    "Elhorst, J. P. (2014). *Spatial Econometrics: From Cross-Sectional Data to Spatial Panels*. Springer. https://doi.org/10.1007/978-3-642-40340-8",
    "Freeman, L. C. (1978). Centrality in social networks conceptual clarification. *Social Networks*, 1(3), 215-239. https://doi.org/10.1016/0378-8733(78)90021-7",
    "Gürsoy, S., & Badur, D. (2022). Network analysis of internal migration in Turkey. *Physica A: Statistical Mechanics and its Applications*, 596, 127138. https://doi.org/10.1016/j.physa.2022.127138",
    "Haase, A., Haase, A., & Rink, D. (2021). Conceptualizing place attractiveness for migration. *Population, Space and Place*, 27(6), e2427. https://doi.org/10.1002/psp.2427",
    "Im, K. S., Pesaran, M. H., & Shin, Y. (2003). Testing for unit roots in heterogeneous panels. *Journal of Econometrics*, 115(1), 53-74. https://doi.org/10.1016/S0304-4076(03)00092-7",
    "Jeong, S., Kim, Y., & Yoon, J. (2025). Analyzing the Influences of Economic Opportunity and Residential Substitutability on Population Migration by Age Group. *Journal of Korea Planning Association*, 60(4), 38-59.",
    "Lee, E. S. (1966). A theory of migration. *Demography*, 3(1), 47-57. https://doi.org/10.2307/2060063",
    full_authors["Lee"],
    "Lee, L. F., & Yu, J. (2010). Estimation of spatial autoregressive panel data models with fixed effects. *Journal of Econometrics*, 154(2), 165-185. https://doi.org/10.1016/j.jeconom.2009.08.001",
    "LeSage, J., & Pace, R. K. (2009). *Introduction to Spatial Econometrics*. CRC Press. https://doi.org/10.1201/9781420064254",
    "Levin, A., Lin, C. F., & Chu, C. S. J. (2002). Unit root tests in panel data: asymptotic and finite-sample properties. *Journal of Econometrics*, 108(1), 1-24. https://doi.org/10.1016/S0304-4076(01)00098-7",
    "Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In *Advances in Neural Information Processing Systems* (Vol. 30).",
    "Mabogunje, A. L. (1970). Systems approach to a theory of rural‐urban migration. *Geographical Analysis*, 2(1), 1-18. https://doi.org/10.1111/j.1538-4632.1970.tb00140.x",
    "Massey, D. S., Arango, J., Hugo, G., Kouaouci, A., Pellegrino, A., & Taylor, J. E. (1993). Theories of international migration: A review and appraisal. *Population and Development Review*, 19(3), 431-466. https://doi.org/10.2307/2938462",
    "Niedomysl, T. (2010). Towards a conceptual framework of place attractiveness: A migration perspective. *Geografiska Annaler: Series B, Human Geography*, 92(1), 97-109. https://doi.org/10.1111/j.1468-0467.2010.00335.x",
    "Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). *The PageRank citation ranking: Bringing order to the web*. Stanford InfoLab.",
    full_authors["Pitoski"],
    "Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: unbiased boosting with categorical features. In *Advances in Neural Information Processing Systems* (Vol. 31).",
    "Pu, Y., Zhao, X., & Chi, G. (2019). Spatial dynamic panel model of internal migration in China. *Demographic Research*, 41(31), 873-904. https://doi.org/10.4054/DemRes.2019.41.31",
    "Ravenstein, E. G. (1885). The laws of migration. *Journal of the Statistical Society of London*, 48(2), 167-227. https://doi.org/10.2307/2979181",
    "Roberts, M. E., Stewart, B. M., & Tingley, D. (2017). stm: An R package for structural topic models. *Journal of Statistical Software*, 10(2), 1-40.",
    full_authors["Sahin"],
    "Sarra, A., D'Ingiullo, D., Evangelista, A., Nissi, E., Quaglione, D., & Di Battista, T. (2025). A network analysis of skill-specific internal migration flows in Italy. *Socio-Economic Planning Sciences*, 100, 102225. https://doi.org/10.1016/j.seps.2025.102225",
    "Shangguan, Z. (2025). An Explainable Machine-Learning Framework Based on XGBoost-SHAP and Big Data for Revealing the Socioeconomic Drivers of Population Urbanization in China. *Systems*, 13(8), 679. https://doi.org/10.3390/systems13080679",
    "Tranos, E., Gheasi, M., & Nijkamp, P. (2015). International migration: A global complex network analysis. *Regional Studies*, 49(1), 4-22. https://doi.org/10.1080/00343404.2014.964666",
    "Wu, J., & Liu, Y. (2022). Stability and change in China's geography of intercity migration. *Population, Space and Place*, 28(6), e2570. https://doi.org/10.1002/psp.2570",
    "Xu, X., Hu, Y., & Wang, F. (2025). Unraveling the COVID-19 impact on spatiotemporal dynamics of U.S. domestic migration: A network perspective. *The Professional Geographer*, 77(2), 104-120. https://doi.org/10.1080/00330124.2025.2455188",
    
    # 국문
    "이상현, 오윤경. (2017). 시계열 인구이동 자료를 활용한 네트워크 연결중심성 분석. *국토계획*, 52(4), 115-131.",
    "이찬영, 이흥후. (2016). 청년층의 지역 간 인구이동 결정요인 분석. *지역연구*, 32(3), 3-21.",
    "이희연, 황명화. (2011). 전국 시군구의 인구이동 패턴과 공간적 상호작용. *한국경제지리학회지*, 23(4), 605-625.",
    "전명진. (2014). 수도권 인구이동의 결정요인에 관한 연구: 공간계량경제모형의 적용. *국토계획*, 49(5), 97-111."
]

# 국문 먼저, 영문 나중으로 정렬
korean_refs = sorted([r for r in master_refs if re.search(r'[가-힣]', r[:10])])
english_refs = sorted([r for r in master_refs if not re.search(r'[가-힣]', r[:10])])
final_refs = korean_refs + english_refs

# 포맷팅: 번호 없이 hanging indent 효과를 위해 markdown 리스트(-) 또는 HTML 사용
# 지시서: "목록에서 번호 제거, 행 들여쓰기(hanging indent) APA 형식"
# Markdown에서는 `<div style="padding-left: 2em; text-indent: -2em;">` 사용이 확실함
formatted_refs = "## References\n\n<div style=\"padding-left: 2em; text-indent: -2em;\">\n\n"
for ref in final_refs:
    formatted_refs += f"{ref}\n\n"
formatted_refs += "</div>\n"

# 1. §2, §3 파일에서 기존 References 삭제
files_to_strip = [
    "/home/ubuntu/korea-migration-network/docs/02_문헌연구_Literature_Review.md",
    "/home/ubuntu/korea-migration-network/docs/03_방법론_Methodology.md"
]

for path in files_to_strip:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    ref_start = text.find("## References")
    if ref_start != -1:
        text = text[:ref_start].strip() + "\n"
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

# 2. §5 결론 파일 끝에 마스터 리스트 추가
conclusion_path = "/home/ubuntu/korea-migration-network/docs/05_결론_Conclusion.md"
with open(conclusion_path, "r", encoding="utf-8") as f:
    text = f.read()

# 기존 References가 있다면 제거
ref_start = text.find("## References")
if ref_start != -1:
    text = text[:ref_start].strip() + "\n\n"
else:
    text = text.strip() + "\n\n"

text += formatted_refs

with open(conclusion_path, "w", encoding="utf-8") as f:
    f.write(text)

print("통합 단일 참고문헌 목록 구축 완료")
