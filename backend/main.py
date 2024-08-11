from flask import Flask
from app.routes.transactions import transactions_bp
from app.routes.budgets import budgets_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(transactions_bp, url_prefix='/')
app.register_blueprint(budgets_bp)

# Define a route for the root URL
@app.route("/")
def home():
    return "Welcome to the Personal Finance Tracker API!"

if __name__ == "__main__":
    app.run(debug=True)


