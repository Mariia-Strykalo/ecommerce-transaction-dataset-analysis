import csv
import sys


def main():
    if len(sys.argv) == 2:
        data = load_csv(sys.argv[1].strip())
    else:
        data = load_csv(input("File Name: ").strip())

    summary = aggregate_by_category(data)
    analysis = analyze_purchase_patterns(data, summary)
    report = format_table(summary, analysis)
    print(report)

    with open("report.txt", "w") as file:
        file.write(report)



def load_csv(path: str):
    """
    Load e-commerce transactions from a CSV file.
    Returns a list of dictionaries, one per transaction.
    """
    data = []

    try:
        with open(path) as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    transaction = {
                        "transaction_id": row["Transaction_ID"],
                        "user": row["User_Name"],
                        "age": int(row["Age"]),
                        "country": row["Country"],
                        "category": row["Product_Category"],
                        "amount": float(row["Purchase_Amount"]),
                        "payment_method": row["Payment_Method"],
                        "date": row["Transaction_Date"],
                    }
                    data.append(transaction)

                # skip rows with incorrect or missing data
                except (ValueError, KeyError):
                    continue

    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {path}")

    return data



def aggregate_by_category(data):
    """
    Aggregate transactions by product category.
    Returns a dictionary with counts and total sales per category.
    """
    summary = {}

    for transaction in data:
        category = transaction["category"]
        amount = transaction["amount"]

        if category not in summary:
            summary[category] = {
                "count": 0,
                "total_amount": 0.0,
            }

        summary[category]["count"] += 1
        summary[category]["total_amount"] += amount

    # Average purchase per category
    for category, stats in summary.items():
        stats["average_amount"] = stats["total_amount"] / stats["count"]

    return summary



def analyze_purchase_patterns(data: list[dict], summary: dict):
    # Average purchase overall
    total_amount = sum(row["amount"] for row in data)
    average_purchase = total_amount / len(data)

    # Top categories by average purchase
    top_categories = sorted(
        summary.items(),
        key=lambda x: x[1]["average_amount"],
        reverse=True
    )[:5]

    # Young & old big spenders
    top_big_purchases_by_youngest_user = sorted(
        data,
        key=lambda x: (x["age"], -x["amount"])
    )[:5]

    top_big_purchases_by_oldest_users = sorted(
        data,
        key=lambda x: (-x["age"], -x["amount"])
    )[:5]

    # Consequent
    return {
        "average_purchase": average_purchase,
        "top_categories": top_categories,
        "top_big_purchases_by_youngest_user": top_big_purchases_by_youngest_user,
        "top_big_purchases_by_oldest_users": top_big_purchases_by_oldest_users
    }


def format_table(summary: dict, analysis: dict):
    lines = []

    # Report title
    lines.append("E-COMMERCE SALES REPORT")
    lines.append("=" * 30)
    lines.append("")

    # Overall average
    lines.append(f"Average purchase amount: ${analysis['average_purchase']:.2f}")
    lines.append("")

    # Category summary
    lines.append("Sales by Category:")
    lines.append("-" * 30)

    for category, stats in summary.items():
        lines.append(
            f"{category:15} | "
            f"Count: {stats['count']:5} | "
            f"Total: ${stats['total_amount']:.2f}"
        )

    lines.append("")
    lines.append("Top Categories by Average Purchase:")
    lines.append("-" * 30)

    for category, stats in analysis["top_categories"]:
        lines.append(
            f"{category:15} | Average purchase: ${stats['average_amount']:.2f}"
        )

    lines.append("")
    lines.append("Top Large Purchases Among the Youngest Users:")
    lines.append("-" * 30)

    for row in analysis["top_big_purchases_by_youngest_user"]:
        lines.append(
            f"{row['user']} ({row['age']} y.o.) - ${row['amount']:.2f}"
        )

    lines.append("")
    lines.append("Top Large Purchases Among the Oldest Users:")
    lines.append("-" * 30)

    for row in analysis["top_big_purchases_by_oldest_users"]:
        lines.append(
            f"{row['user']} ({row['age']} y.o.) - ${row['amount']:.2f}"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    main()
