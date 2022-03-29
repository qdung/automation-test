# Design by Nguyen Quoc Dung
# Copyright ZenS Company 2021-2022

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")

driver.maximize_window()
driver.get("https://www.phptravels.net/login")

# Testcase name: Login test (abnormal 3)

try: 
  # Step 1. Input email address (2):
  action1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input (2)").send_keys("user@phptravels.com (2)")
  driver.implicitly_wait(10)
  # Step 2. Input email password (2):
  action2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys("demouser")
  driver.implicitly_wait(10)
  # Step 3. Press button Sign In (2):
  action3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/button").click()
  driver.implicitly_wait(10)
  # Step 4. Check title after sign in (2):
  action4 = print(driver.find_element(By.XPATH, "/html/body/section[1]/div/div[1]/div/div[1]/div[1]/div/div/h2").get_attribute("textContent"))
  driver.implicitly_wait(10)
  # Step 5. Check title after sign in (3):
  action5 = print(driver.find_element(By.XPATH, "abacasd").get_attribute("textContent"))
  driver.implicitly_wait(10)
  driver.close()

except Exception as e: print(e)
#End of file
