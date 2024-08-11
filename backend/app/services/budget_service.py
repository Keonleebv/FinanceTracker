import pandas as pd
from app.models.budget import Budget
from app.repositories.budgetRepo import BudgetRepository
from app.services.transaction_service import TransactionService
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository

# Adding here for comparison
transaction_repo = SQLiteTransactionRepository("transactions.db")
transaction_service = TransactionService(transaction_repo)

class BudgetService:
    def __init__(self, budget_repo, transaction_service):
        self.budget_repo = budget_repo
        self.transaction_service = transaction_service

    def add_budget(self, category, amount):
        budget = Budget(category, amount)
        self.budget_repo.add_budget(budget)

    def get_budgets(self):
        return self.budget_repo.get_budgets()

    def compare_budget(self):
        transactions = self.transaction_service.get_transactions()
        budgets = self.get_budgets()

        # Calculate total spending per category
        spending_by_category = {}
        for transaction in transactions:
            category = transaction[3]
            amount = transaction[4]
            if category in spending_by_category:
                spending_by_category[category] += amount
            else:
                spending_by_category[category] = amount

        # Compare spending to budgets
        comparison = []
        for budget in budgets:
            category = budget[1]
            budget_amount = budget[2]
            spent = spending_by_category.get(category, 0)
            remaining = budget_amount - spent
            comparison.append({
                "Category": category,
                "Budgeted Amount": budget_amount,
                "Spent Amount": spent,
                "Remaining Budget": remaining
            })

        return pd.DataFrame(comparison)

    def export_budgets_to_csv(self, file_name):
        comparison_df = self.compare_budget()
        comparison_df.to_csv(file_name, index=False, float_format='%.2f')
