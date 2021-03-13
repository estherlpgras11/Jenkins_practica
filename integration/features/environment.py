from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture
def selenium_browser_chrome(context):
    options = Options()
    options.add_argument("--headless")
    context.browser = webdriver.Chrome(chrome_options=options)
    context.browser.implicitly_wait(15)
    yield context.browser
    context.browser.quit()


def before_feature(context, feature):
    use_fixture(selenium_browser_chrome, context)
