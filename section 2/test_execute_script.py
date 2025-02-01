from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link="http://suninjuly.github.io/execute_script.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    x=int(browser.find_element(By.ID, "input_value").text)
    ans=browser.find_element(By.ID, "answer")
    ans.send_keys(str(math.log(abs(12*math.sin(x)))))
    checkb=browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    checkb.click()
    rad=browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rad)
    rad.click()
    button=browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(10)
finally:
    browser.quit()
