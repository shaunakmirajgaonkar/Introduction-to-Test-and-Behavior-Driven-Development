@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Update an existing product"""
    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found")
    
    data = request.get_json()
    if "name" in data:
        product.name = data["name"]
    if "category" in data:
        product.category = data["category"]
    if "price" in data:
        product.price = data["price"]
    if "stock" in data:
        product.stock = data["stock"]

    db.session.commit()
    return jsonify({
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "price": product.price,
        "stock": product.stock
    }), 200
