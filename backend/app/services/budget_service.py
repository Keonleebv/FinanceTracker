from app.models.budget import Budget
from app.repositories.budgetRepo import BudgetRepository

class BudgetService:
    def __init__(self, budget_repo: BudgetRepository):
        self.budget_repo = budget_repo

    def add_budget(self, category, amount):
        budget = Budget(category, amount)
        self.budget_repo.add_budget(budget)

    def get_budgets(self):
        return self.budget_repo.get_budgets()

    def compare_budget(self, transactions):
        budgets = self.get_budgets()
        budget_dict = {budget[1]: budget[2] for budget in budgets}
        comparison = {}
        for transaction in transactions:
            category = transaction[3]
            if category in budget_dict:
                if category not in comparison:
                    comparison[category] = 0
                comparison[category] += transaction[4]
        return comparison
