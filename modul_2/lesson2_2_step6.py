from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector('label>#input_value')

input2 = browser.find_element_by_css_selector('#answer')
input2.send_keys(calc(input1.text))

option1 = browser.find_element_by_css_selector('#robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

option2 = browser.find_element_by_css_selector('#robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()