from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector('label>#input_value')
print(input1.text)

input2 = browser.find_element_by_css_selector('#answer')
input2.send_keys(calc(input1.text))

option1 = browser.find_element_by_css_selector('#robotCheckbox')
option1.click()

option2 = browser.find_element_by_css_selector('#robotsRule')
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()