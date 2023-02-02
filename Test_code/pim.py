from selenium import webdriver
from selenium.webdriver.common.by import By
from TEST import Data
#from TEST.HRM import Searchnew
import time

class Test_PJ2:
    url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome("D:\\webdrivers\\chromedriver.exe")
    driver.maximize_window()
    time.sleep(10)
    Search_PIM = HRM.Searchnew.Search_Pim
    Sear=HRM.Searchnew.Search
    pi=HRM.Searchnew.PIM

    def TC_PIM_01(self):
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(By.NAME, value=HRM.Element.username).send_keys(HRM.data_Input.UserNameInput)
        time.sleep(2)
        if HRM.data_Input.UserNameInput != "Admin":
            print("Username Incorrect")
        self.driver.find_element(By.NAME, value=HRM.Element.password).send_keys(HRM.data_Input.PasswordInput)
        time.sleep(2)
        if HRM.data_Input.PasswordInput != "admin123":
            print("Password Incorrect")
        self.driver.find_element(By.XPATH, value=HRM.Element.login).click()
        time.sleep(5)

        self.sp=HRM.Searchnew(self.driver)
        self.sp.sendpim(Search_PIM)



r=Test_PJ2()
r.TC_PIM_01()