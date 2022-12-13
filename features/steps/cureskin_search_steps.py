from behave import given, when, then


@then('No search results are shown')
def no_search_results(context):
    context.app.search_results_page.no_search_results()



