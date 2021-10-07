
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.laduree.fr/mon-compte/mes-informations.html")
letters = string.ascii_lowercase

passw = driver.find_element_by_id('rbs-user-change-password-current')
passw.send_keys("contraActual")

npassw = driver.find_element_by_name('rbs-user-change-password-new')
passw.send_keys("contraNueva")

repassw = driver.find_element_by_name('rbs-user-change-password-confirm-password')
repassw.send_keys("contraNueva")

clk = driver.find_element_by_xpath('//*[@id="content-column"]/div/div[2]/div/form/fieldset/div[4]/div/button').click()