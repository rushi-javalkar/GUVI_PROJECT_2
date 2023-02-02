# import datetime
import pytest
from selenium import webdriver
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from TEST import Data
import time
# from datetime import date



time.sleep(5)


class vikas:
    # url="http://savitaarts.com/"


    def booting_function(self):
        self.driver = webdriver.Chrome("D:\\webdrivers\\chromedriver.exe")
        self.driver.get("http://savitaarts.com/")
        self.driver.maximize_window()
        time.sleep(5)
        # yield
        # self.driver.close()

    def test_get_title(self):
        #self.driver.get(self.url)
        assert self.driver.title == 'Savita Arts Goa | Led Broad Manufactures in Goa, led broads in panjim'
        print("SUCCESS # Web Title Captured Successfully")
        time.sleep(2)

    def Validate(self):
        self.driver.find_element(By.XPATH, "//ul[@id='top-menu']//a[normalize-space()='OUR SERVICES']").click()
        our_services=self.driver.find_element(By.XPATH,"//div[contains(@class,'et_pb_row et_pb_row_0')]//div[contains(@class,'et_pb_text_inner')]")
        print(our_services.text)

        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ul[@id='top-menu']//a[normalize-space()='PRODUCT FOCUS']").click()
        time.sleep(2)
        PRODUCT_FOCUS=self.driver.find_element(By.XPATH,"//a[@title='Picture4']//img").click()
        time.sleep(2)
        image1=self.driver.find_element(By.XPATH,"//button[@title='Next (Right arrow key)']")
        image1.click()
        time.sleep(2)
        image1.click()
        time.sleep(2)
        image1.click()
        time.sleep(2)
        image1.click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//ul[@id='top-menu']//a[normalize-space()='SUPPLY FOCUS']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ul[@id='top-menu']//a[normalize-space()='GALLERY']").click()
        self.driver.find_element(By.XPATH,"//a[@title='2']//img").click()
        img=self.driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        img.click()
        time.sleep(2)
        close = self.driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()

        client=self.driver.find_element(By.XPATH,"//ul[@id='top-menu']//a[normalize-space()='CLIENTS']")
        client.click()
        #print(client.text)
        retail_jewllery=self.driver.find_element(By.XPATH,"//div[contains(@class,'et_pb_row et_pb_row_0')]//div[1]//div[2]//div[1]//div[1]//div[1]//ul[1]//li[1]")
        print(retail_jewllery.text)
        time.sleep(2)


# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# cookie=driver.get_cookies()
# print(len(cookie))
# print(cookie)
# time.sleep(5)

# cookis={'name':'rushi','value':'9876543210'}
# driver.add_cookie(cookis)
#
# cookies=driver.get_cookies()
# print(len(cookies))
# print(cookies)

Art=vikas()
Art.booting_function()
Art.Validate()


















# driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-container']/div[@role='table']/div[2]/div[1]").click()
# time.sleep(3)

# a = driver.find_element(By.XPATH,"//div[@role='tablist']")
# print(a.text)

# nikename=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input').send_keys("Rsnea12j")
# time.sleep(2)
# other_id=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input').send_keys("12345")
# time.sleep(2)
# Drive_LN=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("94836112")
# time.sleep(2)
# Dri_EXp_date=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("1993-02-22")
# time.sleep(2)
# SSn=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input').send_keys("9483623456")
# time.sleep(2)
# Sip=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input').send_keys("12345678910")
# time.sleep(2)
#
#
# Nationality=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]').click()
# indian=driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.indian)
# action=ActionChains(driver)
# action.move_to_element(indian).click().perform()
#
# time.sleep(5)


# test=speedtest.__version__
# now=date.today()
# up_speed=test.upload()

# print(now)
# print(up_speed)


# n=range(1,1000)
# def prime(num):
#     for x in range(2,num):
#         if (num%x)==0:
#             return False
#     return True
# p=list(filter(prime, n))
# print(p)



