from behave import given
from service.models import db, Product

@given('the following products exist')
def step_impl(context):
    """ Load background data (products) into the database """
    for row in context.table:
        product = Product(
            name=row['name'],
            category=row['category'],
            available=row['available'].lower() == "true",
            price=float(row['price'])
        )
        db.session.add(product)
    db.session.commit()
