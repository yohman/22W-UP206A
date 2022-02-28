########################################

#     Folium HTML generator

########################################

import osmnx as ox
import folium

# ask user for a location
location = input("Hello. What city do you want to go to? ")

try:
    # get the lat/lon by geocoding the location
    latlon = ox.geocode(location)

    # create a folium map
    m = folium.Map(location=[latlon[0],latlon[1]])

    # save it as an html file
    m.save(location + '.html')
    
    # leave a message
    print('Bon voyage! Look for your travel file "'+location+'.html"')

except:
    print('Could not geocode your location')