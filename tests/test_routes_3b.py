import pytest
from myapp import create_app
from myapp.models import db, Product

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

@pytest.mark.usefixtures("client")
def test_update_product(client):
    # Create a test product
    product = Product(name="Laptop", price=50000, stock=10)
    db.session.add(product)
    db.session.commit()

    # Update the product
    update_data = {"name": "Gaming Laptop", "price": 60000, "stock": 8}
    response = client.put(f"/products/{product.id}", json=update_data)

    # Assertions
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Gaming Laptop"
    assert data["price"] == 60000
    assert data["stock"] == 8
