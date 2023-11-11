from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from text_converter import  newlis

import time
from urllib.parse import quote
import os
import csv

#setting options for startup
options = Options()
options.add_argument('--profile-directory=Default')
options.add_argument("--user-data-dir=C:path/to/profile")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"

#starting a chromedriver instance
service=Service('path/to/chrome')
driver = uc.Chrome(executable_path = 'path/to/chrome.exe', options=options)

driver.get('https://web.whatsapp.com')


#reading numbers off of sample csv file
rows = []
numbers = []
with open("./Groups.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)
  #checking if a message has been sent to the listed contact or not.
  for row in csvreader:
    if row[1] != '':
       continue
    #if message not sent, load the number and mark as sent in the csv file.
    else:
       row[1] = 'True'
       numbers.append(row[0])

print(numbers)

#Sending messages to the numbers
for i in numbers:
    click_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')))
    click_btn.click()
    click_btn.send_keys(f"{i}")
    click_btn.send_keys(Keys.ENTER)  
    message_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))

    #importing the message from a seperate python file.
    for i in newlis:
        message_field.send_keys(i)
        message_field.send_keys(Keys.SHIFT+Keys.ENTER)
    



time.sleep(20)
