from flask import Blueprint, request, jsonify
from app.services.budget_service import BudgetService
from app.repositories.SQLiteBudgetRepo import SQLiteBudgetRepository

budgets_bp = Blueprint('budgets', __name__)
budget_repo = SQLiteBudgetRepository("budgets.db")
budget_service = BudgetService(budget_repo)

@budgets_bp.route("/add_budget", methods=["POST"])
def add_budget():
    data = request.json
    budget_service.add_budget(data["category"], data["amount"])
    return jsonify({"message": "Budget added successfully"}), 201

@budgets_bp.route("/budgets", methods=["GET"])
def get_budgets():
    budgets = budget_service.get_budgets()
    return jsonify(budgets), 200

@budgets_bp.route("/compare_budget", methods=["GET"])
def compare_budget():
    # Assuming you have access to transactions here
    transactions = []  # You need to fetch transactions from your transaction service
    comparison = budget_service.compare_budget(transactions)
    return jsonify(comparison), 200
