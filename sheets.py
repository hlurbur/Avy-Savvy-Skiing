import pandas as pd
from skiRoute import skiRoute
from user import user

sheet_id = "1M4zSa9Osun8BaQos3dhi97FRa74uo5EJjaIh3NV7-3U"


def readInRoutes(): 
    """
    Reads in routes from the google sheet. Returns a list of route objects, myRoutes.
    """
    #sheet_name = 'Routes'
    routeURL = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid=0&format=csv&sheet=Routes"
    routeDF = pd.read_csv(routeURL,index_col=0)
    print(routeDF.head())
    print(len(routeDF))

    myRoutes = []
    
    #itterate through all rows of the data, creating a route from each row of data
    for routeName, row in routeDF.iterrows():
        #print(routeName, row["Region"])
        thisRoute = skiRoute(routeName, row["Region"], row["Below Treeline"], row["Near Treeline"], row["Above Treeline"], row["Avalanche Terrain?"], row["Avy terrain avoidable?"], row["Fun out of 10"], row["Risk"])
        print(thisRoute)
        myRoutes.append(thisRoute)
    return myRoutes

def readInUsers():

    #userURL = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid=0&format=csv&sheet=Users"
    sheet_name = "Users"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    userDF = pd.read_csv(url,index_col=0)
    print(userDF.head())
    print(len(userDF))
    
    myUsers = []
    
    #itterate through all rows of the data, creating a user object from each row of data
    for userName, row in userDF.iterrows():
        thisUser = user(userName, row["Region to Ski"], row["Email"])
        print(thisUser)
        myUsers.append(thisUser)
    
    #return the list of all users created from the spreadsheet
    return myUsers

readInRoutes()
readInUsers()