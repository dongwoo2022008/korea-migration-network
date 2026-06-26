# Shapefile & Code Mapping

## Files

| File | Size | Description |
|------|------|-------------|
| `korea_sgg_lawcode.geojson` | 632 KB | GeoJSON boundary file for 229 Si-Gun-Gu (SGG) units in South Korea (law-code based) |
| `sgg_code_mapping_229.csv` | 9 KB | Code mapping table: SGG code ↔ name ↔ province ↔ region |

## Variables in `sgg_code_mapping_229.csv`

| Column | Description |
|--------|-------------|
| `sgg_code` | 5-digit SGG administrative code |
| `sgg_name` | Korean name of the SGG unit |
| `sido_name` | Province (시도) name |
| `region` | Macro-region label (수도권, 영남권, 호남권, 충청권, 강원·제주) |

## Notes

- Coordinate system: EPSG:4326 (WGS84)
- N = 229 SGG units (as of 2024 administrative boundaries)
- Source: Statistics Korea (KOSIS) administrative boundary data
