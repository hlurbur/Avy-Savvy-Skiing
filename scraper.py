""" The web scraper utilizes the BeautifulSoup library to scrape the avalanche forecast
from the Northwest Avalanche Center website for a given region in the Cascades. 
The Avalanche forecast is made up of three forecasted danger levels: below treeline, near treeline and above treeline.
Each danger level ranges from low (1) to extreme (5). The scraper returns a list of three forecasts, one
for each treeline level for a specified region.
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


# path in the computer for the web driver
webdriver_path = ('/Users/hadassahlurbur/Desktop/Avvy-Savvy-Skiing/chromedriver')

# make the driver
driver = webdriver.Chrome(webdriver_path)



def scrapeForecast(url):
    """
    Scrapes data from the NWAC page of a given forecasted region in the North Cascades

    Args:
    url: url string of an NWAC page for a specific region of the cascades to scrape 

    Returns:
    dangersList: a list of the danger levels from the forecasted elevation bands: aboveTreeline, nearTreeline, and belowTreeline
    in that order. 

    """
    
    #Load the url, use sleep to ensure that page and scraped content loads completely
    #before getting content from the soup.
    r = driver.get(url)
    sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sleep(1)
    #Use class names from page inspection to extract desired information
    dangers = soup.find(class_  = 'nac-contentPanel').findAll(class_ = 'nac-dangerLabel') #this is a list of HTML objects
    
    #Get the desired text from the HTML objects
    aboveTreeline = dangers[0].text
    nearTreeline = dangers[1].text
    belowTreeline = dangers[2].text
    
    dangersList = [aboveTreeline, nearTreeline, belowTreeline]
    
    #return a list of the three forecasted danger levels ranging from low to extreme
    return dangersList

"""
Each Scraper method returns the avalanche forecast for the region name specified in the definition as well
as a link to the NWAC forecast page for the region
"""
def scrapeOlympics():
    olympics = "https://nwac.us/avalanche-forecast/#/olympics"
    return scrapeForecast(olympics), olympics
    
def scrapeWestSlopesNorth():
    westSlopesNorth = "https://nwac.us/avalanche-forecast/#/west-slopes-north"
    return scrapeForecast(westSlopesNorth), westSlopesNorth

def scrapeWestSlopesCentral():
    westSlopesCentral = "https://nwac.us/avalanche-forecast/#/west-slopes-central"
    return scrapeForecast(westSlopesCentral), westSlopesCentral

def scrapeWestSlopesSouth():
    westSlopesSouth = "https://nwac.us/avalanche-forecast/#/west-slopes-south"
    return scrapeForecast(westSlopesSouth), westSlopesSouth

def scrapeStevensPass():
    stevensPass = "https://nwac.us/avalanche-forecast/#/stevens-pass"
    return scrapeForecast(stevensPass), stevensPass

def scrapeSnoqualmiePass():
    snoqualmiePass = "https://nwac.us/avalanche-forecast/#/snoqualmie-pass"
    return scrapeForecast(snoqualmiePass), snoqualmiePass

def scrapeEastSlopesCentral():
    eastSlopesCentral = "https://nwac.us/avalanche-forecast/#/east-slopes-central"
    return scrapeForecast(eastSlopesCentral), eastSlopesCentral

def scrapeEastSlopesSouth():
    eastSlopesSouth = "https://nwac.us/avalanche-forecast/#/east-slopes-south"
    return scrapeForecast(eastSlopesSouth), eastSlopesSouth

def scrapeEastSlopesNorth():
    eastSlopesNorth = "https://nwac.us/avalanche-forecast/#/east-slopes-north"
    return scrapeForecast(eastSlopesNorth), eastSlopesNorth

def scrapeMtHood():
    mountHood = "https://nwac.us/avalanche-forecast/#/mt-hood"
    return scrapeForecast(mountHood), mountHood





