import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

executable_path = "/webdrivers"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('kkelicaakdanhinjdeammmilcgefonfh.crx')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get()
## open browser without going to a URL yet

driver.set_window_rect(width=100, height=200)
driver.set_window_position(-200, -200)
