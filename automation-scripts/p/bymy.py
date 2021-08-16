from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=r'C:\Users\12064\Documents\Login\chromedriver.exe', chrome_options=options)
driver.get("https://www.drive.google.com")
driver.implicitly_wait(5)
driver.get("https://drive.google.com/drive/u/0/my-drive")



print(driver.current_url)

driver.quit()

import youtube_dl

