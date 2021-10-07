
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.carnesdab.cl/web/signup")
letters = string.ascii_lowercase

usr = driver.find_element_by_id("login")
usr.send_keys("sebastian.gallardo1@mail.udp.cl")

name = driver.find_element_by_id("name")
name.send_keys("Sebastian")

psw = driver.find_element_by_id("password")
psw.send_keys('passwordExample')

repsw = driver.find_element_by_id("confirm_password")
repsw.send_keys('passwordExample')

clk = driver.find_element_by_xpath('//*[@id="wrapwrap"]/main/div/form/div[5]/button').click()