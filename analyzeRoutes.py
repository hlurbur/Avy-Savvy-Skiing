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
        print("No valid Region Name found")
    
def makeForecastNumerical(forecastList):
    """
    Takes in a list of strings of the forecast at each elecation level, returns a list of only the integer forecast
    for each elecation band.
    """
    numericalForecast = []
    for forecast in forecastList:
        numericalForecast.append(int(forecast[1:2])) #this should grab just the integer and turn it into an int
    print(numericalForecast)
    return numericalForecast


#In the format [above treeline, near treeline, below treeline]

numerical = makeForecastNumerical([' 2 - Moderate ', ' 2 - Moderate ', ' 2 - Moderate '])
print(numerical)

goodRoutes = readInRoutes()
below = numerical[0]
near = numerical[1]
above = numerical[2]

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
        if route._belowTreeline()== True and route.get_avyTerrain() and route.get_avyAvoidable() == False and route.get_risk() >= 6:
            goodRoutes.remove(route)

if near == 2:
    for route in goodRoutes:
        if route.get_nearTreeline() == True and route.get_avyTerrain() and route.get_avyAvoidable() == False and route.get_risk() >= 6:
            goodRoutes.remove(route)
if above == 2:
    for route in goodRoutes:
        if route.get_aboveTreeline() == True and route.get_avyTerrain() and route.get_avyAvoidable() == False and route.get_risk() >= 6:
            goodRoutes.remove(route)
            
            
##Get the three most fun of the remaining routes
if len(goodRoutes)==0:
    print("There are no safe routes to ski today:(")

if len(goodRoutes) <= 3:
    print(goodRoutes)

else:
    #
    funSorted = goodRoutes.sort(key=lambda x: x._funOften, reverse = True)
    print(funSorted[0], funSorted[1], funSorted[2])



# progUsers = readInUsers()

# hadassah = progUsers[0]
# print(hadassah)

