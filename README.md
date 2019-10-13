# Travian alarm.

# Not confirmed if legal! Use on Your own responsibility!

## About project.
Travian alarm uses Python scraping with libraries like: Selenium, BeautifulSoup, pandas etc. Main goal of this alarm is to check if there is an attack comming on certain village, and play sound.


## How to install.
First we need to install Python with libraries:

### Install Python:
You need to install Python. To do it, You need to download installer vaild for Your OS, from site: 
```
https://www.python.org/
```

### Install Selenium
To install selenium You can use CMD and execute command:
```
pip install Selenium
```

### Install BeautifulSoup
To install BeautifulSoup You can use CMD and execute command:
```
pip install beautifulsoup4
```
or
```
pip install beautifulsoup
```
### Install Playsound
To install Playsound You can use CMD and execute command:
```
pip install Playsound
```
## Remember to run CMD as admin.

## Configuration:
In travian.py there are three fields that needs to be filled:
### Link to game:
```
driver.get("https://ts1.travian.pl/dorf1.php?newdid=79&")
```
between quotation marks write Your link from village You want to check.
### Username:
```
username.send_keys("MyUserName")
```
between quotation marks write Your login to the game.
### Password:
```
password.send_keys("MyPassword")
```
between quotation marks write Your password to the game.
