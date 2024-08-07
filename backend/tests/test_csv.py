import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.transaction_service import TransactionService
from app.repositories.sqlite import SQLiteTransactionRepository

# Initialize the repository and service
repo = SQLiteTransactionRepository("transactions.db")
service = TransactionService(repo)

# Add some sample transactions
service.add_transaction("2024-07-25", "Salary", "Income", 1000)
service.add_transaction("2024-07-26", "Groceries", "Expense", -200)

# Export transactions to CSV
service.export_transactions_to_csv("transactions23.csv")
