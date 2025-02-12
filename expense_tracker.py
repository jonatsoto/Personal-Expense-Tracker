import csv
from datetime import datetime

# File where expenses will be stored
EXPENSES_FILE = 'expenses.csv'

# Function to add an expense
def add_expense(date, description, amount):
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    print("Expense added successfully.")

# Function to view expenses
def view_expenses():
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}")
    except FileNotFoundError:
        print("No expenses found. Start adding some!")

# Function to delete an expense by date
def delete_expense(date):
    expenses = []
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.reader(file)
        expenses = [row for row in reader if row[0] != date]

    with open(EXPENSES_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    print("Expense deleted successfully.")

# Main function
def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(date, description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            date = input("Enter date of expense to delete (YYYY-MM-DD): ")
            delete_expense(date)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()