import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link="http://suninjuly.github.io/find_link_text"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    s=str(math.ceil(math.pow(math.pi, math.e)*10000))
    link=browser.find_element(By.LINK_TEXT, s)
    link.click()
    fn_field=browser.find_element(By.NAME, "first_name")
    fn_field.send_keys("Danna")
    ln_field=browser.find_element(By.NAME, "last_name")
    ln_field.send_keys("Jevg")
    city_field=browser.find_element(By.CSS_SELECTOR, ".city")
    city_field.send_keys("Pompey")
    country_field=browser.find_element(By.ID, "country")
    country_field.send_keys("Rome")
    button=browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    time.sleep(7)
finally:
    browser.quit()
