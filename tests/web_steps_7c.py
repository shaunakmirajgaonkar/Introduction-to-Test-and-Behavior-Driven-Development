from behave import then
from selenium.webdriver.common.by import By

@then('I should not see "{unexpected_text}" on the page')
def step_impl(context, unexpected_text):
    page_text = context.driver.find_element(By.TAG_NAME, "body").text
    assert unexpected_text not in page_text, f'Unexpected "{unexpected_text}" was found on the page.'
