from scraper import *
from sheets import *
from skiRoute import *

def get_regionForecast(regionString):
    if regionString.lower() == "olympics" :
        return scrapeOlympics
    elif regionString.lower() == "west slopes north":
        return scrapeWestSlopesNorth
    elif regionString.lower() == "west slopes central":
        return scrapeWestSlopesCentral
    elif regionString.lower() == "west slopes south":
        return scrapeWestSlopesSouth
    elif regionString.lower() == "stevens pass":
        return scrapeStevensPass
    elif regionString.lower() == "snoqualmie pass":
        return scrapeSnoqualmiePass
    elif regionString == "east slopes central":
        return scrapeEastSlopesCentral
    elif regionString.lower() == "east slopes south":
        return scrapeEastSlopesSouth
    elif regionString.lower() == "east slopes north":
        return scrapeEastSlopesNorth
    elif regionString == ("mount hood" or "mt hood" or "mt. hood"):
        return scrapeMtHood
    else:
        return "No valid Region Name found"
    
def makeForecastNumerical(forecastList):
    
    numericalForecast = []
    for forecast in forecastList:
        numericalForecast += int(forecast[1:2]) #this should grab just the integer and turn it into an int
    return numericalForecast

def getBelowTL_routes(allRoutes):
    """
    takes a list of all routes in the spreadsheet and returns a list of the routes which cross through the below treeline elevation band
    """
    belowTLroutes = []
    for route in allRoutes:
        if get_belowTreeline(route) == True:
            belowTLroutes.append(route)
    return belowTLroutes

def getNearTL_routes(allRoutes):
    """
    takes a list of all routes and returns a list of the routes which cross through the near treeline elevation band
    """
    nearTLroutes = []
    for route in allRoutes:
        if get_nearTreeline(route) == True:
            nearTLroutes.append(route)
    return nearTLroutes

def getAboveTLroutes(allRoutes):
    """
    takes a list of all routes and returns a list of the routes which cross through the above treeline elevation band
    """
    aboveTLroutes = []
    for route in allRoutes:
        if get_aboveTreeline(route) == True:
            aboveTLroutes.append(route)
    return aboveTLroutes
#In the format [above treeline, near treeline, below treeline]
numericalForecast = [3,2,2]

goodRoutes = []

belowLT = getBelowTL_routes
nearTL = getNearTL_routes
aboveTL = getAboveTLroutes
#
if numericalForecast[0] < 3:
    goodRoutes.extend(aboveTL)




skiRoutes = readInRoutes()
progUsers = readInUsers()

hadassah = progUsers[0]
print(hadassah)

