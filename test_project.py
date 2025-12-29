import pytest
from project import load_csv, aggregate_by_category, analyze_purchase_patterns, format_table

@pytest.fixture
def sample_data():
    return [
    {'transaction_id': '11540', 'user': 'Noah White', 'age': 43, 'country': 'France', 'category': 'Sports', 'amount': 231.72, 'payment_method': 'Debit Card', 'date': '2023-03-29'},
    {'transaction_id': '11590', 'user': 'Isabella Thompson', 'age': 28, 'country': 'Japan', 'category': 'Toys', 'amount': 259.55, 'payment_method': 'Credit Card', 'date': '2024-08-01'},
    {'transaction_id': '11642', 'user': 'Isabella Rodriguez', 'age': 25, 'country': 'Canada', 'category': 'Home & Kitchen', 'amount': 773.13, 'payment_method': 'UPI', 'date': '2025-01-25'},
    {'transaction_id': '11661', 'user': 'Noah Anderson', 'age': 62, 'country': 'Japan', 'category': 'Books', 'amount': 431.34, 'payment_method': 'PayPal', 'date': '2023-07-16'},
    {'transaction_id': '11663', 'user': 'Noah Harris', 'age': 38, 'country': 'Japan', 'category': 'Clothing', 'amount': 666.47, 'payment_method': 'Debit Card', 'date': '2024-10-03'},
    {'transaction_id': '11700', 'user': 'Isabella Clark', 'age': 46, 'country': 'Australia', 'category': 'Grocery', 'amount': 171.25, 'payment_method': 'Debit Card', 'date': '2025-01-01'},
    {'transaction_id': '11690', 'user': 'Isabella Rodriguez', 'age': 42, 'country': 'Mexico', 'category': 'Clothing', 'amount': 15.11, 'payment_method': 'Debit Card', 'date': '2025-01-08'},
    {'transaction_id': '12272', 'user': 'Oliver White', 'age': 65, 'country': 'Mexico', 'category': 'Electronics', 'amount': 529.78, 'payment_method': 'Credit Card', 'date': '2023-09-10'}
]

def test_load_csv():
    with pytest.raises(FileNotFoundError):
        load_csv("non_existed_file.csv")

def test_aggregate_by_category(sample_data):
    summary = aggregate_by_category(sample_data)

    assert "Sports" in summary
    assert summary["Sports"]["count"] == 1
    assert summary["Sports"]["total_amount"] == 231.72
    assert summary["Clothing"]["count"] == 2
    assert round(summary["Clothing"]["total_amount"], 2) == 681.58

def test_analyze_purchase_patterns(sample_data):
    summary = aggregate_by_category(sample_data)
    analysis = analyze_purchase_patterns(sample_data, summary)

    assert "average_purchase" in analysis
    assert analysis["average_purchase"] > 0
    assert len(analysis["top_categories"]) <= 5


def test_format_table(sample_data):
    summary = aggregate_by_category(sample_data)
    analysis = analyze_purchase_patterns(sample_data, summary)
    report = format_table(summary, analysis)

    assert "E-COMMERCE SALES REPORT" in report
    assert "Average purchase amount" in report
    assert "Sales by Category" in report
