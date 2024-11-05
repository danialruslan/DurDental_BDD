from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Browser initialization
def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    return driver

@given("I open the VSM login page")
def step_open_login_page(context):
    context.driver = setup_driver()
    context.driver.get("https://vsmonitor.com")
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "//button[@type='button']").click() # Click the Login button

@when("I enter valid credentials")
def step_enter_credentials(context):
    context.driver.find_element(By.ID, "username").send_keys("danial_ruslan@yahoo.com")
    context.driver.find_element(By.ID, "password").send_keys("Danial01!")
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click() # Click Log-in button

@then("I should be redirected to the VSM dashboard")
def step_check_dashboard(context):
    WebDriverWait(context.driver, 10).until(EC.url_to_be("https://vsmonitor.com/dashboard"))
    assert context.driver.current_url == "https://vsmonitor.com/dashboard", \
        f"Expected URL to be 'https://vsmonitor.com/dashboard' but found '{context.driver.current_url}'"

@then("the URL should be \"https://vsmonitor.com/dashboard\"")
def step_verify_dashboard_url(context):
    assert context.driver.current_url == "https://vsmonitor.com/dashboard", \
        f"Expected URL to be 'https://vsmonitor.com/dashboard' but got '{context.driver.current_url}'"

@given("I am logged into VSM")
def step_logged_into_vsm(context):
    step_open_login_page(context)
    step_enter_credentials(context)
    step_check_dashboard(context)

@when("I navigate to \"My user account\"")
def step_navigate_user_account(context):
    context.driver.find_element(By.XPATH, "(//div[@aria-label='nav-user-button'])[2]").click() # Click name to open menu
    my_account_link = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "user-profile")))
    my_account_link.click()

@then("I should see my name and email")
def step_verify_user_info(context):
    # Verify name is Danial
    input_name = context.driver.find_element(By.ID, "firstName")
    actual_name = input_name.get_attribute("value")
    expected_name = "Danial"
    assert actual_name == expected_name, f"Expected name '{expected_name}' but got '{actual_name}'"

    # Verify email is danial_ruslan@yahoo.com
    input_email = context.driver.find_element(By.ID, "email")
    actual_email = input_email.get_attribute("value")
    expected_email = "danial_ruslan@yahoo.com"
    assert actual_email == expected_email, f"Expected email '{expected_email}' but got '{actual_email}'"

@then("the URL should be \"https://vsmonitor.com/user/profile\"")
def step_verify_profile_url(context):
    WebDriverWait(context.driver, 10).until(EC.url_to_be("https://vsmonitor.com/user/profile"))
    assert context.driver.current_url == "https://vsmonitor.com/user/profile", \
        f"Expected URL to be 'https://vsmonitor.com/user/profile' but got '{context.driver.current_url}'"

# Teardown to close the browser after each scenario
def after_scenario(context, scenario):
    context.driver.quit()
