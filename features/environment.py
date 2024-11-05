from features.steps.login_steps import setup_driver

def before_scenario(context, scenario):
    context.driver = setup_driver()

def after_scenario(context, scenario):
    context.driver.quit()
