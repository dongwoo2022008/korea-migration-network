# Age-specific Network Data

## Files

| File | Size | Description |
|------|------|-------------|
| `age_top_hubs_allyears.xlsx` | 23 KB | Top hub regions by age group and year (pre-computed from OD matrix) |

## Schema: `age_top_hubs_allyears.xlsx`

| Column | Description |
|--------|-------------|
| `year` | Year |
| `age_group` | Age group (youth: 20–34, middle: 35–54, elderly: 55+) |
| `sgg_code` | SGG code |
| `sgg_name` | SGG name |
| `pagerank` | PageRank centrality score |
| `in_degree` | In-degree centrality |
| `rank` | Rank within age group × year |

## Notes

- Used for RQ4: Age-specific migration network comparison (§4.5)
- Full age-group OD matrices available in `../od_matrix/migration_long.parquet`
