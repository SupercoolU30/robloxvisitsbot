import random
import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
random.seed(time.localtime)

path = 'D:\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=selenium")
#chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.get("https://web.roblox.com/games/6051947035")
assert "Roblox" in driver.title

play_button = driver.find_element_by_id("MultiplayerVisitButton")
play_button.click()

time.sleep(10)
os.system("TASKKILL /F /IM RobloxPlayerBeta.exe")