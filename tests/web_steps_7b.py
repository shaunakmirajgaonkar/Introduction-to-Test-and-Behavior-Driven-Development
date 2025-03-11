from behave import then
from selenium.webdriver.common.by import By

@then('I should see "{expected_text}" on the page')
def step_impl(context, expected_text):
    page_text = context.driver.find_element(By.TAG_NAME, "body").text
    assert expected_text in page_text, f'Expected "{expected_text}" to be found on the page, but it was not.'
