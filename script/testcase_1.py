# Design by Nguyen Quoc Dung
# Copyright ZenS Company 2021-2022

import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")

driver.maximize_window()
driver.get("https://www.w3schools.com/bootstrap/bootstrap_dropdowns.asp")

# Testcase name: Login test with student (abnormal)

try:
    sel = driver.find_element(
        By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[3]/button").clic
    print(sel)
    time.sleep(5)
    # driver.close()

except Exception as e:
    print(e)
# End of file
