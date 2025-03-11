import factory
from myapp.models import Product  # Update with your actual app name
from faker import Faker

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda _: fake.sentence())
    price = factory.LazyAttribute(lambda _: round(fake.random_number(digits=2), 2))
    stock = factory.LazyAttribute(lambda _: fake.random_int(min=0, max=100))

# Usage:
# product = ProductFactory()
