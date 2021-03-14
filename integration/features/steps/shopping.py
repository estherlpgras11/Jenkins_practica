from behave import *
from selenium.webdriver.common.by import By
from time import sleep


@given('We are in the main site')
def step_impl(context):
    context.browser.get('http://localhost:8080')


@then('{total} items must be displayed')
def step_impl(context, total):
    row_count = len(context.browser.find_elements_by_xpath("//table/tbody/tr"))
    assert int(row_count) == int(total), f'Row count {row_count} is not the same than expected: {total}'


@then('"{item}" item must be displayed')
def step_impl(context, item):
    found = context.browser.find_element_by_id(f'name-{item}')
    assert found.text == item, f'Item "{item}" not found: "{found.text}"'


@then('We want to buy a "{item}" with "{email}" email')
def step_impl(context, item, email):
    context.browser.find_element_by_id(f'buy-{item}').click()
    form = context.browser.find_element_by_class_name('swal2-input')
    form.send_keys(email)
    context.browser.find_element_by_class_name('swal2-confirm').click()
    sleep(1)
    title = context.browser.find_element_by_class_name('swal2-title')
    assert title.text == 'Registered successfully', f'Order was not placed: {title.text}'
