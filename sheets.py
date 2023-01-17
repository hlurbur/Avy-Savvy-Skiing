import pandas as pd
from skiRoute import skiRoute


#url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSk4DAFdMfMObApX_jl4mseQM950yuxAuCxL2lJLe17Udi16JZOZ1KR1yq3UpagOkRGW7nHoESb6nTM/pubhtml"

#url = "https://docs.google.com/spreadsheets/d/1M4zSa9Osun8BaQos3dhi97FRa74uo5EJjaIh3NV7-3U/edit#gid=0"

sheet_id = "1M4zSa9Osun8BaQos3dhi97FRa74uo5EJjaIh3NV7-3U"

#sheet_name = 'Sheet1'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid=0&format=csv"
df = pd.read_csv(url,index_col=0)
print(df.head())
print(len(df))

myRoutes = []

for routeName, row in df.iterrows():
    #print(routeName, row["Region"])
    thisRoute = skiRoute(routeName, row["Region"], row["Below Treeline"], row["Near Treeline"], row["Above Treeline"], row["Avalanche Terrain?"], row["Avy terrain avoidable?"], row["Fun out of 10"], row["Risk"])
    print(thisRoute)
    myRoutes.append(thisRoute)
#print(myRoutes) 
