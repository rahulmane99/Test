from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
time.sleep(3)
checkb = driver.find_element (By. XPATH, "//*[@id='navMenus']/li[2]/a").click()
time.sleep(2)
print(driver.title)
driver.find_element(By.XPATH,"//input[@id='c_bs_1']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='bs_1']/span[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='c_bf_2']").click()
time.sleep(2)
driver.quit()