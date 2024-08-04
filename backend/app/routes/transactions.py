# backend/app/routes/transactions.py

from flask import Blueprint, request, jsonify
from app.services.transactionService import TransactionService
from app.repositories.SQLite import SQLiteTransactionRepository

# Set up the Blueprint and repository/service instances
transactions_bp = Blueprint('transactions', __name__)
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
