
# E-commerce Data Scraper & Cleaner 🛒📊

## 📌 Project Overview
This project is an automated ETL (Extract, Transform, Load) script built with Python. It extracts raw book data from an e-commerce website, cleans and formats the data, and exports it into a structured CSV file ready for business analysis.

## 🛠️ Technologies Used
* **Python** * **BeautifulSoup & Requests:** For web scraping and data extraction.
* **Pandas:** For data cleaning, string manipulation, and data formatting (Regex).

## 💡 What this script does:
1. **Extracts:** Scrapes Book Title, Price, Rating, and Availability.
2. **Transforms:** - Removes currency symbols and converts prices to float numbers.
   - Converts text-based ratings (e.g., "Three") into numeric values (3).
3. **Loads:** Saves the clean dataset as a `CSV` file.

## 🚀 Business Value
This tool saves hours of manual data entry and provides clean, structured data that can be immediately used in Excel or BI tools for competitor pricing analysis.
