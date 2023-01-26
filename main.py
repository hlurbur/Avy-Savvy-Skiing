"""
main.py combines the methods in scraper, sheets, analyzeRoutes and emailer to iterate through users of the program and
send an email with their route suggestions for the day as well as a link to the full avalanche forecast."""

from scraper import *
from sheets import *
from analyzeRoutes import *
from emailer import *
from skiRoute import *
from user import *

#A list of user objects from the users sheet
users = readInUsers()

## Iterate through users. For each user, get the avalanche forecast from their region,
#choose their suggested routes, and send them a personalized email with their suggestion.
for user in users:
    name = user.get_userName()
    region = user.get_skiRegion().lower()
    email = user.get_email()

    #get the raw forecast of the users preferred region and the link to the forecast
    forecast, link = get_regionForecast(region)

    #get the route suggestion from the forecast
    routeSugg = chooseRoutes(forecast, region)

    #send the user an email with their route suggestion
    sendEmail(email, name, routeSugg, link)
