from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
search_box = driver.find_element(By.CSS_SELECTOR, "[id=username]")
search_box.send_keys("tomsmith")
search_box = driver.find_element(By.CSS_SELECTOR, "[id=password]")
search_box.send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()
wait = WebDriverWait(driver, 10)
flash_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.flash.success")))
print(flash_message.text.strip())

sleep(5)

driver.quit()
