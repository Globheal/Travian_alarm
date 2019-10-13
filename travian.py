from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from playsound import playsound
import pandas as pd
import threading as td

driver = webdriver.Chrome(executable_path=r'\chromedriver_win32\chromedriver.exe')

driver.get("https://ts1.travian.pl/dorf1.php?newdid=79&") #link to village

username = driver.find_element_by_name("name")
password = driver.find_element_by_name("password")

username.send_keys("MyLogin") #login
password.send_keys("MyPassword") #pass

driver.find_element_by_name("s1").click()

def checkAttack():
    td.Timer(60.0, checkAttack).start()
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    span = soup.find("span", {"class" : "a1"})
    print(span.text)
    attack = span.text

    if "Atak" or "Attack" in attack:
        playsound('audio.mp3')

checkAttack()
