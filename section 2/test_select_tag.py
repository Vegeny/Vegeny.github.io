from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link="https://suninjuly.github.io/selects1.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    select=Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(int(browser.find_element(By.ID, "num1").text)+int(browser.find_element(By.ID, "num2").text)))
    button=browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(10)
finally:
    browser.quit()