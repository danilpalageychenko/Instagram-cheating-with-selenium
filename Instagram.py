from selenium import webdriver
from time import sleep


#list_of_usernames = ["timatiofficial","urgantcom","buzova86","borodylia","samburskaya","ververa","instagram","pavelvolyaofficial","selenagomez","taylorswift","arianagrande","beyonce","kimkardashian","justinbieber","cristiano",
#"kyliejenner","kendalljenner","nickiminaj","therock","nike","natgeo","neymarjr","leomessi","khloekardashian","katyperry","mileycyrus","jlo",
#"ddlovato","kourtneykardash","victoriassecret","badgalriri","kevinhart4real"]
list_of_usernames = ["timatiofficial","urgantcom","buzova86","borodylia","samburskaya","ververa","instagram","pavelvolyaofficial","selenagomez","taylorswift"]



options = webdriver.ChromeOptions()

options.binary_location = "C:\Program Files\Opera\launcher.exe" # path to opera executable, even though it's in PATH :/
#options.binary_location = "C:\Program Files\Opera\operadriver.exe" # path to opera executable, even though it's in PATH :/

browser = webdriver.Opera(opera_options=options,executable_path="C:\Program Files\Opera\operadriver.exe")

browser.get("https://www.instagram.com/")

browser.add_cookie({'name' : 'csrftoken','value' : '...', 'domain': 'www.instagram.com','path' : '/'})
browser.add_cookie({'name' : 'ds_user_id','value' : '...', 'domain': 'www.instagram.com','path' : '/'})
browser.add_cookie({'name' : 'sessionid','value' : '...', 'domain': 'www.instagram.com','path' : '/'})
browser.add_cookie({'name' : 'mid','value' : '...', 'domain': 'www.instagram.com','path' : '/'})
 
while(True):
    i=0
    for username in list_of_usernames:
        i+=1
        browser.get("https://www.instagram.com/"+list_of_usernames[i]+"/")
        




        code = """
            time=30;
            a=document.getElementsByClassName("_ah57t");
            function nakr() {a[0].click();}
            nakr();
            console.log("Script runned.");
            """
        a = browser.execute_script(code)
        print("Pressing button to "+username)
        #sleep(2)
        #element = browser.find_element_by_class_name('_ah57t')
        #if element.get_attribute("Class") == "_ah57t _84y62 _frcv2 _rmr7s":
        #    a = browser.execute_script(code)
        sleep(30)


