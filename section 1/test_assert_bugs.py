from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link=" http://suninjuly.github.io/registration2.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    fn_field=browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
    fn_field.send_keys("Word")
    ln_field=browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    ln_field.send_keys("Word")
    email_field=browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    email_field.send_keys("Word")
    button=browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(5)
    welcome_text_elt=browser.find_element(By.TAG_NAME, "h1")
    welcome_text=welcome_text_elt.text
    assert "Congratulations! You have successfully registered!"==welcome_text
finally:
    time.sleep(10)
    browser.quit()