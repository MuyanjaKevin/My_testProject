import pytest
from selenium.webdriver.chrome import webdriver


import pytest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import config
from src.common.BasePage import BasePage


@pytest.fixture(scope="function", name="app")
def main_app():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    yield BasePage(driver)
    driver.quit()


@pytest.fixture(scope="function")
def admin_setup(app):
    """Login as an admin"""
    app.go_to_site()
    # app.landing.
    return app
