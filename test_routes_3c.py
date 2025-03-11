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
def test_delete_product(client):
    # Create a test product
    product = Product(name="Smartphone", price=30000, stock=15)
    db.session.add(product)
    db.session.commit()

    # Delete the product
    response = client.delete(f"/products/{product.id}")

    # Assertions
    assert response.status_code == 204  # No content on successful deletion

    # Verify the product no longer exists
    deleted_product = Product.query.get(product.id)
    assert deleted_product is None
