import pandas as pd

def add_trans(date, description, category, amount):
    new_transaction = pd.DataFrame([[date, description, category, amount]], 
                                   columns=["Date", "Description", "Category", "Amount"])
    return new_transaction

def calculator(df):
    income = df[df["Category"].str.lower() == "income"]["Amount"].sum()
    expenses = df[df["Category"].str.lower() == "expense"]["Amount"].sum()
    return income, expenses
