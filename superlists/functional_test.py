from selenium import webdriver

browser = webdriver.Chrome('../resources/chromedriver')
browser.get('http://localhost:8000')

assert 'Congratulations' in browser.title