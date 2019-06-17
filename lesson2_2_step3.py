from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_css_selector('#num1')
y = browser.find_element_by_css_selector('#num2')

c = str(int(x.text)+int(y.text))
print(c)
select = webdriver.support.ui.Select(browser.find_element_by_tag_name("select"))
select.select_by_value(c)


button = browser.find_element_by_css_selector("button.btn")
button.click()