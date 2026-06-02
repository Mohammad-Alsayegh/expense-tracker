import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def add_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            print("\nAll Expenses:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found yet.")


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            add_expense(amount, category)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
