import pandas as pd
from skiRoute import skiRoute

sheet_id = "1M4zSa9Osun8BaQos3dhi97FRa74uo5EJjaIh3NV7-3U"


def readInRoutes(): 
    #sheet_name = 'Routes'
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid=0&format=csv&sheet=Routes"
    df = pd.read_csv(url,index_col=0)
    print(df.head())
    print(len(df))

    myRoutes = []

    for routeName, row in df.iterrows():
        #print(routeName, row["Region"])
        thisRoute = skiRoute(routeName, row["Region"], row["Below Treeline"], row["Near Treeline"], row["Above Treeline"], row["Avalanche Terrain?"], row["Avy terrain avoidable?"], row["Fun out of 10"], row["Risk"])
        print(thisRoute)
        myRoutes.append(thisRoute)
    return myRoutes

def readInUsers():
    
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid=0&format=csv&sheet=Routes"
    df = pd.read_csv(url,index_col=0)
    print(df.head())
    print(len(df))
    pass

readInRoutes()