# E-commerce Transaction Dataset Analysis

## Video Demo:
https://youtu.be/qpRjwJy3dAw

## Description
This project analyzes e-commerce transaction data using Python and its embedded libraries.
The goal is to demonstrate basic data analysis logic, data aggregation, and reporting without external data analysis libraries. The program loads transaction data from a CSV file and allows the user to explore different analytical views through an interactive menu.

The dataset used in this project is synthetic and was created as an educational exercise and can serve as a beginner-level data analysis portfolio project. The dataset contains tens of thousands of transactions, which makes manual analysis impractical and justifies automated processing. The dataset simulates real-world e-commerce transactions and includes:
- Transaction ID
- User name
- User age
- Country
- Product category
- Purchase amount
- Payment method
- Transaction date

The project is structured around several агтсешщті responsible for a specific task.
The load_csv function reads the CSV file and converts each valid row into a dictionary representing a single transaction. This function also handles basic error checking, such as empty rows or invalid data types.
The aggregate_by_category function groups transactions by product category and calculates the total number of purchases, total amount of purchaces, and average purchase value for each category. This aggregated data is reused in later analysis steps.
The analyze_purchase_patterns function calculates the overall average purchase amount, identifies the top five categories by average purchase value, and finds extreme cases such as the largest purchases made by the youngest and oldest users.
User interaction is handled through an interactive menu implemented in the menu function. Based on the user’s choice, the program calls different output functions such as show_average_purchase, show_category_summary, show_top_categories, and show_top_spenders. Each of these functions is responsible only for formatting and displaying results, keeping presentation logic separate from analysis logic.
The format_table function generates a complete textual report that combines all analyses into a single formatted output. This report is might be saved to a file if the user choices the appropriate option.

The program provides an interactive menu that allows the user to choose which analysis to display. The menu options include:
- Viewing the overall average purchase amount
- Viewing aggregated statistics by product category
- Viewing top product categories by average purchase value
- Viewing top spenders among the youngest and oldest users
- Saving a full formatted analysis report to a text file

This interactive approach allows the user to explore the dataset step by step instead of viewing all results at once.

Future improvements may include demographic analysis such as more detailded age / country-based purchasing patterns, defining top 5 customer who made the biggest purchases accross all categories. Defining most popular payment method.

### How to Run:
- Clone the repository
- Make sure the CSV file is in the project folder
- Run the program from the terminal: python project.py ecommerce_transactions.csv
