@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete an existing product"""
    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found")
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({"message": "Product deleted successfully"}), 200
