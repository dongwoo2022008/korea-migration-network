# Spatial Weights Matrix

## Files

| File | Size | Description |
|------|------|-------------|
| `queen_w_229_fixed.npz` | 3.3 KB | Queen contiguity spatial weights matrix (229×229, scipy sparse format) |
| `queen_w_229_fixed_index.csv` | 4.9 KB | Row/column index mapping for the weights matrix |
| `queen_w_229_neighbors.csv` | 11 KB | Neighbor list in long format (origin–destination pairs) |

## Usage

```python
import numpy as np
from scipy.sparse import load_npz

W = load_npz('queen_w_229_fixed.npz')   # 229×229 sparse matrix
idx = pd.read_csv('queen_w_229_fixed_index.csv')
```

## Notes

- Type: Queen contiguity (shared edge or vertex = neighbor)
- Row-standardized: Yes
- N = 229 SGG units
- Used in: Moran's I, LM tests, SDM estimation (§3.5.3, Table 3-6)
