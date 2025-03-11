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
def test_list_by_availability(client):
    # Create test products
    available_product = Product(name="Laptop", category="Electronics", price=60000, stock=10)
    unavailable_product = Product(name="Phone", category="Electronics", price=30000, stock=0)
    
    db.session.add_all([available_product, unavailable_product])
    db.session.commit()

    # Send GET request to list available products
    response = client.get("/products?available=true")

    # Assertions
    assert response.status_code == 200  # Successful request
    data = response.get_json()
    assert isinstance(data, list)  # Should return a list
    assert len(data) == 1  # Only one product should be available
    assert data[0]["name"] == "Laptop"  # The available product should be Laptop
