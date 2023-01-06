import requests
from bs4 import BeautifulSoup


# scrapes information from NWAC all forecasts page
#The URL to scrape
URL = "https://nwac.us/avalanche-forecast/#/all/"

#the response
r = requests.get(URL)

#parse the HTML
#soup = BeautifulSoup(r.content,'html5lib')
soup = BeautifulSoup(r.text, 'html.parser')

#print the pretty version of the data
print(soup.prettify())
