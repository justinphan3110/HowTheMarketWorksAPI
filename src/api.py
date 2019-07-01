import mechanicalsoup
import time 
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class API: 
    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.open("https://www.howthemarketworks.com", verify = False)
        self.userLogin = False;


    def login(self, usename, password):
        try:
            self.browser.follow_link("login")
            self.browser.select_form('form[action="/login"]')
            self.browser["UserName"] = usename
            self.browser["Password"] = password
            response = self.browser.submit_selected()
            self.userLogin = True;
        except mechanicalsoup.LinkNotFoundError:
            self.userLogin = False; 

    def trade(self, companyName, ammount):
        if(self.userLogin){
            self.browser.open("https://www.howthemarketworks.com")
            self.browser.follow_link("/")
            self.browser.launch_browser()
        }
       

test = API()
test.login("justinphan3110", "justinphan3110")
test.trade("g",1)

# browser.follow_link("https://www.howthemarketworks.com/trading/equities")




# print(response.text)
# browser.launch_browser()

# browser.get_current_form()





# browser.follow_link("login")
# browser.select_form('#login form')

# mainPage = browser.get_current_page



# message = browser.get_current_page().find("a", class_ ="account-links")
# browser["login"] = "justinphan3110@gmail.com"
# browser["password"] = "justinphan3110"
# reso = browser.submit_selected()






# page = browser.get_current_page()
# messages = page.find("h2", class_="shelf-title")
# if messages:
#     print(messages.text)
# assert page.select(".logout-form")
# print(page.title.text)