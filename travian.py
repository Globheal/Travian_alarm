from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from playsound import playsound
import pandas as pd
import threading as td

driver = webdriver.Chrome(executable_path=r'H:\Projekty\Travian_Alarm\chromedriver_win32\chromedriver.exe')

attacks=[] #List to store attacks

driver.get("https://ts1.travian.pl/dorf1.php?newdid=79&") #link do sprawdzanej wioski

username = driver.find_element_by_name("name")
password = driver.find_element_by_name("password")

username.send_keys("") #login
password.send_keys("") #pass

driver.find_element_by_name("s1").click()

def checkAttack():
    td.Timer(60.0, checkAttack).start()
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    span = soup.find("span", {"class" : "a1"})
    print(span.text)
    atak = span.text

    if "Atak" in atak:
        print("atak jest")
        playsound('audio.mp3')
    else:
        print("Nie ma ataku")

checkAttack()
