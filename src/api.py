import mechanicalsoup
import time 
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.howthemarketworks.com", verify = False)
browser.follow_link("login")

try:
    browser.select_form('form[action="/login"]')
    browser["UserName"] = "justinphan3110"
    browser["Password"] = "justinphan3110"
    response = browser.submit_selected()
except:
    browser.launch_browser()


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