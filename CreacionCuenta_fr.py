
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.laduree.fr/creation-de-compte.html")
letters = string.ascii_lowercase

usr = driver.find_element_by_id("rbs-user-create-account-email")
usr.send_keys("sebastian.gallardo1@mail.udp.cl")


psw = driver.find_element_by_id("rbs-user-create-account-password")
psw.send_keys('passwordExample')

repsw = driver.find_element_by_id("rbs-user-create-account-confirm-password")
repsw.send_keys('passwordExample')

clk = driver.find_element_by_xpath('//*[@id="content-column"]/div/div[1]/div/div[1]/form/fieldset/div[6]/button').click()