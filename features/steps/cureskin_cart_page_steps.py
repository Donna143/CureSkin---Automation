from behave import given, when, then


@when('Delete the product')
def delete_product(context):
    context.app.cart_page.delete_product()


@then('Cart is empty')
def cart_empty(context):
    context.app.cart_page.cart_empty()

