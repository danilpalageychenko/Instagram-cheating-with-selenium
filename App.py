from selenium import webdriver
from time import sleep


list_of_usernames = ["timatiofficial",]


options = webdriver.ChromeOptions()

options.binary_location = "C:\Program Files\Opera\46.0.2597.46\opera.exe" # path to opera executable, even though it's in PATH :/

browser = webdriver.Opera(opera_options=options)

 browser.get("https://www.instagram.com/)

        browser.add_cookie({'name' : 'csrftoken','value' : '...', 'domain': 'www.instagram.com','path' : '/'})
        browser.add_cookie({'name' : 'ds_user_id','value' : '...', 'domain': 'www.instagram.com','path' : '/'})
        browser.add_cookie({'name' : 'sessionid','value' : '...', 'domain': 'www.instagram.com','path' : '/'})
        browser.add_cookie({'name' : 'mid','value' : '...', 'domain': 'www.instagram.com','path' : '/'})
 
while(True):
    for username in list_of_usernames:

        browser.get("https://www.instagram.com/"+username+"/")



        code = """time=30;
            a=document.getElementsByClassName("_ah57t");
            function nakr() {a[0].click();}
            nakr();
            console.log("Скрипт выполнен.");"""

        a = browser.execute_script(code)
		#sleep(5)
		#a = browser.execute_script(code)
        print("Pressing button to "+username)
        sleep(30)


