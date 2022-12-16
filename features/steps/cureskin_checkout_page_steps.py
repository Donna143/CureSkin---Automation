from behave import given, when, then


@then('User is taken to checkout page')
def verify_checkout(context):
    context.app.checkout_page.verify_checkout()
