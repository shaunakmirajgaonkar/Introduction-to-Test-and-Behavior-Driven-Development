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
def test_list_all_products(client):
    # Create test products
    product1 = Product(name="Laptop", price=60000, stock=10)
    product2 = Product(name="Headphones", price=5000, stock=20)
    db.session.add_all([product1, product2])
    db.session.commit()

    # Send GET request to list all products
    response = client.get("/products")

    # Assertions
    assert response.status_code == 200  # Successful request
    data = response.get_json()
    assert isinstance(data, list)  # Should return a list
    assert len(data) == 2  # Two products should be returned
    assert data[0]["name"] == "Laptop"
    assert data[1]["name"] == "Headphones"
