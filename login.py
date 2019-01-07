import getpass
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

CRNs = []
class Semester_Registration:    
    
    chrome_executable_path = "/usr/bin/chromedriver"
    
    #CRNs = [] #Array of course numbers
    def get_classes(self):
        print("Enter the Course Registration Numbers, and -1 when finished")
        CRN = 0 #Initialize at arbitrary value
        while True:
           CRN = int(input("Class Number: "))
           if CRN == -1: 
               break
           else:
               CRNs.append(CRN)
        for CRN in CRNs:
           print(CRN)
 
    #while datetime.datetime.now() < target_time: #waits for desired time
    #   time.sleep(0.25)
    

    def get_password(self):
        while True:
            password1 = getpass.getpass("Password: ")
            password2 = getpass.getpass("Please re-enter the password: ")
            if password1 == password2:
                print("Thank you")
                break
            else:
    	        print("Passwords didn't match, please try again")
        return password1

    def get_login_date(self):
        print("What's the date of registration?")
        date = input("Date(MM/DD): ")
        day, month = date.split("/", 1)
        return (day, month)


    def get_username(self):
        username = input('Enter your username: ')
        return username

    def login(self, a, b):
        login_url = 'https://login.rowan.edu/cas/login?TARGET=https%3A%2F%2Fbanner9.rowan.edu%2FStudentRegistrationSsb%2Fj_spring_cas_security_check'
        options=webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.binary_location = '/usr/bin/google-chrome'
        print("Opening Browser...")
        browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)
        browser.get(login_url)
        print("Logging in...")
        browser.find_element_by_name('username').send_keys(a)
        browser.find_element_by_name('password').send_keys(b, Keys.RETURN)
        wait = WebDriverWait(browser, 10) #sets wait time for 10 seconds
        wait.until(EC.element_to_be_clickable((By.ID, 'registerLink'))) #waits for link to become visible
        browser.find_element_by_xpath("//a[@id='registerLink']").click()
        
