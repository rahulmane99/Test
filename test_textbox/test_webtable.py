from selenium import webdriver
import time

from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
time.sleep(3)
checkb = driver.find_element (By. XPATH, "//*[@id='navMenus']/li[4]/a").click()
driver.save_screenshot("webtable.png")
print("screenshot captured")
time.sleep(2)
