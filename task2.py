from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
import time

code = input("enter the contest code: ")
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://codeforces.com/problemset")
options = webdriver.ChromeOptions()
options.headless = True
table = driver.find_element_by_tag_name("tbody")
trs = driver.find_elements_by_tag_name("tr")

for i in trs :

 if code in i.text :
     a = i.find_element_by_tag_name("a")
     qCode= a.text 
     a.click()
     driver.get_screenshot_as_file("C:\\Users\\asus\\Desktop\\Dev-Club recruitment\\Lec3-WebScraping\\screenshots\\"+qCode+".png")
     qCode =""
     driver.back()
     body = driver.find_element_by_id("pageContent")
     
 
   
time.sleep(5)
driver.quit()
