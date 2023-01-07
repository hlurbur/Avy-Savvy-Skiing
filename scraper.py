import requests
from bs4 import BeautifulSoup
from selenium import webdriver


webdriver_path = ('/Users/hadassahlurbur/Desktop/Avvy-Savvy-Skiing/chromedriver')

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
# print(soup.find(class_  = 'nac-contentPanel').find(class_ = 'nac-danger').find(class_ = 'nac-dangerLabel'))
# print(soup.findAll(class_ = 'nac-dangerLabel'))

dangers = soup.find(class_  = 'nac-contentPanel').findAll(class_ = 'nac-dangerLabel') #this is a list of HTML objects
Above = dangers[0].text
Near = dangers[1].text
Below = dangers[2].text
print("poop")

# make a list of the URls, make a function that returns infor the URL


#print(soup.find(class_  = 'nac-contentPanel').find_all(class_ = 'nac-danger').find_all(class_ = 'nac-dangerLabel'))
#print(danger_text)
#print(soup)
