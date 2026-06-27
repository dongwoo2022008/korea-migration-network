#!/usr/bin/env python3
"""
E: §2 참고문헌 [19-x] 비표준 번호 전면 재정렬
현재 본문 인용 순서대로 단일 연속번호([1]~[N]) 재부여
삭제된 LLC[19-1], IPS[19-2], Optuna[29]는 이미 제거됨

현재 본문 인용 순서 분석:
[1] Ravenstein 1885
[2] Lee 1966
[3] Mabogunje 1970
[4] Massey 1993
[5] Castles 2014
[6] de Haas 2010
[7] Danchev & Porter 2020
[8] Barabási & Albert 1999
[9] Brin & Page 1998
[10] Tranos 2015
[11] Gürsoy & Badur 2022
[19-3] Wu & Liu 2022  → 새 번호 [12]
[12] Xu 2025          → 새 번호 [13]
[13] Sarra 2025       → 새 번호 [14]
[19-6] Abel & Sander 2014 → 새 번호 [15]  (A-1 삽입으로 이 순서)
[19-4] Pitoski 2021   → 새 번호 [16]
[19-5] Almquist 2024  → 새 번호 [17]
[14] Chen 2025        → 새 번호 [18]
[15] 이상현·오윤경 2017 → 새 번호 [19]
[16] Anselin 1988     → 새 번호 [20]
[17] LeSage & Pace 2009 → 새 번호 [21]
[18] Pu 2019          → 새 번호 [22]
[19] Sahin 2026       → 새 번호 [23]
[20] 전명진 2014      → 새 번호 [24]
[21] 이희연 2011      → 새 번호 [25]
[22] 이찬영 2016      → 새 번호 [26]
[23] Jeong 2025       → 새 번호 [27]
[19-7] Lee 2025       → 새 번호 [28]
[24] Breiman 2001     → 새 번호 [29]
[25] Chen & Guestrin 2016 → 새 번호 [30]
[26] Lundberg & Lee 2017 → 새 번호 [31]
[27] Shangguan 2025   → 새 번호 [32]
[30] Niedomysl 2010   → 새 번호 [33]
[31] Haase 2021       → 새 번호 [34]
[28] Prokhorenkova (CatBoost) 2018 → 새 번호 [35]
"""

import re

path = "/home/ubuntu/korea-migration-network/docs/02_문헌연구_Literature_Review.md"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 구번호 → 신번호 매핑 (긴 번호부터 처리해야 [19-3]이 [19]로 잘못 치환되지 않음)
# 순서: 반드시 [19-x] 형식을 먼저, 그 다음 일반 번호
mapping = [
    # 비표준 번호 먼저
    ("[19-3]", "[12]"),
    ("[19-6]", "[15]"),
    ("[19-4]", "[16]"),
    ("[19-5]", "[17]"),
    ("[19-7]", "[28]"),
    # 기존 번호 중 충돌 가능성 있는 것 (큰 번호 먼저)
    ("[31]", "[34]"),
    ("[30]", "[33]"),
    ("[29]", "[DELETED]"),   # 이미 삭제됐으나 혹시 남아있을 경우 처리
    ("[28]", "[35]"),
    ("[27]", "[32]"),
    ("[26]", "[31]"),
    ("[25]", "[30]"),
    ("[24]", "[29]"),
    ("[23]", "[27]"),
    ("[22]", "[26]"),
    ("[21]", "[25]"),
    ("[20]", "[24]"),
    ("[19]", "[23]"),
    ("[18]", "[22]"),
    ("[17]", "[21]"),
    ("[16]", "[20]"),
    ("[15]", "[19]"),
    ("[14]", "[18]"),
    ("[13]", "[14]"),
    ("[12]", "[13]"),   # 이미 [12]로 바뀐 Wu&Liu → [12] 유지 (아래 재정렬에서 처리)
    # [1]~[11]은 변경 없음
]

# 단계적 치환 (충돌 방지를 위해 임시 마커 사용)
# Step 1: 모든 구번호를 임시 마커로 변환
temp_mapping = {}
for old, new in mapping:
    temp = f"__TEMP_{old[1:-1].replace('-','_')}__"
    temp_mapping[temp] = new
    text = text.replace(old, temp)

# Step 2: 임시 마커를 신번호로 변환
for temp, new in temp_mapping.items():
    if new != "[DELETED]":
        text = text.replace(temp, new)
    else:
        text = text.replace(temp, "")

# Wu&Liu [19-3]은 이미 [12]로 변환됐으나 Xu [12]도 [13]으로 변환됨
# → Wu&Liu의 임시마커 __TEMP_19_3__ → [12], Xu의 __TEMP_12__ → [13]
# 순서 확인: Wu&Liu 먼저 [12]로, 그 다음 원래 [12](Xu)가 [13]으로
# 이 순서는 위 mapping에서 [19-3]→[12] 먼저, [12]→[13] 나중에 처리하므로 충돌 없음

# References 섹션도 재정렬
# 현재 References 순서를 새 번호 순서로 재작성
old_refs = """## References

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
[11] Gürsoy, S., & Badur, D. (2022). Network analysis of internal migration in Turkey. *Physica A: Statistical Mechanics and its Applications*, 596, 127138. https://doi.org/10.1016/j.physa.2022.127138"""

# References 섹션을 완전히 새로 작성
new_refs = """## References

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
[12] Wu, J., & Liu, Y. (2022). Stability and change in China's geography of intercity migration. *Population, Space and Place*, 28(6), e2570. https://doi.org/10.1002/psp.2570
[13] Xu, X., Hu, Y., & Wang, F. (2025). Unraveling the COVID-19 impact on spatiotemporal dynamics of U.S. domestic migration: A network perspective. *The Professional Geographer*, 77(2), 104-120. https://doi.org/10.1080/00330124.2025.2455188
[14] Sarra, A., D'Ingiullo, D., Evangelista, A., Nissi, E., Quaglione, D., & Di Battista, T. (2025). A network analysis of skill-specific internal migration flows in Italy. *Socio-Economic Planning Sciences*, 100, 102225. https://doi.org/10.1016/j.seps.2025.102225
[15] Abel, G. J., & Sander, N. (2014). Quantifying global international migration flows. *Science*, 343(6178), 1520-1522. https://doi.org/10.1126/science.1248676
[16] Pitoski, D., et al. (2021). Migration networks: A PageRank-based approach to internal migration. *Computational Social Networks*, 8(1), 10.
[17] Almquist, Z. W., et al. (2024). Uncovering migration systems through spatio-temporal tensor co-clustering. *Scientific Reports*, 14, 26861.
[18] Chen, Y., Tao, R., Ma, Q., & Wang, M. (2025). Shrinking cities in China's urban network: a data-driven exploration of migration and investment flows. *Applied Geography*, 180, 103596. https://doi.org/10.1016/j.apgeog.2025.103596
[19] 이상현, 오윤경. (2017). 시계열 인구이동 자료를 활용한 네트워크 연결중심성 분석. *국토계획*, 52(4), 115-131.
[20] Anselin, L. (1988). *Spatial Econometrics: Methods and Models*. Kluwer Academic Publishers.
[21] LeSage, J., & Pace, R. K. (2009). *Introduction to Spatial Econometrics*. CRC Press. https://doi.org/10.1201/9781420064254
[22] Pu, Y., Zhao, X., & Chi, G. (2019). Spatial dynamic panel model of internal migration in China. *Demographic Research*, 41(31), 873-904. https://doi.org/10.4054/DemRes.2019.41.31
[23] Sahin, S., et al. (2026). Analysing the impact of migration flows on regional per capita GDP in Türkiye: a spatial panel data approach. *Public Sector Economics*, 50(2), 259-286. https://doi.org/10.3326/pse.50.2.4
[24] 전명진. (2014). 수도권 인구이동의 결정요인에 관한 연구: 공간계량경제모형의 적용. *국토계획*, 49(5), 97-111.
[25] 이희연, 황명화. (2011). 전국 시군구의 인구이동 패턴과 공간적 상호작용. *한국경제지리학회지*, 23(4), 605-625.
[26] 이찬영, 이흥후. (2016). 청년층의 지역 간 인구이동 결정요인 분석. *지역연구*, 32(3), 3-21.
[27] Jeong, S., Kim, Y., & Yoon, J. (2025). Analyzing the Influences of Economic Opportunity and Residential Substitutability on Population Migration by Age Group. *Journal of Korea Planning Association*, 60(4), 38-59.
[28] Lee, J., et al. (2025). Disaggregating Multifaceted Destination Effects on Residential Migration. *Land*, 14(9), 1833.
[29] Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324
[30] Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785-794). https://doi.org/10.1145/2939672.2939785
[31] Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In *Advances in Neural Information Processing Systems* (Vol. 30).
[32] Shangguan, Z. (2025). An Explainable Machine-Learning Framework Based on XGBoost-SHAP and Big Data for Revealing the Socioeconomic Drivers of Population Urbanization in China. *Systems*, 13(8), 679. https://doi.org/10.3390/systems13080679
[33] Niedomysl, T. (2010). Towards a conceptual framework of place attractiveness: A migration perspective. *Geografiska Annaler: Series B, Human Geography*, 92(1), 97-109.
[34] Haase, A., Haase, A., & Rink, D. (2021). Conceptualizing place attractiveness for migration. *Population, Space and Place*, 27(6), e2427.
[35] Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: unbiased boosting with categorical features. In *Advances in Neural Information Processing Systems* (Vol. 31)."""

# References 섹션 전체 교체
# 현재 References 섹션 시작부터 끝까지 찾아서 교체
ref_start = text.find("## References")
if ref_start != -1:
    text = text[:ref_start] + new_refs + "\n"
else:
    text += "\n" + new_refs + "\n"

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("E: 번호 재정렬 완료")

# 검증: 비표준 번호 잔존 여부 확인
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

import re
nonstandard = re.findall(r'\[19-\d\]', content)
temp_markers = re.findall(r'__TEMP_\w+__', content)
print(f"\n비표준 번호 잔존: {nonstandard if nonstandard else '없음 ✅'}")
print(f"임시 마커 잔존: {temp_markers if temp_markers else '없음 ✅'}")

# 본문 인용 번호 목록 확인
all_cites = sorted(set(re.findall(r'\[(\d+)\]', content)))
print(f"\n본문 인용 번호 범위: [{all_cites[0]}] ~ [{all_cites[-1]}]")
print(f"총 고유 번호 수: {len(all_cites)}")

# References 항목 수 확인
ref_entries = re.findall(r'^\[(\d+)\]', content, re.MULTILINE)
print(f"References 항목 수: {len(ref_entries)} ([{ref_entries[0]}]~[{ref_entries[-1]}])")
