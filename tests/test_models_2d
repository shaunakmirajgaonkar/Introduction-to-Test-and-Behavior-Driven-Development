import pytest
from myapp.models import Product

@pytest.mark.django_db
def test_list_all_products():
    # Create multiple products
    Product.objects.create(name="Product 1", description="First product", price=19.99, stock=5)
    Product.objects.create(name="Product 2", description="Second product", price=29.99, stock=10)
    Product.objects.create(name="Product 3", description="Third product", price=39.99, stock=15)
    
    # Retrieve all products
    products = Product.objects.all()

    # Assertions
    assert products.count() == 3
    assert products[0].name == "Product 1"
    assert products[1].name == "Product 2"
    assert products[2].name == "Product 3"
