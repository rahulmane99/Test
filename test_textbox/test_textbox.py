from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
time.sleep(3)
title=driver.title
print(title)
fullname= driver.find_element(By.ID,"fullname")
fullname.send_keys("Rahul")
time.sleep(2)
email=driver.find_element(By.ID,"email")
email.send_keys("test@testing.com")
time.sleep(2)
add=driver.find_element(By.ID,"address")
add.send_keys("Satara")
city=add.get_attribute('value')
print(city)
time.sleep(2)
passw = driver.find_element(By.ID,"password")
passw.send_keys("Satara")
time.sleep(2)
submmit=driver.find_element(By. XPATH, "//input[@type='submit']").click()
time.sleep(2)
print("Submitted successfully")

driver.quit()