import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link="https://suninjuly.github.io/simple_form_find_task.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    fn_field=browser.find_element(By.NAME, "first_name")
    fn_field.send_keys("Danna")
    ln_field=browser.find_element(By.NAME, "last_name")
    ln_field.send_keys("Jevg")
    city_field=browser.find_element(By.CSS_SELECTOR, ".city")
    city_field.send_keys("Pompey")
    country_field=browser.find_element(By.ID, "country")
    country_field.send_keys("Rome")
    button=browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(7)
finally:
    browser.quit()
