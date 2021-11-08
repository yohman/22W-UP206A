########################################

#     Folium HTML generator

########################################

# libraries
import osmnx as ox
import folium
import argparse

########################################

#     Set up the command parser

########################################

parser = argparse.ArgumentParser(description='This script generates an interactive map.')

# arguments
parser.add_argument("--zoom", 
                    default=10, 
                    type=int, 
                    help="Enter a zoom level (default=10)")

args = parser.parse_args()

########################################

#     Generate the map

########################################

# ask user for a location
location = input("Hello. What city do you want to go to? ")
marker = input("Leave a marker? (yes/no)")

try:
    # get the lat/lon by geocoding the location
    latlon = ox.geocode(location)

    # create a folium map
    m = folium.Map(location=[latlon[0],latlon[1]],
                   zoom_start = args.zoom)
    
    # marker
    if marker == 'yes':
        folium.Marker(
            [latlon[0],latlon[1]], tooltip=location
        ).add_to(m)

    # save it as an html file
    m.save(location + '.html')
    
    # leave a message
    print('Bon voyage! Look for your travel file "'+location+'.html"')

except:
    print('Could not geocode your location')