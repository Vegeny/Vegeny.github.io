import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    inpt_fields=browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for i in inpt_fields:
        i.send_keys("Word")
    time.sleep(4)
    button=browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(5)
finally:
    browser.quit()