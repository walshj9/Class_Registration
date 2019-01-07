from login import *

if __name__ in '__main__':
    student = Semester_Registration()
    student.get_classes()
    student.get_login_date()
    user_name = student.get_username()
    pass_word = student.get_password()
    student.login(user_name, pass_word)
    input('Press any key to close...') #pauses before closing the program
