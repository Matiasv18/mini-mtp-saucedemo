
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_validacion():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        # Abrir SauceDemo
        driver.get("https://www.saucedemo.com/")

        # =========================
        # 1. Inicio de sesión
        # =========================
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # =========================
        # 2. Agregar producto
        # =========================
        driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        ).click()

        # =========================
        # 3. Ir al carrito
        # =========================
        driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()

        # =========================
        # 4. Ir al checkout
        # =========================
        driver.find_element(
            By.ID,
            "checkout"
        ).click()

                # =========================
        # 5. Intentar continuar
        #    sin llenar los datos
        # =========================
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

                # =========================
        # 6. Verificar mensaje
        #    de validación
        # =========================
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "First Name is required" in error.text

        print("AUT-02: Validación de checkout exitosa")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_checkout_validacion()

