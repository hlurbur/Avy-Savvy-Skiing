import requests
from bs4 import BeautifulSoup
from selenium import webdriver



# path in the computer for the web driver
webdriver_path = ('/Users/hadassahlurbur/Desktop/Avvy-Savvy-Skiing/chromedriver')

# make the driver
driver = webdriver.Chrome(webdriver_path)

# # get the response
# r = driver.get('https://nwac.us/avalanche-forecast/#/olympics')

# # make the soup
# soup = BeautifulSoup(driver.page_source, 'html.parser')

#Scrapes the avalanche forecast from a NWAC URL for a particular region's URL forecast page
#Returns a list of the dangers at each elevation level.
def scrapeForecast(url):
    """
    Scrapes data from the NWAC page of a given forecasted region in the North Cascades

    Args:
    url: url string to scrape

    Returns:
    dangersList: a list of the dagers from the forecasted elevation bands: AboveTreeline, nearTreeline, and belowTreeline
    in that order. 

    """
    
    r = driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    dangers = soup.find(class_  = 'nac-contentPanel').findAll(class_ = 'nac-dangerLabel') #this is a list of HTML objects
    
    aboveTreeline = dangers[0].text
    nearTreeline = dangers[1].text
    belowTreeline = dangers[2].text
    
    dangersList = [aboveTreeline, nearTreeline, belowTreeline]

    return dangersList

def scrapeOlympics():
    """
    Scrapes and returns the avalanche forecast for the olympics region
    """
    olympics = "https://nwac.us/avalanche-forecast/#/olympics"
    return scrapeForecast(olympics)
    
def scrapeWestSlopesNorth():
    westSlopesNorth = "https://nwac.us/avalanche-forecast/#/west-slopes-north"
    return scrapeForecast(westSlopesNorth)

def scrapeWestSlopesCentral():
    westSlopesCentral = "https://nwac.us/avalanche-forecast/#/west-slopes-central"
    return scrapeForecast(westSlopesCentral)

def scrapeWestSlopesSouth():
    westSlopesSouth = "https://nwac.us/avalanche-forecast/#/west-slopes-south"
    return scrapeForecast(westSlopesSouth)

def scrapeStevensPass():
    stevensPass = "https://nwac.us/avalanche-forecast/#/stevens-pass"
    return scrapeForecast(stevensPass)

def scrapeSnoqualmiePass():
    snoqualmiePass = "https://nwac.us/avalanche-forecast/#/snoqualmie-pass"
    return scrapeForecast(snoqualmiePass)

def scrapeEastSlopesCentral():
    eastSlopesCentral = "https://nwac.us/avalanche-forecast/#/east-slopes-central"
    return scrapeForecast(eastSlopesCentral)

def scrapeEastSlopesSouth():
    eastSlopesSouth = "https://nwac.us/avalanche-forecast/#/east-slopes-south"
    return scrapeForecast(eastSlopesSouth)

def scrapeEastSlopesNorth():
    eastSlopesNorth = "https://nwac.us/avalanche-forecast/#/east-slopes-north"
    return scrapeForecast(eastSlopesNorth)

def scrapeMtHood():
    mountHood = "https://nwac.us/avalanche-forecast/#/mt-hood"
    return scrapeForecast(mountHood)

scrapeMtHood()
# # # scrapes information from NWAC all forecasts page
# # #The URL to scrape
# # URL = "https://nwac.us/avalanche-forecast/#/olympics"

# # #the response
# # r = requests.get(URL)

# # #parse the HTML
# # soup = BeautifulSoup(r.content,'html5lib')
# # #soup = BeautifulSoup(r.text, 'html.parser')

# # #print the pretty version of the data

# # found one
# # print(soup.find(class_  = 'nac-contentPanel').find(class_ = 'nac-danger').find(class_ = 'nac-dangerLabel'))
# # print(soup.findAll(class_ = 'nac-dangerLabel'))

# dangers = soup.find(class_  = 'nac-contentPanel').findAll(class_ = 'nac-dangerLabel') #this is a list of HTML objects
# Above = dangers[0].text
# Near = dangers[1].text
# Below = dangers[2].text
# print("poop")

# # make a list of the URls, make a function that returns infor the URL


# #print(soup.find(class_  = 'nac-contentPanel').find_all(class_ = 'nac-danger').find_all(class_ = 'nac-dangerLabel'))
# #print(danger_text)
# #print(soup)


