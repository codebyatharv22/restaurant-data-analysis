# Restaurant Data Analysis Project

## Project overview
Analyze restaurant data to identify patterns in cuisine popularity, locations, ratings, pricing, online delivery, table booking, restaurant chains, and votes.

**Project type:** Data Analysis / Exploratory Data Analysis (EDA)  
**Tools:** Python, Pandas, NumPy, Matplotlib  
**Dataset size:** 9,551 restaurant records and 21 columns

## Business objectives
- Identify the most common cuisines.
- Find cities with the most restaurants and compare average ratings by city.
- Understand restaurant price-range distribution.
- Compare ratings for restaurants with and without online delivery.
- Examine rating distributions and voting patterns.
- Compare cuisine combinations and restaurant chains.
- Explore geographic distribution using latitude and longitude.
- Check how price range relates to delivery and table-booking availability.

## Main findings
- North Indian, Chinese, and Fast Food are the three most common cuisines when multi-cuisine entries are split.
- New Delhi has the largest restaurant count: 5,473.
- Price Range 1 contains 46.53% of restaurants.
- 25.66% of restaurants offer online delivery.
- Average rating is 3.249 for restaurants offering online delivery and 2.465 for those without it.
- The most common rating band is 3.00–3.99.
- Votes and aggregate rating have a positive but limited correlation of about 0.3137.
- Table booking is more common in price ranges 3 and 4 than in ranges 1 and 2.

## Dataset notes and limitations
Nine cuisine values are missing and are labeled `Unknown` for analysis. The dataset has `Rating text`, which is a categorical label, but no written review comments. Review keyword and review-length analysis therefore require another source.

## Project structure
- `Dataset.csv`: source dataset.
- `cognifyz_complete_analysis.py`: Python analysis script.
- `analysis_notebook.ipynb`: step-by-step notebook.
- `charts/`: generated visualizations.
- `results_*.csv`: exported result tables.
- `Restaurant_Data_Analysis_Project_Report.pdf`: report.
- `Restaurant_Data_Analysis_Project_Report.docx`: editable report.

## How to run
Install dependencies:
```bash
pip install pandas numpy matplotlib jupyter
```
Keep `Dataset.csv` in the same folder as the Python script, then run:
```bash
python cognifyz_complete_analysis.py
```
Or open `analysis_notebook.ipynb` in Jupyter Notebook or VS Code.

## Portfolio description
Analyzed 9,551 restaurant records using Python, Pandas, NumPy, and Matplotlib. Performed data cleaning and exploratory analysis across cuisine popularity, city-level restaurant distribution, pricing, ratings, online delivery, restaurant chains, geographic patterns, and voting behavior. Created visualizations and exported result tables to support data-driven findings.

## Resume bullet
**Restaurant Data Analysis Project | Python, Pandas, NumPy, Matplotlib**
- Analyzed 9,551 restaurant records to identify cuisine trends, city-level patterns, pricing distribution, ratings, and service availability.
- Cleaned missing cuisine values, calculated category percentages and average ratings, and examined the relationship between votes and ratings.
- Built visualizations and documented findings in a structured report.

This is a portfolio project based on the supplied restaurant dataset and task brief. Follow any internship submission rules and disclose tools/work as required.
