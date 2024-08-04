# backend/app/models/transaction.py

class Transaction:
    def __init__(self, date, description, category, amount):
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount
