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
def test_list_by_category(client):
    # Create test products
    product1 = Product(name="Laptop", category="Electronics", price=60000, stock=10)
    product2 = Product(name="Phone", category="Electronics", price=30000, stock=15)
    product3 = Product(name="Shoes", category="Fashion", price=2000, stock=50)
    
    db.session.add_all([product1, product2, product3])
    db.session.commit()

    # Send GET request to list products by category
    response = client.get("/products?category=Electronics")

    # Assertions
    assert response.status_code == 200  # Successful request
    data = response.get_json()
    assert isinstance(data, list)  # Should return a list
    assert len(data) == 2  # Two products should match the category
    assert all(product["category"] == "Electronics" for product in data)
