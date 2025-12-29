# Ecommerce Transaction Dataset Analysis

## Description
This project analyzes e-commerce transaction data using Python and its embedded libraries.
The goal is to demonstrate basic data analysis logic, data aggregation, and reporting without external data analysis libraries.

The dataset used in this project is synthetic and was created as an educational exercise and can serve as a beginner-level data analysis portfolio project.

The project performs the following analyses:
- Calculates the average purchase amount across all transactions and per product category
- Aggregates transactions by product category (count and total sales)
- Identifies top 5 categories by average purchase value
- Highlights extreme cases:
  - Largest purchases made by the youngest users
  - Largest purchases made by the oldest users

Future improvements may include demographic analysis such as more detailded age / country-based purchasing patterns, defining top 5 customer who made the biggest purchases accross all categories. Defining most popular payment method.

### How to Run:
- Clone the repository
- Make sure the CSV file is in the project folder
- Run the program from the terminal: python project.py ecommerce_transactions.csv

### The program will:
- Print the analysis report to the terminal
- Save the report to report.txt
