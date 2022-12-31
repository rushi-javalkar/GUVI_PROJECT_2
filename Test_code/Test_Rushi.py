from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from TEST import Data
import pytest
import time


class Test_PJ2:
    url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome("D:\\webdrivers\\chromedriver.exe")
    driver.maximize_window()
    time.sleep(4)
    def login(self):
        self.driver.get(self.url)
        time.sleep(6)
        # Login
        self.driver.find_element(By.NAME, value=Data.login.E_login.username).send_keys(Data.login.I_login.UserNameInput)
        time.sleep(2)
        if Data.login.I_login.UserNameInput != "Admin":
            print("Username Incorrect")
        self.driver.find_element(By.NAME, value=Data.login.E_login.password).send_keys(Data.login.I_login.PasswordInput)
        time.sleep(2)
        if Data.login.I_login.PasswordInput != "admin123":
            print("Password Incorrect")
        self.driver.find_element(By.XPATH, value=Data.login.E_login.login1).click()
        time.sleep(6)


        # validate the search (text box)
    def TC_PIM_01(self):
        # search Admin
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Admin)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Admin).click()
        time.sleep(5)
        actual_admin = self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Act_Admin)
        print(actual_admin.text)


        # search Pim
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Pim)
        time.sleep(2)
        self.driver.find_element(By.XPATH,value=Data.TC_PIM_01.E_menu.PIM).click()
        time.sleep(5)
        actual_pim = self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Act_pim)
        print(actual_pim.text)
        # search Leave
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Leave)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Leave).click()
        time.sleep(5)
        actual_leave = self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Act_leave)
        print(actual_leave.text)
        # search Time
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Time)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Time).click()
        time.sleep(5)
        actual_time = self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Act_time)
        print(actual_time.text)
        # search _Recruitment
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Recruitment)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Recruitment).click()
        time.sleep(5)
        #My_Info
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_My_Info)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.My_Info).click()
        time.sleep(5)
        #Search_Performance
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Performance)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Performance).click()
        time.sleep(5)
        #Search_Dashboard
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Dashboard)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Dashboard).click()
        time.sleep(5)
        #Search_Directory
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Directory)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Directory).click()
        time.sleep(5)
        #Search_Maintenance
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Maintenance)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Maintenance).click()
        time.sleep(5)

        password1 = self.driver.find_element(By.NAME, value=Data.login.E_login.password).send_keys(Data.login.I_login.PasswordInput)
        time.sleep(2)
        Confirm = self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.confirm).click()
        time.sleep(5)
        #Buzz
        Search_Test_Box=self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Buzz)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Buzz).click()
        time.sleep(5)


    def TC_PIM_02(self):
        # self.driver.get(self.url)
        # time.sleep(2)
        # #Login
        # self.driver.find_element(By.NAME, value=Data.Element.username).send_keys(Data.data_Input.UserNameInput)
        # time.sleep(2)
        # if Data.data_Input.UserNameInput != "Admin":
        #     print("Username Incorrect")
        # self.driver.find_element(By.NAME, value=Data.Element.password).send_keys(Data.data_Input.PasswordInput)
        # time.sleep(2)
        # if Data.data_Input.PasswordInput != "admin123":
        #     print("Password Incorrect")
        # self.driver.find_element(By.XPATH, value=Data.Element.login).click()
        # time.sleep(8)
        Search_Test_Box = self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Search).send_keys(Data.TC_PIM_01.I_menu.Search_Admin)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_01.E_menu.Admin).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.User_management).click()
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.user).click()
        time.sleep(5)

        # select Admin
        User_role=self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.user_role).click()
        time.sleep(2)
        Admin=self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.admin)
        action = ActionChains(self.driver)
        action.move_to_element(Admin).perform()
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(4)
        print(Admin.text)

        # select Enabled
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.status).click()
        time.sleep(2)
        Enabled = self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.enabled)
        action = ActionChains(self.driver)
        action.move_to_element(Enabled)
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(4)
        print(Enabled.text)

        # select ESS
        User_role = self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.user_role).click()
        time.sleep(4)
        ESS = self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.ess)
        action = ActionChains(self.driver)
        action.move_to_element(ESS).perform()
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(4)
        print(ESS.text)

        # select Disabled
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.status).click()
        time.sleep(2)
        Disabled = self.driver.find_element(By.XPATH, value=Data.TC_PIM_02.E_TC.disabled)
        action = ActionChains(self.driver)
        action.move_to_element(Disabled)
        action.key_down(Keys.DOWN).release().click().perform()
        time.sleep(4)
        print(Disabled.text)
        time.sleep(3)

        # add employee
    def TC_PIM_03(self):

        #PIM
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.pim).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.add_button).click()
        time.sleep(5)

        image_upload=self.driver.find_element(By.XPATH,value=Data.TC_PIM_03.E_AddEmply.Emply_image)
        image_upload.send_keys('C:/Users/DELL/Desktop/avatar.png')
        time.sleep(5)

        self.driver.find_element(By.NAME, value=Data.TC_PIM_03.E_AddEmply.first).send_keys(Data.TC_PIM_03.I_AddEmply.E_first_name)
        self.driver.find_element(By.NAME, value=Data.TC_PIM_03.E_AddEmply.middle).send_keys(Data.TC_PIM_03.I_AddEmply.E_middle_name)
        self.driver.find_element(By.NAME, value=Data.TC_PIM_03.E_AddEmply.last).send_keys(Data.TC_PIM_03.I_AddEmply.E_last_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.create_login_details).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.username).send_keys(Data.TC_PIM_03.I_AddEmply.E_user_name)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.status_enabled).click()
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.password).send_keys(Data.TC_PIM_03.I_AddEmply.E_password)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.confirm_password).send_keys(Data.TC_PIM_03.I_AddEmply.E_password)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.save_button).click()
        time.sleep(15)



        # Validation of Employee List
    def TC_PIM_04(self):
        # self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.pim).click()
        # time.sleep(4)
        # self.driver.find_element(By.XPATH, value=Data.TC_PIM_03.E_AddEmply.add_button).click()
        # time.sleep(8)
        actual_PD=self.driver.find_element(By.XPATH, value=Data.TC_PIM_04.E_Validation.personal_details)
        print(actual_PD.text)
        time.sleep(4)
        C_details=self.driver.find_element(By.XPATH, value=Data.TC_PIM_04.E_Validation.contact_Details).click()
        #print(C_details)
        time.sleep(4)
        Emergency_Contacts=self.driver.find_element(By.XPATH, value=Data.TC_PIM_04.E_Validation.emergency_Contacts).click()
        #print(Emergency_Contacts.text)
        time.sleep(2)
        Dependents=self.driver.find_element(By.XPATH, value=Data.TC_PIM_04.E_Validation.dependent).click()
        #print(Dependents.text)
        time.sleep(2)
        Immigration = self.driver.find_element(By.XPATH, value=Data.TC_PIM_04.E_Validation.immigration).click()
        #print(Immigration.text)
        time.sleep(5)




        # personal_details
    def TC_PIM_05(self):

        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-container']/div[@role='table']/div[2]/div[1]").click()
        # time.sleep(3)
        actual_PD = self.driver.find_element(By.XPATH, value=Data.TC_PIM_04.E_Validation.per_det).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,value=Data.TC_PIM_05.E_P_Details.Nickname).send_keys(Data.TC_PIM_05.I_P_Details.nickname)
        time.sleep(2)
        self.driver.find_element(By.XPATH,value=Data.TC_PIM_05.E_P_Details.Other_ID).send_keys(Data.TC_PIM_05.I_P_Details.other_id)
        time.sleep(2)
        self.driver.find_element(By.XPATH,value=Data.TC_PIM_05.E_P_Details.driver_license_number).send_keys(Data.TC_PIM_05.I_P_Details.driver_LN)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_05.E_P_Details.lic_expiry_date).send_keys(Data.TC_PIM_05.I_P_Details.L_Exp_date)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_05.E_P_Details.ssn).send_keys(Data.TC_PIM_05.I_P_Details.SSN)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=Data.TC_PIM_05.E_P_Details.sin_num).send_keys(Data.TC_PIM_05.I_P_Details.SIN_num)
        time.sleep(2)


        Nationlity=self.driver.find_element(By.XPATH, value=Data.TC_PIM_05.E_P_Details.nationality).click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.indian)).perform()
        time.sleep(4)

        Marital_Status = self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.Marital_Status ).click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.single)).click().perform()
        time.sleep(4)

        date_of_Birth = self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.date_of_Birth).send_keys(Data.TC_PIM_05.I_P_Details.DOB)
        time.sleep(2)
        male = self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.male).click()
        time.sleep(2)
        Military_Service = self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.military_service).send_keys(Data.TC_PIM_05.I_P_Details.Military_service)
        time.sleep(2)
        save = self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.save).click()

        Blood_Type = self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.Blood_Type).click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.Opositive)).click().perform()
        time.sleep(4)

        save1=self.driver.find_element(By.XPATH,Data.TC_PIM_05.E_P_Details.save1)
        time.sleep(10)

        # Contact_details
    def TC_PIM_06(self):

        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-container']/div[@role='table']/div[2]/div[1]").click()
        # time.sleep(3)
        C_details = self.driver.find_element(By.XPATH, value=Data.TC_PIM_06.E_Cd.Emer_con).click()
        time.sleep(4)
        Street1=self.driver.find_element(By.XPATH,Data.TC_PIM_06.E_Cd.street1).send_keys(Data.TC_PIM_06.I_CD.Street1)
        time.sleep(2)
        Street2=self.driver.find_element(By.XPATH,Data.TC_PIM_06.E_Cd.street2).send_keys(Data.TC_PIM_06.I_CD.Street2)
        time.sleep(2)
        City=self.driver.find_element(By.XPATH,Data.TC_PIM_06.E_Cd.city).send_keys(Data.TC_PIM_06.I_CD.City)
        time.sleep(2)
        State=self.driver.find_element(By.XPATH,Data.TC_PIM_06.E_Cd.state_province).send_keys(Data.TC_PIM_06.I_CD.State)
        time.sleep(2)
        ZIP=self.driver.find_element(By.XPATH,Data.TC_PIM_06.E_Cd.zip_posstalcode).send_keys(Data.TC_PIM_06.I_CD.Zip)
        time.sleep(2)

        Country=self.driver.find_element(By.XPATH,Data.TC_PIM_06.E_Cd.Country).click()
        time.sleep(2)
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_06.E_Cd.indian)).click().perform()
        time.sleep(4)

        T_HOME=self.driver.find_element(By.XPATH,Data.TC_PIM_06.E_Cd.t_home).send_keys(Data.TC_PIM_06.I_CD.T_Home)
        time.sleep(2)
        T_MOBILE = self.driver.find_element(By.XPATH, Data.TC_PIM_06.E_Cd.t_mobile).send_keys(Data.TC_PIM_06.I_CD.T_M_W)
        time.sleep(2)
        T_WORK = self.driver.find_element(By.XPATH, Data.TC_PIM_06.E_Cd.t_work).send_keys(Data.TC_PIM_06.I_CD.T_M_W)
        time.sleep(2)
        W_EMAIL = self.driver.find_element(By.XPATH, Data.TC_PIM_06.E_Cd.w_email).send_keys(Data.TC_PIM_06.I_CD.Email)
        time.sleep(2)
        OTH_EMAIL = self.driver.find_element(By.XPATH, Data.TC_PIM_06.E_Cd.other_email).send_keys(Data.TC_PIM_06.I_CD.O_Email)
        time.sleep(2)
        SAVE = self.driver.find_element(By.XPATH, Data.TC_PIM_06.E_Cd.save).click()

    # Emergency Contacts
    def TC_PIM_07(self):
        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-container']/div[@role='table']/div[2]/div[1]").click()
        # time.sleep(2)
        Emer_details = self.driver.find_element(By.XPATH, Data.TC_PIM_07.E_EmerCont.Emer_Con).click()
        time.sleep(8)
        Add_Button=self.driver.find_element(By.XPATH,Data.TC_PIM_07.E_EmerCont.add_button).click()
        name=self.driver.find_element(By.XPATH,Data.TC_PIM_07.E_EmerCont.name).send_keys(Data.TC_PIM_07.I_EmerCont.Name)
        time.sleep(2)
        relationship=self.driver.find_element(By.XPATH,Data.TC_PIM_07.E_EmerCont.Relationship).send_keys(Data.TC_PIM_07.I_EmerCont.RELATIONSHIP)
        time.sleep(2)
        HOME_Telep=self.driver.find_element(By.XPATH,Data.TC_PIM_07.E_EmerCont.H_Telep).send_keys(Data.TC_PIM_07.I_EmerCont.Home_Tempt)
        time.sleep(2)
        MOBILE=self.driver.find_element(By.XPATH,Data.TC_PIM_07.E_EmerCont.Mobil).send_keys(Data.TC_PIM_07.I_EmerCont.mobile)
        time.sleep(2)
        WORK_Telep=self.driver.find_element(By.XPATH,Data.TC_PIM_07.E_EmerCont.Work_Telep).send_keys(Data.TC_PIM_07.I_EmerCont.work_temp)
        time.sleep(2)
        SAVE=self.driver.find_element(By.XPATH,Data.TC_PIM_07.E_EmerCont.save).click()
        time.sleep(4)

        #Dependents
    def TC_PIM_08(self):
        dependents=self.driver.find_element(By.XPATH, Data.TC_PIM_08.E_dependents.Dependents).click()
        time.sleep(2)
        ADD_dependen=self.driver.find_element(By.XPATH,Data.TC_PIM_08.E_dependents.ADD_depend).click()
        time.sleep(2)
        NAME=self.driver.find_element(By.XPATH, Data.TC_PIM_08.E_dependents.name).send_keys(Data.TC_PIM_08.I_depend.Name)
        time.sleep(2)

        Relationship=self.driver.find_element(By.XPATH, Data.TC_PIM_08.E_dependents.Relationship).click()
        time.sleep(2)
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Data.TC_PIM_08.E_dependents.please_Specify)).click().perform()
        time.sleep(4)

        Please_Specify=self.driver.find_element(By.XPATH, Data.TC_PIM_08.E_dependents.please_Specify).send_keys(Data.TC_PIM_08.I_depend.Please_specify)
        time.sleep(2)
        Save=self.driver.find_element(By.XPATH,Data.TC_PIM_08.E_dependents.SAVE).click()
        time.sleep(2)


        #JOB details 1
    def TC_PIM_09(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-container']/div[@role='table']/div[2]/div[1]").click()
        time.sleep(2)
        JOB=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.job).click()
        time.sleep(8)
        Joined_Date=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.joined_Date).send_keys(Data.TC_PIM_09.E_job.Joined_Date)
        time.sleep(2)

        JOB_Title=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.job_Title).click()
        time.sleep(2)
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.job_it_manager)).click().perform()
        time.sleep(4)
        # IT_MANGER=self.driver.find_elements(By.XPATH,Data.TC_PIM_09.E_job.job_it_manager)
        # for i in IT_MANGER:
        #     if i.text == Data.TC_PIM_09.E_job.job_Title:
        #         action.move_to_element(i).click().perform()
        # time.sleep(2)

        Job_Category=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.job_category).click()
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.office_manger)).click().perform()
        time.sleep(4)


        SUB_Unit=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.sub_Unit).click()
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.engineering)).click().perform()
        time.sleep(4)


        Location=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.location).click()
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.location)).click().perform()
        time.sleep(4)


        Employment_Status=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.employment_status).click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.fulltm_cont)).click().perform()
        time.sleep(2)


        Include_E_CD=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.include_e_CD).click()
        time.sleep(2)
        Contract_StDt=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.contract_startdate).send_keys(Data.TC_PIM_09.I_job.Contract_startdate)
        time.sleep(2)
        Contract_EndDt=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.contract_enddate).send_keys(Data.TC_PIM_09.I_job.Contract_enddate)
        time.sleep(2)
        #Contract_Details=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.contract_details).click()

        SAVE=self.driver.find_element(By.XPATH,Data.TC_PIM_09.E_job.save).click()
        time.sleep(3)

        #JOB Details 2
    def TC_PIM_10(self):


        EMP_TERMINATION=self.driver.find_element(By.XPATH,Data.TC_PIM_10.E_Job_2.Emp_Termination).click()
        time.sleep(2)
        TERMINATION_DATE=self.driver.find_element(By.XPATH,Data.TC_PIM_10.E_Job_2.termination_Date).send_keys(Data.TC_PIM_10.I_Job_2.Termination_Date)
        time.sleep(4)

        TERMINATION_REASON=self.driver.find_element(By.XPATH,Data.TC_PIM_10.E_Job_2.Termination_Reason).click()
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_10.E_Job_2.resign_self_proposed)).click().perform()

        time.sleep(5)

        NOTE=self.driver.find_element(By.XPATH,Data.TC_PIM_10.E_Job_2.note).send_keys(Data.TC_PIM_10.I_Job_2.Note)
        time.sleep(4)
        SAVE=self.driver.find_element(By.XPATH,Data.TC_PIM_10.E_Job_2.save).click()
        time.sleep(10)

        #JOB Details 3
    def TC_PIM_11(self):
        Terminated_ON=self.driver.find_element(By.XPATH,Data.TC_PIM_10.E_Job_2.terminated_on).click()
        time.sleep(4)
        SAVE = self.driver.find_element(By.XPATH, Data.TC_PIM_10.E_Job_2.save).click()
        time.sleep(10)
        Activation=self.driver.find_element(By.XPATH,Data.TC_PIM_11.E_Job_3.activation).click()


        # salary_details
    def TC_PIM_12(self):
        SALARY=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.salary).click()
        time.sleep(2)
        ADD_BUTTON=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.add_button).click()
        time.sleep(2)
        SALARY_Component=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.salary_component).send_keys(Data.TC_PIM_12.I_salarydetails.Salary_component)
        time.sleep(2)

        Pay_Grade=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.pay_grade).click()
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.grade4)).click().perform()
        time.sleep(4)

        Pay_Frequency=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.pay_frequency).click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.montly)).click().perform()
        time.sleep(4)

        CURRENCY = self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.pay_frequency).click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.Indian_rupee)).click().perform()
        time.sleep(4)

        AMOUNT = self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.amount).send_keys(Data.TC_PIM_12.I_salarydetails.Amount)
        time.sleep(2)
        Comments=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.comments).send_keys(Data.TC_PIM_12.I_salarydetails.Comments)
        time.sleep(2)
        IncludeDirectDepositDetails=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.includeDDD).click()
        time.sleep(2)

        ACCOUNT_NUMBER=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.account_number).send_keys(Data.TC_PIM_12.I_salarydetails.Account_number)
        time.sleep(2)
        Account_Type=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.account_type).click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.saving)).click().perform()
        time.sleep(4)

        Routing_Number=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.routing_Number).send_keys(Data.TC_PIM_12.I_salarydetails.Routing_Number)
        time.sleep(2)
        Amount1=self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.amount1).send_keys(Data.TC_PIM_12.I_salarydetails.Amount1)
        time.sleep(2)
        SAVE=self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.saving).click()
        time.sleep(4)

        ADD_BUTTON1=self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.add_button1).click()
        time.sleep(2)
        ADD_Attachment=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.add_attachment)
        ADD_Attachment.send_keys("C:/Users/DELL/Desktop/DEMO.txt")
        time.sleep(4)
        Comment1=self.driver.find_element(By.XPATH,Data.TC_PIM_12.E_salarydetails.comment1).send_keys(Data.TC_PIM_12.E_salarydetails.comment1)
        time.sleep(2)
        SAVE1 = self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.save).click()
        time.sleep(4)

    def TC_PIM_13(self):
        Tax_Exemptions=self.driver.find_element(By.XPATH, Data.TC_PIM_12.E_salarydetails.save).click()
        time.sleep(4)
        action=ActionChains(self.driver)
        #FederalIncomeTax
        Status=self.driver.find_element(By.XPATH,Data.TC_PIM_13.E_Tax_Exemptions.status).click()
        action.move_to_element(self.driver.find_element(By.XPATH,Data.TC_PIM_13.E_Tax_Exemptions.single)).click()
        time.sleep(4)

        Exemptions=self.driver.find_element(By.XPATH,Data.TC_PIM_13.E_Tax_Exemptions.Exemptions).click()
        time.sleep(2)
        #StateIncomeTax






r=Test_PJ2()
r.login()
r.TC_PIM_01()
r.TC_PIM_02()
r.TC_PIM_03()
r.TC_PIM_04()
r.TC_PIM_05()
r.TC_PIM_06()
r.TC_PIM_07()
r.TC_PIM_08()
r.TC_PIM_09()
r.TC_PIM_10()
r.TC_PIM_11()
r.TC_PIM_12()
#r.TC_PIM_13()