from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    # Evite que la page se referme de suite
    chrome_options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(chrome_options)
    context.driver.implicitly_wait(10)

#def after_all(context):
#    context.driver.quit()