import requests
from bs4 import BeautifulSoup


# scrapes information from NWAC all forecasts page
#The URL to scrape
URL = "https://nwac.us/avalanche-forecast/#/all/"

#the response
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')
print(soup.pretify())
