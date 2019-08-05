from selenium import webdriver
import time

username = 'fb_email@email.com'
password = 'fb_password'

url = 'http://www.simplysit.com/01496//vwIQW/?sc=1&sc=1&l=1&ppy=5772259&i=5772259'

driver = webdriver.Chrome()

driver.get(url)

username_box = driver.find_element_by_id('email').send_keys(username)
username_box = driver.send_keys(usr)
username_box = driver.find_element_by_id('pass').send_keys(password)
username_box = driver.send_key(pwd)

time.sleep(2)

login_btn = driver.find_element_by_id('loginbutton').click()
