import pytest
from myapp.models import Product

@pytest.mark.django_db
def test_find_available_products():
    # Create products with different stock levels
    Product.objects.create(name="Laptop", price=50000, stock=10)
    Product.objects.create(name="Smartphone", price=30000, stock=0)  # Out of stock
    Product.objects.create(name="Tablet", price=20000, stock=5)

    # Retrieve only available products (stock > 0)
    available_products = Product.objects.filter(stock__gt=0)

    # Assertions
    assert available_products.count() == 2
    assert all(product.stock > 0 for product in available_products)
d
