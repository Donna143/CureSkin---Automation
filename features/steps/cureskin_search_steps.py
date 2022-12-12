from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open main page')
def open_google(context):
    context.app.main_page.open_google()


@when('Search for {search_word}')
def input_search(context, search_word):
    context.app.main_page.input_search(search_word)


@then('No search results are shown')
def no_search_results(context):
    context.app.search_results_page.no_search_results()



