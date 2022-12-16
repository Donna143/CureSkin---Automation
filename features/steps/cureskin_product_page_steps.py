from behave import given, when, then


@given('Open Product Detail page')
def open_product(context):
    product = 'products/cureskin-cleansing-gel'
    context.app.product_page.open_product(product)


@when('click to Buy it now')
def click_buy_now(context):
    context.app.product_page.click_buy_now()


@when('Click Add to cart')
def add_cart(context):
    context.app.product_page.add_cart()


@when('Open Cart page')
def view_cart(context):
    context.app.product_page.view_cart()






