# 📊 Mobile Sales Data Pipeline

## 📋 Project Description

This project focuses on cleaning and analyzing sales data of mobile phones from different regions.  
Main tasks include:
- Filling missing values in `Quantity`, `Price`, and `Order ID`.
- Converting `Date` to the standard `YYYY-MM-DD` format.
- Checking for duplicate `Order ID`s.
- Calculating `Total Sales` for each order.
- Summarizing sales by region.

## 🏗️ Steps Performed

1. Load data from `data/sales_data.csv`.
2. Check for duplicate Order IDs and print warnings.
3. Handle missing values:
   - Fill `Quantity` and `Price` with their column averages.
   - Drop rows missing `Order ID`.
4. Format `Date` to `YYYY-MM-DD`.
5. Compute `Total Sales` = `Quantity * Price`.
6. Group and sum sales by region.
7. Save the cleaned data to the `output/` folder.

## 🚨 Notes

- Duplicate `Order ID`s are only printed, not removed (can be enabled in code).
- NumPy is used for basic validation tasks.

## 🖥️ Requirements

- Python 3.x  
- pandas  
- numpy  

Install dependencies with:

<pre>
pip install -r requirements.txt
</pre>

# 🧑‍💻 Author

Kavin Kishore   
B.Tech Student, DTU     
Built as a real-time data engineering mini project.