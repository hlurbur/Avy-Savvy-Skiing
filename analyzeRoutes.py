"""
analyzeRoutes sorts and compares skiRoutes based on the region the user would like to ski in
and the avalanche forecast for the day. AnalyzeRoutes gets the forecast from a specific region,
that forecast and region can then be used in chooseRoutes which picks safe routes
to ski in the specified region.
"""

from scraper import *
from sheets import *
from skiRoute import *


def get_regionForecast(regionString):
    """
    Takes in the string name of a region and reutns the avalanche forecast from the region.
    """
    if regionString.lower() == "olympics" :
        return scrapeOlympics()
    elif regionString.lower() == "west slopes north":
        return scrapeWestSlopesNorth()
    elif regionString.lower() == "west slopes central":
        return scrapeWestSlopesCentral()
    elif regionString.lower() == "west slopes south":
        return scrapeWestSlopesSouth()
    elif regionString.lower() == "stevens pass":
        return scrapeStevensPass()
    elif regionString.lower() == "snoqualmie pass":
        return scrapeSnoqualmiePass()
    elif regionString == "east slopes central":
        return scrapeEastSlopesCentral
    elif regionString.lower() == "east slopes south":
        return scrapeEastSlopesSouth()
    elif regionString.lower() == "east slopes north":
        return scrapeEastSlopesNorth()
    elif regionString == ("mount hood" or "mt hood" or "mt. hood"):
        return scrapeMtHood()
    else:
        print("No valid Region Name found") #should this have a quit as well?
    
def makeForecastNumerical(avyForecast):
    """
    Takes in a list of strings of the forecast at each treeline level, returns a list of only the integer forecast
    for each elevation level.

    Args:
    avyForecast: a list of strings, each of which is the forecast for a treeline level.

    Returns:
    numericalForecast: A list of integer forecasted danger levels, in the format [aboveTreeline, nearTreeline, belowTreeline]
    """
    numericalForecast = []
    for forecast in avyForecast:
        #grab just the integer and turn it into an int
        numericalForecast.append(int(forecast[1:2])) 
    return numericalForecast

def getRegionRoutes(region):
    """
    Takes in the string name of a region and returns a list of routes which are in the specified region.
    
    Args:
    region: The string name of a region a user wants to ski in

    Returns:
    goodRoutes: a list of routes that are in the specified region
    """
    goodRoutes = []
    allRoutes = readInRoutes()
    for route in allRoutes:
        #if the region of the route equals the specified region
        if route.get_region().lower() == region:
            goodRoutes.append(route)

    return goodRoutes


def chooseRoutes(avyForecast, region):
    """
    Takes in an avalanche forecaset and returns a string of the safe routes to ski,
    otherwise returns a string saying there are no safe routes to ski

    Args:
    avyForecast: a list of strings of th avalanche forecast for each treeline level: below, near and above
    region: the string name of a region of the Cascades

    Returns:
    routeSuggestion: a string of suggested routes to ski or a string saying there are no
    safe routes to ski.
    """
    #Make the forecast purley numerical for easy analysis
    numericalForecast = makeForecastNumerical(avyForecast)
    
    #get the danger number for each treeline level
    below = numericalForecast[0]
    near = numericalForecast[1]
    above = numericalForecast[2]
    
    #get a list of all possible routes to ski in the specified region
    goodRoutes = getRegionRoutes(region)
   

    #If the forecast at an elevation band is considerale or above, remove all routues which both pass through
    #the given elevation band AND pass through avalanche terrain

    if below >= 3:
        for route in goodRoutes:
            if route.get_belowTreeline() == True and route.get_avyTerrain() == True:
                goodRoutes.remove(route)
    if near >= 3:
        for route in goodRoutes:
            if route.get_nearTreeline() == True and route.get_avyTerrain == True:
                goodRoutes.remove(route)
    if above >= 3:
        for route in goodRoutes:
            if route.get_aboveTreeline() == True and route.get_avyTerrain() == True:
                goodRoutes.remove(route)

    #If the forecast is moderate, remove routes which have high risk, or in which entering avy terrian is unavoidable
    if below == 2:
        for route in goodRoutes:
            if route.get_belowTreeline()== True and route.get_avyTerrain() and route.get_avyAvoidable() == False and route.get_risk() >= 6:
                goodRoutes.remove(route)

    if near == 2:
        for route in goodRoutes:
            if route.get_nearTreeline() == True and route.get_avyTerrain() and route.get_avyAvoidable() == False and route.get_risk() >= 6:
                goodRoutes.remove(route)
    if above == 2:
        for route in goodRoutes:
            if route.get_aboveTreeline() == True and route.get_avyTerrain() and route.get_avyAvoidable() == False and route.get_risk() >= 6:
                goodRoutes.remove(route)
                
                
    #If there are no routes remaining, print that there are no safe routes to ski today
    if len(goodRoutes)==0:
        #In the case that there are no safe routes, print that message
        return "There are no safe routes to ski today:("

    #If there are less than three options, just print the routes that are suitable to ski
    if len(goodRoutes) <= 3:
        return goodRoutes

    #otherwise, if there are more than three safe routes to ski, sort them by fun level and reutrn the three most fun options.
    else:
        goodRoutes.sort(key=lambda x: x.get_funOften(), reverse = True)
        #Return a list of the top three most fun routes 
        top3 = [goodRoutes[0], goodRoutes[1], goodRoutes[2]]
        #return the top three routes 
        return top3



