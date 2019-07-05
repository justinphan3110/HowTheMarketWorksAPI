import mechanicalsoup
import time 
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class API: 
    def __init__(self, useName, passWord):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.open("https://www.howthemarketworks.com", verify = False)
        self.userLogin = False;
        self.useName = useName
        self.passWord = passWord


    def login(self):
        while(not self.userLogin):  
            try:
                self.browser.open("https://www.howthemarketworks.com/login")
                self.browser.select_form('form[action="/login"]')
                # self.browser.get_current_form().print_summary()
                self.browser["UserName"] = self.useName
                self.browser["Password"] = self.passWord
                response = self.browser.submit_selected()
                self.userLogin = True;
            except mechanicalsoup.LinkNotFoundError:
                print("log in failed")
                self.userLogin = False; 

    def marketStatus(self):
        if(self.userLogin):
            self.browser.open("https://www.howthemarketworks.com/trading/equities")
            status = self.browser.get_current_page().find("p", class_="text-center" )
            if(str(status.text) == "This contest has not started yet"):
                print("Market is openning")
            else: 
                status = str(status.text).split('\n')[1].replace("...", "")
                print(status)
        else: 
            print("you need to log in first")



    def trade(self, companyName, ammount):
        if(self.userLogin):
            self.browser.open("https://www.howthemarketworks.com/trading/equities")
            self.browser.select_form('form[action="/trading/placeorder"]')
            self.browser["OrderSide"] = 1
            self.browser["OrderType"] = 1
            self.browser["Symbol"] = companyName
            self.browser["Quantity"] = ammount
            self.browser.submit_selected()
        else:
            print("you need to log in first")
       

    def tradeWithLimit(self, companyName, amount):
        if(self.userLogin):
            self.browser.open("https://www.howthemarketworks.com/trading/equities")
            self.browser.select_form('form[action="/trading/placeorder"]')
            self.browser["OrderSide"] = 1
            self.browser["OrderType"] = 2
            self.browser["Symbol"] = companyName
            self.browser["Price"] = amount
            # self.browser.get_current_form().print_summary()
            # self.browser.launch_browser()
            self.browser.submit_selected()
        else:
            print("you need to log in first")
       

test = API("justinphan3110", "justinphan3110")
test.login()
test.marketStatus()
test.trade("AMD", 200)

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