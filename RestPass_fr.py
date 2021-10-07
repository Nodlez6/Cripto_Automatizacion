
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.laduree.fr/identification.html")
letters = string.ascii_lowercase

clk = driver.find_element_by_xpath('//*[@id="content-column"]/div/div[1]/div/div[1]/form/fieldset/div[3]/p/a').click()

correo = driver.find_element_by_name('reset-password-email')
correo.send_keys("sebastian.gallardo1@mail.udp.cl")

clk2 = driver.find_element_by_xpath('//*[@id="reset-password-modal-main-content"]/div/div/div[2]/div/div[1]/button').click()