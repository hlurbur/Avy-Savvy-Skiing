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
    
def makeForecastNumerical(avyForecast):
    """
    Takes in a list of strings of the forecast at each elecation level, returns a list of only the integer forecast
    for each elecation band.
    """
    numericalForecast = []
    for forecast in avyForecast:
        numericalForecast.append(int(forecast[1:2])) #this should grab just the integer and turn it into an int
    print(numericalForecast)
    return numericalForecast


#In the format [above treeline, near treeline, below treeline]
numerical = makeForecastNumerical([' 3 - Moderate ', ' 2 - Moderate ', ' 2 - Moderate '])
print(numerical)


def chooseRoutes(avyForecast):
    """
    Takes in an avalanche forecaset and returns a list of up to three safe routes to ski for the day
    """
    #Make the forecast purley numerical for easy analysis
    numericalForecast = makeForecastNumerical(avyForecast)
    
    #get the numerical forecast at each elevtion band
    below = numericalForecast[0]
    near = numericalForecast[1]
    above = numericalForecast[2]
    
    #get a list of all possible routes to ski
    goodRoutes = readInRoutes()
   

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
        print("There are no safe routes to ski today:(")

    #If there are less than three options, just print the routes that are suitable to ski
    if len(goodRoutes) <= 3:
        return goodRoutes

    #otherwise, if there are more than three safe routes to ski, sort them by fun level and reutnr the three most fun options.
    else:
        print(goodRoutes)
        goodRoutes.sort(key=lambda x: x.get_funOften(), reverse = True)
        #Return a list of the top three most fun routes 
        return [goodRoutes[0], goodRoutes[1], goodRoutes[2]]



