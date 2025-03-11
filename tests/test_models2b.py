import pytest
from myapp.models import Product

@pytest.mark.django_db
def test_update_product():
    # Create a product
    product = Product.objects.create(
        name="Old Product",
        description="Old description",
        price=49.99,
        stock=5
    )
    
    # Update the product
    product.name = "Updated Product"
    product.description = "Updated description"
    product.price = 59.99
    product.stock = 15
    product.save()
    
    # Retrieve the updated product
    updated_product = Product.objects.get(id=product.id)

    # Assertions
    assert updated_product.name == "Updated Product"
    assert updated_product.description == "Updated description"
    assert updated_product.price == 59.99
    assert updated_product.stock == 15
