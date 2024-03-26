from datetime import datetime

def calculate_days():
    start_date = datetime.strptime(input("Enter the start date (YYYY-MM-DD): "), "%Y-%m-%d")
    end_date = datetime.strptime(input("Enter the end date (YYYY-MM-DD): "), "%Y-%m-%d")
    return (end_date - start_date).days

print("The number of days between the two dates is:", calculate_days())
