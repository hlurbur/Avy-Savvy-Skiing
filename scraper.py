import requests
from bs4 import BeautifulSoup
from selenium import webdriver


webdriver_path = ('/Users/mlurbur/Documents/chromedriver')

driver = webdriver.Chrome(webdriver_path)

# the response
r = driver.get('https://nwac.us/avalanche-forecast/#/olympics')

soup = BeautifulSoup(driver.page_source, 'html.parser')


#dangers = driver.find_elements_by_xpath('//td[@class="name"]')
# # scrapes information from NWAC all forecasts page
# #The URL to scrape
# URL = "https://nwac.us/avalanche-forecast/#/olympics"

# #the response
# r = requests.get(URL)

# #parse the HTML
# soup = BeautifulSoup(r.content,'html5lib')
# #soup = BeautifulSoup(r.text, 'html.parser')

# #print the pretty version of the data

# found one
danger_text = soup.find(class_  = 'nac-contentPanel').find(class_ = 'nac-danger').find(class_ = 'nac-dangerLabel').text
print(danger_text)
# print(soup.prettify())
