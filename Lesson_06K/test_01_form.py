import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(params=["edge"])
def driver(request):
    service = EdgeService()
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button").click()

    wait = WebDriverWait(driver, 30)

    def get_border_color(element):
        return element.value_of_css_property("border-color")

    zip_code = driver.find_element(By.ID, "zip-code")
    first_name = driver.find_element(By.ID, "first-name")
    last_name = driver.find_element(By.ID, "last-name")
    address = driver.find_element(By.ID, "address")
    email = driver.find_element(By.ID, "e-mail")
    phone = driver.find_element(By.ID, "phone")
    city = driver.find_element(By.ID, "city")
    country = driver.find_element(By.ID, "country")
    job_position = driver.find_element(By.ID, "job-position")
    company = driver.find_element(By.ID, "company")

    wait.until(lambda d: get_border_color(zip_code) != "")

    red_colors = ["rgb(245, 194, 199)", "rgba(255, 0, 0, 1)"]
    green_colors = ["rgb(186, 219, 204)", "rgba(0, 128, 0, 1)", "rgb(40, 167, 69)"]  # может быть bootstrap green

    zip_color = get_border_color(zip_code)
    assert any(c in zip_color for c in red_colors), f"Zip code border color is not red: {zip_color}"

    for field in [first_name, last_name, address, email, phone, city, country, job_position, company]:
        color = get_border_color(field)
        assert any(c in color for c in green_colors), f"Field {field.get_attribute('id')} border color is not green: {color}"