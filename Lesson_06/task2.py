from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput?")

search_box = driver.find_element(By.CSS_SELECTOR, "[id=newButtonName]")
search_box.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)


driver.quit()