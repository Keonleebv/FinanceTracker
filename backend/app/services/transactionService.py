# backend/app/services/transaction_service.py

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
