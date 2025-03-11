from flask import Flask, jsonify, request, abort
from myapp.models import db, Product

app = Flask(__name__)

@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    """Retrieve a product by its ID"""
    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found")
    
    return jsonify({
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "price": product.price,
        "stock": product.stock
    }), 200
