import sys
import os
import unittest

# # Add the 'backend' directory to sys.path to import the 'app' package
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Correct import paths based on directory structure
from app.services.transaction_service import TransactionService
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        # Use an in-memory SQLite database for testing
        self.repo = SQLiteTransactionRepository(":memory:")  
        self.service = TransactionService(self.repo)

    def test_add_transaction(self):
        self.service.add_transaction("2024-07-25", "Salary", "Income", 1000)
        transactions = self.service.get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][1], "2024-07-25")
        self.assertEqual(transactions[0][2], "Salary")
        self.assertEqual(transactions[0][3], "Income")
        self.assertEqual(transactions[0][4], 1000)

    def test_get_transactions(self):
        self.service.add_transaction("2024-07-25", "Salary", "Income", 1000)
        self.service.add_transaction("2024-07-26", "Groceries", "Expense", -200)
        transactions = self.service.get_transactions()
        self.assertEqual(len(transactions), 2)

    def test_calculate_totals(self):
        self.service.add_transaction("2024-07-25", "Salary", "Income", 1000)
        self.service.add_transaction("2024-07-26", "Groceries", "Expense", -200)
        income, expenses = self.service.calculate_totals()
        self.assertEqual(income, 1000)
        self.assertEqual(expenses, -200)

    def test_export_transactions_to_csv(self):
        # Add transactions
        self.service.add_transaction("2024-07-25", "Salary", "Income", 1000)
        self.service.add_transaction("2024-07-26", "Groceries", "Expense", -200)

        # Export to CSV
        file_name = "test_transactions.csv"
        self.service.export_transactions_to_csv(file_name)

        # Check if file exists
        self.assertTrue(os.path.exists(file_name))

        # Verify file content
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 3)  # Header + 2 transactions
            self.assertEqual(lines[0].strip(), "ID,Date,Description,Category,Amount")
            self.assertEqual(lines[1].strip(), "1,2024-07-25,Salary,Income,1000.00")
            self.assertEqual(lines[2].strip(), "2,2024-07-26,Groceries,Expense,-200.00")

        # Clean up
        os.remove(file_name)
        
if __name__ == "__main__":
    unittest.main()
