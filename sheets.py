
"""
Sheets reads in route and user data from a google sheet using the pandas library.
Sheets creates skiRoute and user objects as it reads in data. 
"""

import pandas as pd
from skiRoute import skiRoute
from user import user

#The sheet ID of a public google sheet where route and user data is stored.
#The the skiRoute sheet and user sheet share the same sheet ID.
sheet_id = "1M4zSa9Osun8BaQos3dhi97FRa74uo5EJjaIh3NV7-3U"


def readInRoutes(): 
    """
    Reads in routes from the google sheet creating a skiRoute object for each row of the sheet.

    Returns:
    myRoutes: A list of skiRoute objects
    """

    #the URL fo the sheet with route data
    routeURL = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid=0&format=csv&sheet=Routes"
    #Create a data frame from the sheet csv
    routeDF = pd.read_csv(routeURL,index_col=0)

    #Initialize a list to store route objects
    myRoutes = []
    
    #iterate through all rows of the data, creating a skiRoute object from each row of data
    for routeName, row in routeDF.iterrows():
        thisRoute = skiRoute(routeName, row["Region"], row["Below Treeline"], row["Near Treeline"], row["Above Treeline"], row["Avalanche Terrain?"], row["Avy terrain avoidable?"], row["Fun out of 10"], row["Risk"])
        #add the route to the list of routes
        myRoutes.append(thisRoute)
    return myRoutes

def readInUsers():
    """
    Reads in users from the users google sheet and creates user objects from each row of the sheet.
    
    Returns:
    myUsers: a list of user objects
    """

    #Create the pandas dataframe from the sheet url
    sheet_name = "Users"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    userDF = pd.read_csv(url,index_col=0)
    
    #initialize an empty list to store users
    myUsers = []
    
    #iterate through all rows of the data, creating a user object from each row of data
    for userName, row in userDF.iterrows():
        thisUser = user(userName, row["Region to Ski"], row["Email"])
        myUsers.append(thisUser)
    
    #return the list of all users created from the spreadsheet
    return myUsers

