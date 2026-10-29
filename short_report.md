# Sales Data Analysis – Task 2 Report

## Project objective
Clean a sales dataset and summarize sales performance by product and region using Python, pandas, and matplotlib.

## Dataset note
The repository's CSV contains 12 illustrative sample sales records. It is not represented as an official dataset supplied by CodeOrbit Tech. Replace it with the official dataset if the internship instructions provided one.

## Methodology
1. Load the CSV with pandas.
2. Check for duplicate rows and convert dates and numeric fields.
3. Remove invalid rows and records with non-positive quantities or negative unit prices.
4. Recalculate revenue as Quantity × Unit_Price.
5. Summarize orders, units, revenue per product, and revenue per region.
6. Export the cleaned dataset and create a product-revenue chart.

## Results from the current sample dataset
- Rows before cleaning: 12
- Rows after cleaning: 12
- Exact duplicate rows removed: 0
- Unique orders: 12
- Units sold: 34
- Total revenue: Rs. 309,300.00
- Average revenue per order: Rs. 25,775.00

### Revenue by product
| Product | Revenue (Rs.) |
|---|---:|
| Laptop | 220,000 |
| Monitor | 60,000 |
| Headphones | 14,000 |
| Mouse | 7,800 |
| Keyboard | 7,500 |

### Revenue by region
| Region | Revenue (Rs.) |
|---|---:|
| North | 130,000 |
| East | 65,500 |
| South | 61,000 |
| West | 52,800 |

## Files
- `sales_dataset.csv` — original illustrative sample dataset.
- `sales_analysis.py` — analysis and cleaning script.
- `sales_analysis_output.csv` — cleaned output generated from the current sample data.
- `revenue_by_product.svg` — chart of revenue by product.
- `requirements.txt` — required Python libraries.
- `short_report.md` — this report.

## How to reproduce
Install dependencies with `pip install -r requirements.txt`, then run `python sales_analysis.py`. The script generates `sales_analysis_output.csv` and `revenue_by_product.png` in the project folder.

## Conclusion
This sample run demonstrates basic data validation, cleaning, aggregation, and visualization. Before final internship submission, confirm whether CodeOrbit required a specific dataset and replace the sample dataset if needed. Re-run the script and update these findings if the data changes.
