from selenium import webdriver

chrome_browser = webdriver.Chrome(r"C:\Users\Francis\Desktop\py\ZTM_Python\Aulas\Selenium\chromedriver.exe")

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(show_message_button)
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('HEYYYYY ABCDE')

show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'HEYYYYY ABCDE' in output_message.text

user_button2 = chrome_browser.find_elements_by_css_selector('#get-input > .btn')
print(user_button2)

# CLOSE Pode não funcionar.. tentar chamar 2 vezes ou usar o quit()
# chrome_browser.close()

chrome_browser.quit()

# WAIT no script
# Usar módulo time e o metódo sleep...
