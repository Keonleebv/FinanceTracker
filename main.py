# Imports
import pandas as pd
from datetime import datetime

# Functions
def add_trans(date, description, category, amount):
    # Create a new transaction DataFrame
    new_transaction = pd.DataFrame([[date, description, category, amount]], 
                                   columns=["Date", "Description", "Category", "Amount"])
    return new_transaction

def calculator(df):
    # Calculate total income and expenses
    income = df[df["Category"] == "Income"]["Amount"].sum()
    expenses = df[df["Category"] == "Expense"]["Amount"].sum()
    return income, expenses

def main():
    transactions = pd.DataFrame(columns=["Date", "Description", "Category", "Amount"])
    
    while True:
        command = input("\nEnter command (add/view/exit): ").strip().lower()
        
        if command == "add":
            # Automatically set the current date and time
            curr_date = datetime.now()
            date_str = curr_date.strftime("%Y-%m-%d %H:%M:%S")
            
            date = date_str
            description = input("\nDescription: ")
            category = input("\nCategory (Income/Expense): ")
            amount = float(input("\nAmount: "))
            
            # Add the new transaction
            new_transaction = add_trans(date, description, category, amount)
            transactions = pd.concat([transactions, new_transaction], ignore_index=True)

            # Make view start at index 1
            transactions.index = range(1, len(transactions) + 1)
            
        elif command == "view":
            # Display the entire transactions DataFrame
            print("\nTransactions:")
            print(transactions)
            
            # Calculate and display totals
            income, expenses = calculator(transactions)
            print(f"\nTotal Income: {income}")
            print(f"Total Expenses: {expenses}\n")
            
        elif command == "exit":
            break

if __name__ == "__main__":
    main()
