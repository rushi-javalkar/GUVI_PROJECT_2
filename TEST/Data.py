#Class for Selenium Selectors
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By



class login:
    class E_login:
        username = "username"
        password = "password"
        login1 = "//button[@type='submit']"

    class I_login:
        UserNameInput = "Admin"  # str(input("Enter Username (Admin): "))
        PasswordInput = "admin123"  # str(input("Enter Password (admin123): "))


class TC_PIM_01:
    class E_menu:

        Search = "//input[@placeholder='Search']"
        Admin = "//span[normalize-space()='Admin']"
        Act_Admin = "//aside[@class='oxd-sidepanel']//li[1]"
        PIM = "//span[normalize-space()='PIM']"
        Act_pim = "//aside[@class='oxd-sidepanel']//li[2]"
        Leave = "//span[normalize-space()='Leave']"
        Act_leave = "//aside[@class='oxd-sidepanel']//li[3]"
        Time = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']"
        Act_time = "//aside[@class='oxd-sidepanel']//li[4]"
        Recruitment = "//span[normalize-space()='Recruitment']"

        My_Info = "//span[normalize-space()='My Info']"
        Performance = "//span[normalize-space()='Performance']"
        Dashboard = "//span[normalize-space()='Dashboard']"
        Directory = "//span[normalize-space()='Directory']"
        Maintenance = "//span[normalize-space()='Maintenance']"
        Buzz = "//span[normalize-space()='Buzz']"
        confirm='//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]'

    class I_menu:
        Search_Admin = "admin"
        Search_Pim = "PIM"
        Search_Leave = "Leave"
        Search_Time = "Time"
        Search_Recruitment = "Recruitment"
        Search_My_Info = "My info"
        Search_Performance = "Performance"
        Search_Dashboard = "Dashboard"
        Search_Directory = "Directory"
        Search_Maintenance = "Maintenance"
        Search_Buzz = "Buzz"

class TC_PIM_02:
    class E_TC:
        User_management = "//span[normalize-space()='User Management']"
        user = "//a[@role='menuitem']"
        user_role="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
        admin ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
        ess = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
        status = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]"
        enabled = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
        disabled='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'

class TC_PIM_03:
    class E_AddEmply:
        pim="//span[normalize-space()='PIM']"
        add_button="//button[normalize-space()='Add']"

        Emply_image='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button'

        first="firstName"
        middle="middleName"
        last="lastName"

        create_login_details="//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
        username='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        password="//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
        confirm_password="//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
        status_enabled="//label[normalize-space()='Enabled']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']"
        upload_file="//button[@class='oxd-icon-button employee-image-action']"
        save_button="//button[@type='submit']"


    class I_AddEmply:
        E_first_name="xyz123"
        E_middle_name="A"
        E_last_name="xyz987"
        E_user_name= "xyzqwerty"
        E_password= "Guvi@123"

class TC_PIM_04:
    class E_Validation:
        personal_details = "//div[@role='tablist']"
        per_det='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
        contact_Details = "//a[normalize-space()='Contact Details']"
        emergency_Contacts = "//a[normalize-space()='Emergency Contacts']"
        dependent = "//a[normalize-space()='Dependents']"
        immigration = "//a[normalize-space()='Immigration']"

class TC_PIM_05:
    class E_P_Details:
        Nickname='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
        Other_ID='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
        driver_license_number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        lic_expiry_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        ssn='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
        sin_num='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'

        nationality='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
        indian='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]/span'

        Marital_Status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
        single='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span'

        date_of_Birth="//div//div//div//div//div//div//div//div//div//div//div//div[3]//div[2]//input[1]"
        male="//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']"
        military_service='//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]'
        save="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']"
        Blood_Type='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
        Opositive='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]'
        save1="//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"

    class I_P_Details:
        nickname="chintu"
        other_id="9483633"
        driver_LN="9483633550"
        L_Exp_date="2000-02-12"
        SSN="1234567891"
        SIN_num="9876543210"
        Nationality="Indian"
        DOB="2000-10-22"
        Military_service="NO"

class TC_PIM_06:
    class E_Cd:
        Emer_con=TC_PIM_04.E_Validation.contact_Details
        street1='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
        street2='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
        city='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
        state_province='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'

        zip_posstalcode='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'

        Country='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
        indian='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'

        t_home='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
        t_mobile='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
        t_work='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
        w_email='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
        other_email='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
        save='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'

    class I_CD:
        Street1 ='Bc No-163 bewoor road'
        Street2 ='Camp belgaum'
        City='Belgaum'
        State='karnataka'
        Zip="590001"
        T_Home='2425490'
        T_M_W='8147001104'
        Email="rishiaj@gmai.com"
        O_Email='rajaj@gmail.com'

class TC_PIM_07:
    class E_EmerCont:
        Emer_Con=TC_PIM_04.E_Validation.emergency_Contacts
        add_button="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/div[@class='orangehrm-action-header']/button[1]"
        name='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
        Relationship='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
        H_Telep='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
        Mobil='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
        Work_Telep='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
        save='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    class I_EmerCont:
        Name='sunny'
        RELATIONSHIP='brother'
        Home_Tempt=TC_PIM_06.I_CD.T_Home
        mobile=TC_PIM_06.I_CD.T_M_W
        work_temp=TC_PIM_06.I_CD.T_M_W

class TC_PIM_08:
    class E_dependents:
        Dependents=TC_PIM_04.E_Validation.dependent
        ADD_depend='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
        name='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'

        Relationship='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
        other='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/span'

        please_Specify='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
        SAVE='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    class I_depend:
        Name='Tejas'
        Please_specify='Son'
        DOB='2011-08-18'


#     class E_Immigration:
#         Immigra=TC_PIM_04.Elements.immigration
#         add_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
#         visa='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/div/label/span'
#         number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
#         issued_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input'
#         expiry_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/div/div/input'
#         eligible_status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/input'
#         issued_by='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]'
#
#         china='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]'
#
#         eligible_review_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[6]/div/div[2]/div/div/input'
#         comments = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[7]/div/div[2]/textarea'
#         save='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
#

class TC_PIM_09:
    class E_job:
        job='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
        joined_Date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'

        job_Title='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
        job_it_manager='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[14]/span'

        #job_specification=''

        job_category='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
        office_manger='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[5]/span'

        sub_Unit='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]'
        engineering='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[2]/div[3]/span'

        location='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
        texas_RD='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[5]/span'

        employment_status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]'
        fulltm_cont='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[3]/span'

        include_e_CD='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span'
        contract_startdate='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input'
        contract_enddate='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input'

        contract_details='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div/div/div/div[2]/div/div[1]'

        save='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

    class I_job:
        Joined_Date='2015-01-01'
        Contract_startdate='2018-02-12'
        Contract_enddate='2020-01-30'


class TC_PIM_10:
    class E_Job_2:
        job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
        Emp_Termination='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
        termination_Date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'

        Termination_Reason='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div'
        Termination_Reason_list ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div[2]'
        resign_self_proposed='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div[2]/div[10]/span'


        note='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]'
        save='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'


    class I_Job_2:
        Termination_Date='2020-05-30'
        Note='Accept and Do my needful as Earliest'

class TC_PIM_11:
    class E_Job_3:
        terminated_on = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/p'
        activation='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'



class TC_PIM_12:
    class E_salarydetails:
        salary="//a[@class='orangehrm-tabs-item --active']"
        add_button="//div[@class='orangehrm-attachment']//button[@type='button'][normalize-space()='Add']"
        salary_component="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
        pay_grade='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
        grade4='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[5]/span'

        pay_frequency='//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]'
        montly='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]/span'

        currency='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
        Indian_rupee='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[63]/span'

        amount='//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[5]/div[1]/div[2]/input[1]'
        comments='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/textarea'
        includeDDD='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
        account_number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
        account_type='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[1]'
        saving='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span'

        routing_Number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
        amount1='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'
        add_button1='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'
        save='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'
        add_attachment= "//div[@class='oxd-file-button']"
        comment1='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[6]/div/form/div[2]/div/div/div/div[2]/textarea'


    class I_salarydetails:
        Salary_component='CTC'
        Amount='30000'
        Comments='netsalary,Gross salary,Basic salary,Bons'
        Account_number='987654321123456789'
        Routing_Number='07654321'
        Amount1='1000'
        Comment1='Successfully Done'

class TC_PIM_13:
    class E_Tax_Exemptions:
        Tax_Exemp='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a'
        status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
        single='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span'
        Exemptions='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'


    class I_Tax_Exemptions:
        Exemptions='20'






   # class Searchnew:
#
#     Search_Pim = "PIM"
#     Search = "//input[@placeholder='Search'] "
#     #Admin = "//span[normalize-space()='Admin']"
#     PIM = "//span[normalize-space()='PIM']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def sendpim(self,PIM,Search,Search_Pim):
#         self.driver.find_element(By.XPATH, value=Search).send_keys(Search_Pim)
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, value=PIM).click()
#         time.sleep(5)
#
# @pytest.fixture()
# def pytest_configure(config):
#     config._metadata['Project Name']= 'nop Commerce'
#     config._metadata['Module Name']= 'Customers'
#     config._metadata['Tester']= 'Avdhut'
