from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link="http://suninjuly.github.io/get_attribute.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    x=int((browser.find_element(By.CSS_SELECTOR, "h2>img")).get_attribute("valuex"))
    inpt_field=browser.find_element(By.ID, "answer")
    inpt_field.send_keys(str(math.log(abs(12*math.sin(x)))))
    chk=browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    chk.click()
    rad=browser.find_elements(By.CSS_SELECTOR, "[type='radio']")
    rad[1].click()
    button=browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()