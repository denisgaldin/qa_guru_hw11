import pytest
from selene import browser
from selenium import webdriver
from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVideo": False
    }
}

driver = webdriver.Remote(
    command_executor="https://selenoid.autotests.cloud/wd/hub",
    desired_capabilities=capabilities)


@pytest.fixture(scope='function', autouse=True)
def set_browser_size():
    browser.driver.set_window_size(1920, 1080)


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/'
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless=new')
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()