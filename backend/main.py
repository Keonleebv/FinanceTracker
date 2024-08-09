from flask import Flask
from app.routes.transactions import transactions_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(transactions_bp, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)

with app.test_request_context():
    print(app.url_map)
