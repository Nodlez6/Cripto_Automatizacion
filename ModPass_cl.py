
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://carnesdab.cl/my/security")
letters = string.ascii_lowercase

passw = driver.find_element_by_id('current')
passw.send_keys("contraActual")

npassw = driver.find_element_by_name('new')
passw.send_keys("contraNueva")

repassw = driver.find_element_by_name('new2')
repassw.send_keys("contraNueva")

clk = driver.find_element_by_xpath('//*[@id="wrap"]/div/div/section[1]/form/button').click()