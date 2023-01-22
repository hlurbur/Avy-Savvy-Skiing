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



# belowLT = getBelowTL_routes
# nearTL = getNearTL_routes
# aboveTL = getAboveTLroutes
#

goodRoutes = readInRoutes()
below = numericalForecast[0]
near = numericalForecast[1]
above = numericalForecast[2]

if below >= 3:
    for route in goodRoutes:
        if get_belowTreeline(route) == True and get_avyTerrain(route) == True:
            goodRoutes.remove(route)
if near >= 3:
    for route in goodRoutes:
        if get_nearTreeline(route) == True and get_avyTerrain(route) == True:
            goodRoutes.remove(route)
if above >= 3:
    for route in goodRoutes:
        if get_aboveTreeline(route) == True and get_avyTerrain(route) == true:
            goodRoutes.remove(route)

#If the forecast is moderate, remove routes which have high risk, or in which entering avy terrian is unavoidable
if below == 2:
    for route in goodRoutes:
        if get_belowTreeline(route) == True and get_avyTerrain(route) and get_avyAvoidable(route) == False and get_risk(route) >= 6:
            goodRoutes.remove(route)

if near == 2:
    for route in goodRoutes:
        if get_nearTreeline(route) == True and get_avyTerrain(route) and get_avyAvoidable(route) == False and get_risk(route) >= 6:
            goodRoutes.remove(route)
if above == 2:
    for route in goodRoutes:
        if get_aboveTreeline(route) == True and get_avyTerrain(route) and get_avyAvoidable(route) == False and get_risk(route) >= 6:
            goodRoutes.remove(route)
            
            
##Get the three most fun of the remaining routes
if len(goodRoutes) <= 3:
    print(goodRoutes)

else:
    #
    funSorted = goodRoutes.sort(key=lambda x: x._funOften, reverse = True)
    print(funSorted[0], funSorted[1], funSorted[2])

# progUsers = readInUsers()

# hadassah = progUsers[0]
# print(hadassah)

