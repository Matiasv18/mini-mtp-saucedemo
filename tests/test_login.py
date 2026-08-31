from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_login_exitoso():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        inventory = driver.find_element(By.ID, "inventory_container")

        assert inventory.is_displayed()

        print("AUT-01: Inicio de sesión exitoso")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_exitoso()