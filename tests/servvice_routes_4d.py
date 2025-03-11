from flask import Flask, jsonify, request, abort
from models import Product  # Assuming Product model is defined in models.py

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def list_products():
    """Retrieve products based on query parameters: name, category, or availability"""
    name = request.args.get("name")
    category = request.args.get("category")
    availability = request.args.get("available")

    query = Product.query  # Start with base query

    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
    
    if category:
        query = query.filter_by(category=category)
    
    if availability is not None:
        is_available = availability.lower() == "true"  # Convert string to boolean
        query = query.filter_by(available=is_available)
    
    products = query.all()
    return jsonify([product.serialize() for product in products]), 200

if __name__ == "__main__":
    app.run(debug=True)
