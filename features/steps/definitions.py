from behave import given, when, then
from src.main import Calculator


@given('we have behave installed')
def step_implements(context):
    pass


@when('we implement a test')
def step_implements(context):
    assert True is not False


@then('behave will test it for us!')
def step_implements(context):
    assert context.failed is False
