from behave import when
from selenium.webdriver.common.by import By

@when('I press the "{button_text}" button')
def step_impl(context, button_text):
    button = context.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
    button.click()
