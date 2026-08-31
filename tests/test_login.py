import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _build_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    for browser_path in [
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]:
        if os.path.exists(browser_path):
            options.binary_location = browser_path
            break

    return webdriver.Chrome(options=options)


def test_login_exitoso():
    driver = _build_driver()

    try:
        driver.get("https://www.saucedemo.com/")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        inventory = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "inventory_container"))
        )

        assert inventory.is_displayed()

        print("AUT-01: Inicio de sesión exitoso")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_exitoso()