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
def test_read_product(client):
    # Create a test product
    product = Product(name="Laptop", price=50000, stock=10)
    db.session.add(product)
    db.session.commit()

    # Fetch the product by ID
    response = client.get(f"/products/{product.id}")
    
    # Assertions
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Laptop"
    assert data["price"] == 50000
