from behave import then
from selenium.webdriver.common.by import By

@then('I should see the message "{expected_message}"')
def step_impl(context, expected_message):
    page_text = context.driver.find_element(By.TAG_NAME, "body").text
    assert expected_message in page_text, f'Expected message "{expected_message}" was not found on the page.'
