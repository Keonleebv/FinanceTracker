from flask import Blueprint, request, jsonify
from app.services.transaction_service import TransactionService
from app.repositories.sqlite import SQLiteTransactionRepository

transactions_bp = Blueprint('transactions', __name__)

# Set up your repository and service instances
transaction_repo = SQLiteTransactionRepository("transactions.db")
transaction_service = TransactionService(transaction_repo)

@transactions_bp.route("/add_transaction", methods=["POST"])
def add_transaction():
    data = request.json
    transaction_service.add_transaction(data["date"], data["description"], data["category"], data["amount"])
    return jsonify({"message": "Transaction added successfully"}), 201

@transactions_bp.route("/transactions", methods=["GET"])
def get_transactions():
    transactions = transaction_service.get_transactions()
    return jsonify(transactions), 200
