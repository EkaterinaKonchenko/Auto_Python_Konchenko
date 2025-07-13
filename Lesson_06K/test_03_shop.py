import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("first_name,last_name,postal_code", [("Ekaterina", "Konchenko", "347360")])
def test_shop_purchase(first_name, last_name, postal_code):
    driver = webdriver.Firefox()

    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item_id in items_to_add:
        wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    driver.find_element(By.ID, "continue").click()

    total_label = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_label.text
    assert "$58.29" in total_text, f"Expected total $58.29 but got {total_text}"

    driver.close()