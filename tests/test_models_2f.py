import pytest
from myapp.models import Product, Category

@pytest.mark.django_db
def test_find_products_by_category():
    # Create a category
    category = Category.objects.create(name="Electronics")

    # Create products in the category
    Product.objects.create(name="Laptop", category=category, price=50000, stock=10)
    Product.objects.create(name="Smartphone", category=category, price=30000, stock=20)

    # Retrieve products by category
    products = Product.objects.filter(category=category)

    # Assertions
    assert products.count() == 2
    assert products[0].name == "Laptop"
    assert products[1].name == "Smartphone"
