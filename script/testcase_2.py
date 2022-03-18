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
#chromedriver_path = "//Users/user/Documents/Automation/chromedriver"

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")

driver.maximize_window()
driver.get("https://www.phptravels.net/login")

# Testcase name: Login test (abnormal)

try: 
  # Step 1. Input email address:
  action1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys("user@phptravels.com")
  driver.implicitly_wait(10)
  driver.close()

except Exception as e: print(e)
#End of file
