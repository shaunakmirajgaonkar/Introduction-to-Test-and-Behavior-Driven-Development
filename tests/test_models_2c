import pytest
from myapp.models import Product

@pytest.mark.django_db
def test_delete_product():
    # Create a product
    product = Product.objects.create(
        name="Sample Product",
        description="This product will be deleted",
        price=29.99,
        stock=10
    )
    
    # Store product ID before deletion
    product_id = product.id

    # Delete the product
    product.delete()
    
    # Verify the product is deleted
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=product_id)
