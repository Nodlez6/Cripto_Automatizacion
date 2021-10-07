
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.carnesdab.cl/web/reset_password")
letters = string.ascii_lowercase


correo = driver.find_element_by_id('login')
correo.send_keys("sebastian.gallardo1@mail.udp.cl")

clk = driver.find_element_by_xpath('//*[@id="wrapwrap"]/main/div/form/div[2]/button').click()