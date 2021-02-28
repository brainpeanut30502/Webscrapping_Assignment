from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
username =input("enter your username : ")
password = input("enter your password : ")
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
usernameBlock = driver.find_element_by_id("username")
passwordBlock = driver.find_element_by_id("password")
usernameBlock.send_keys(username)
passwordBlock.send_keys(password)
login= driver.find_element_by_id("login")
# print(login.text)

if "enter" in login.text :
 if "first" in login.text:
     x= login.text.split(" , ")
     l= len(x[0])
     captcha= int(x[0][l-2:l].strip())
    #  print(captcha)
     
 elif "second" in login.text :
     x= login.text.split(" , ") 
     captcha =int(x[1][0:2].strip())
    #  print(captcha)
 
else:     
    if "+" in login.text :
        x=login.text.split(" + ")
        l= len(x[0])
        a=int(x[0][l-2:l].strip())
        b=int(x[1][0:2].strip())
        captcha = a+b
        # print(captcha)
    elif "-" in login.text :
        x=login.text.split(" - ")
        l= len(x[0])
        a=int(x[0][l-2:l].strip())
        b=int(x[1][0:2].strip())
        captcha = a-b
        # print(captcha)

captchaBlock = driver.find_element_by_id("valuepkg3")
captchaBlock.send_keys(Keys.BACK_SPACE)
captchaBlock.send_keys(captcha)

driver.find_element_by_id("loginbtn").click()

 
              