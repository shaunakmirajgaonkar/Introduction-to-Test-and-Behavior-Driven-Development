import pytest
from myapp.models import Product

@pytest.mark.django_db
def test_read_product():
    # Create a product
    product = Product.objects.create(
        name="Test Product",
        description="This is a test product",
        price=99.99,
        stock=10
    )
    
    # Retrieve the product
    retrieved_product = Product.objects.get(id=product.id)

    # Assertions
    assert retrieved_product.name == "Test Product"
    assert retrieved_product.description == "This is a test product"
    assert retrieved_product.price == 99.99
    assert retrieved_product.stock == 10
