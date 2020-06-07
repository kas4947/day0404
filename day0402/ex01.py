import time
from selenium.webdriver import Chrome

#셀레늄을 이용한 자동로그인

chromeDriver = 'c:\\temp\\chromedriver.exe'

driver = Chrome(chromeDriver)

driver.get('https://login.coupang.com/login/login.pang')

time.sleep(3)

input_login = driver.find_element_by_id('login-email-input')
input_login.send_keys('park31500@naver.com')

time.sleep(3)

input_pw = driver.find_element_by_id("login-password-input")
input_pw.send_keys('1111')

time.sleep(3)


btn = driver.find_element_by_class_name('login__button')

btn.click()

time.sleep(3)

driver.quit()