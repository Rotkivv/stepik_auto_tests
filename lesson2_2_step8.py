import os 
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

in1 = browser.find_element_by_css_selector('input[name="firstname"][required]')
in1.send_keys("Vik")

in2 = browser.find_element_by_css_selector('input[name="lastname"][required]')
in2.send_keys("Shi")

in3 = browser.find_element_by_css_selector('input[name="email"][required]')
in3.send_keys("test@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

in3 = browser.find_element_by_css_selector('#file[required]')
in3.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()
