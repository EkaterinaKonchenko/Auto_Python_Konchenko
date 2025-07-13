import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = ChromeService()
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait = WebDriverWait(driver, 45)
    result_element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    screen_text = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert screen_text == "15", f"Expected result to be 15 but got {screen_text}"