import pytest
from myapp.models import Product

@pytest.mark.django_db
def test_find_product_by_name():
    # Create a product
    product = Product.objects.create(
        name="Test Product",
        description="This is a test product",
        price=49.99,
        stock=20
    )

    # Find product by name
    found_product = Product.objects.get(name="Test Product")

    # Assertions
    assert found_product is not None
    assert found_product.name == "Test Product"
    assert found_product.description == "This is a test product"
