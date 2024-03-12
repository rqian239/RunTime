import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import ids

LOCAL_URL = "http://localhost:8050"

# Define a fixture for the WebDriver
@pytest.fixture(scope="function")
def driver():
    _driver = webdriver.Chrome(ChromeDriverManager().install())
    yield _driver
    _driver.quit() # runs after each test

def test_main_layout(driver):
    driver.get(LOCAL_URL)

    # Wait until the navbar element is present, timeout at 5 seconds
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, ids.NAVBAR))
    )

    assert driver.find_elements(By.ID, ids.NAVBAR)