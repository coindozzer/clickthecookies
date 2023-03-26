#Imports

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime,timedelta

#game URL
URL = "http://orteil.dashnet.org/experiments/cookie/"

#init driver
driver = webdriver.Firefox()
driver.get(URL)

#send endless loop
game_on = True

#find cookie element
cookie = driver.find_element(By.ID, "cookie")

#setup time div
seconds = timedelta(seconds=5)
time_stemp = datetime.now() + seconds

#get store items and slice it down
store = driver.find_element(By.ID,"store").text.split("\n")
store_items = [item.split() for item in store[::2]]


#run the game while forever
while True:
    #click the cookie while not chosing
    cookie.click()
    #if game run for 5sec check money and buy moste valubel item
    if time_stemp <= datetime.now():
         print("yes")
         time_stemp = datetime.now() + seconds
         money = driver.find_element(By.ID,"money")
         for item in store_items[::-1]:
             if int(money.text) >= int(item[len(item)-1].replace(",","")):
                 if item[0] == "Alchemy" or item[0] == "Time":
                     driver.find_element(By.ID, f"buy{item[0]} {item[1]}").click()
                 else:
                     driver.find_element(By.ID, f"buy{item[0]}").click()