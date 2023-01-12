import pandas as pd


url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSk4DAFdMfMObApX_jl4mseQM950yuxAuCxL2lJLe17Udi16JZOZ1KR1yq3UpagOkRGW7nHoESb6nTM/pubhtml"

# https://docs.google.com/spreadsheets/d/1M4zSa9Osun8BaQos3dhi97FRa74uo5EJjaIh3NV7-3U/edit#gid=0

sheet_id = "1M4zSa9Osun8BaQos3dhi97FRa74uo5EJjaIh3NV7-3U"

sheet_name = 'Ski Routes'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df = pd.read_csv(url)
print(df.head())