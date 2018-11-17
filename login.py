import getpass
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
class Semester_Registration:    
    #from selenium.webdriver.common.keys import Keys
    #from selenium.webdriver.chrome.options import Options
    #from selenium.webdriver.common.action_chains import ActionChains
    #import datetime
    #import time

    chrome_executable_path = "/usr/bin/chromedriver"
    

    def get_classes(self):
        CRNs = [] #Array of Course Registration Numbers
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
        print("What's the month and date of registration?")
        month = int(input("Month (1-12): "))
        date = int(input("Date: "))

    def get_username(self):
        username = input('Enter your username: ')
        return username

    def login(self, username, password):
        login_url = 'https://login.rowan.edu/cas/login?TARGET=https%3A%2F%2Fbanner9.rowan.edu%2FStudentRegistrationSsb%2Fj_spring_cas_security_check'
        options=webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.binary_location = '/usr/bin/google-chrome'
        print("Opening Browser...")
        browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)
        browser.get(login_url)
        print("Logging in...")
        browser.find_element_by_name('username').send_keys(username)
        browser.find_element_by_name('password').send_keys(password, Keys.RETURN)
