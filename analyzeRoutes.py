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
    

skiRoutes = readInRoutes()
progUsers = readInUsers()

hadassah = progUsers[0]
print(hadassah)

