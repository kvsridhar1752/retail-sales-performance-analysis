# Generated Analysis Results

The analysis was run on 8,000 synthetic retail sales transactions.

## Revenue by product category

| Product category | Revenue (EUR) | Orders | Units sold |
|---|---:|---:|---:|
| Electronics | 923,205.01 | 2,005 | 3,507 |
| Home & Kitchen | 350,495.53 | 1,601 | 2,712 |
| Sports | 221,262.27 | 1,207 | 2,081 |
| Clothing | 220,146.68 | 1,999 | 3,438 |
| Beauty | 89,862.24 | 1,188 | 2,078 |

## Revenue by region

| Region | Revenue (EUR) | Orders | Average order value (EUR) |
|---|---:|---:|---:|
| Munich | 375,520.11 | 1,652 | 227.31 |
| Cologne | 363,574.24 | 1,595 | 227.95 |
| Hamburg | 363,079.89 | 1,576 | 230.38 |
| Frankfurt | 353,690.41 | 1,621 | 218.19 |
| Berlin | 349,107.08 | 1,556 | 224.36 |

## Key insight

Electronics generates the largest share of revenue, while Beauty has the lowest revenue despite a meaningful number of orders. Munich is the highest-revenue region, and the analysis recommends prioritizing Electronics inventory, promoting higher-margin products, and reviewing Beauty category pricing and assortment.

The dashboard image is generated locally by running:

```bash
python data/generate_data.py
python analysis/sales_analysis.py
```
