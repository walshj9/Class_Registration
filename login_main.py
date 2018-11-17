from login import *

if __name__ in '__main__':
    student = Semester_Registration()
    student.get_classes()
    username = student.get_username()
    password = student.get_password()
    student.login(username, password)
    input("Press enter when ready.")
