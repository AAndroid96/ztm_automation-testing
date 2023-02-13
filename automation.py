from selenium import webdriver

chrome_browser = webdriver.Chrome('/chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('')

print('Python Easy Demo' in chrome_browser.title)

assert 'Selenium Easy Demo' in chrome_browser.title
button_text = chrome_browser.find_element_by_class_name('')
print(button_text.get)

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'I AM EXTRA COOOOL' chrome_browser.find_element_by_id('display')

chrome_browser.quit()