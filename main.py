from scraper import *
from sheets import *
from analyzeRoutes import *
from emailer import *
from skiRoute import *
from user import *

#A list of user objects from the users sheet
users = readInUsers()

for user in users:
    name = user.get_userName()
    region = user.get_skiRegion().lower()
    email = user.get_email()

    #get the raw forecast of the users preferred region
    forecast = get_regionForecast(region)

    #get the string route suggestion from the forecast
    routeSugg = chooseRoutes(forecast, region)

    print(routeSugg)
    #send the user an email with their route suggestion
    sendEmail(email, name, routeSugg)
