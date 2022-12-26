from behave import given, when, then


@given('Open main page')
def open_google(context):
    context.app.main_page.open_google()


@when('Search for {search_word}')
def input_search(context, search_word):
    context.app.main_page.input_search(search_word)


@when('Click on Hamburger')
def click_hamburger(context):
    context.app.main_page.click_hamburger()


@when('Click to Shop by Concern - Select Acne')
def click_concern_acne(context):
    context.app.main_page.click_concern_acne()


@when('Mobile Click to Shop by Concern - Select Acne')
def mobile_click_concern_acne(context):
    context.app.main_page.mobile_click_concern_acne()




