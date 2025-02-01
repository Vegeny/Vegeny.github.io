from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link="https://suninjuly.github.io/math.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    x=int(browser.find_element(By.CSS_SELECTOR, "div.form-group span#input_value").text)
    field=browser.find_element(By.CSS_SELECTOR, "div.form-group input#answer")
    field.send_keys(str(math.log(abs(12*math.sin(x)))))
    check=browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    check.click()
    rad=browser.find_element(By.CSS_SELECTOR, "[type='radio']#robotsRule")
    rad.click()
    button=browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    time.sleep(7)
finally:
    browser.quit()