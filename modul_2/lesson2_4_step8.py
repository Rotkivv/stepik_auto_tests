from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )

if price:
    buttonB = browser.find_element_by_id("book")
    buttonB.click()


input1 = browser.find_element_by_css_selector('label>#input_value')

input2 = browser.find_element_by_css_selector('#answer')
input2.send_keys(calc(input1.text))

button = browser.find_element_by_id("solve")
button.click()


