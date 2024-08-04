# backend/app/services/transaction_service.py

import pandas as pd
from app.models.transaction import Transaction
from app.repositories.transactionRepo import transactionRepo

class TransactionService:
    def __init__(self, transaction_repo: transactionRepo):
        self.transaction_repo = transaction_repo
    
    def add_transaction(self, date, description, category, amount):
        transaction = Transaction(date, description, category, amount)
        self.transaction_repo.add_transaction(transaction)
    
    def get_transactions(self):
        return self.transaction_repo.get_transactions()
    
    def calculate_totals(self):
        transactions = self.get_transactions()
        income = sum(t[4] for t in transactions if t[3] == "Income")
        expenses = sum(t[4] for t in transactions if t[3] == "Expense")
        return income, expenses

    def export_transactions_to_csv(self, file_name='transactions.csv'):
        transactions = self.get_transactions()
        df = pd.DataFrame(transactions, columns=["ID", "Date", "Description", "Category", "Amount"])
        df.to_csv(file_name, index=False)