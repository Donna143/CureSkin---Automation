from behave import given, when, then


@then('For Acne is shown')
def for_acne_shown(context):
    context.app.acne_page.for_acne_shown()
