from selenium import webdriver
import time

from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
time.sleep(3)
checkb = driver.find_element (By. XPATH, "//*[@id='navMenus']/li[3]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='igottwo']").click()
time.sleep(2)
#msg= driver.("//div[@id='check']")
msg=driver.find_element(By. XPATH,"//div[@id='check']" )
text=msg.text
print(text)
time.sleep(2)
print(driver.title)
driver.quit()