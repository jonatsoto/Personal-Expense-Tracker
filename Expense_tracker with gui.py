import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# File where expenses will be stored
EXPENSES_FILE = 'expenses.csv'

# Function to add an expense
def add_expense():
    date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):")
    description = simpledialog.askstring("Input", "Enter description:")
    amount = simpledialog.askstring("Input", "Enter amount:")
    
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    messagebox.showinfo("Success", "Expense added successfully.")

# Function to view expenses
def view_expenses():
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            expenses = "\n".join([f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}" for row in reader])
        if expenses:
            messagebox.showinfo("Expenses", expenses)
        else:
            messagebox.showinfo("Expenses", "No expenses found.")
    except FileNotFoundError:
        messagebox.showinfo("Expenses", "No expenses found. Start adding some!")

# Function to delete an expense by date
def delete_expense():
    date = simpledialog.askstring("Input", "Enter date of expense to delete (YYYY-MM-DD):")
    expenses = []
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.reader(file)
        expenses = [row for row in reader if row[0] != date]

    with open(EXPENSES_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    messagebox.showinfo("Success", "Expense deleted successfully.")

# Main function to create the GUI
def main():
    root = tk.Tk()
    root.title("Personal Expense Tracker")

    tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
    tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=10)
    tk.Button(root, text="Delete Expense", command=delete_expense).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()