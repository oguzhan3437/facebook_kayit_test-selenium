from selenium import webdriver
import time
import random


a=random.randint(1,9)

browser=webdriver.Chrome()

browser.get("https://tr-tr.facebook.com/")
time.sleep(2)

yeniad=browser.find_element_by_name("firstname")
yenisoyad=browser.find_element_by_name("lastname")
yenimail1=browser.find_element_by_xpath("//*[@id='u_0_o']")
time.sleep(1)
yenimail2=browser.find_element_by_xpath("//*[@id='u_0_r']")
yenisifre=browser.find_element_by_xpath("//*[@id='u_0_v']")
cinsiyet=browser.find_element_by_name("sex")
kayit=browser.find_element_by_name("websubmit")
dt=browser.find_element_by_xpath("//*[@id='year']")

yeniad.send_keys("oguzhanedc")
yenisoyad.send_keys("cetinec")
yenimail1.send_keys("dcbv",a,"cbvcbcbcvb@gmail.com")
yenimail2.send_keys("dcbv",a,"cbvcbcbcvb@gmail.com")
yenisifre.send_keys("dsadsad1321")
cinsiyet.click()
for option in dt.find_elements_by_tag_name('option'):
    if option.text == '1970':
        option.click() 
        break


time.sleep(2)
kayit.click()

time.sleep(2)






time.sleep(4)

browser.close()
