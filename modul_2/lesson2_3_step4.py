from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

confirm = browser.switch_to.alert
confirm.accept()

time.sleep(1)

input1 = browser.find_element_by_css_selector('label>#input_value')

input2 = browser.find_element_by_css_selector('#answer')
input2.send_keys(calc(input1.text))

button = browser.find_element_by_css_selector("button.btn")
button.click()