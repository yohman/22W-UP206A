########################################

#     Libraries

########################################

# libraries
import pandas as pd

# to import and manipulate api/json data
import urllib.request 
import json

# to manipulate csv files
import csv
from csv import DictWriter

# to work with time
from datetime import datetime
import pytz
from pytz import timezone
import time

# command line parser
import argparse

########################################

#     Set up the command arguments

########################################

parser = argparse.ArgumentParser(description='This script calls the LA Metro API, and retrieves live bus locations, putting the data into a csv file. You can define which bus route to get buses for (--route default 2), how many times to call the API (--times default 10), and how many seconds to rest between calls (--rest default 10).')

# arguments
parser.add_argument("--route", 
                    default=2, 
                    type=int, 
                    help="Enter a route number (default=2)")

parser.add_argument("--times", 
                    default=10, 
                    type=int, 
                    help="How many times to run (default=10)")

parser.add_argument("--rest", 
                    default=10, 
                    type=int, 
                    help="How many seconds to rest between calls (default=10)")

parser.add_argument("--filename", 
                    required=False,
                    default='la_metro.csv',
                    type=str, 
                    help="File name with csv extension (default=la_metro.csv)")


args = parser.parse_args()

########################################

#     Create a csv file

########################################

    
# field names  
fields = ['route_id',
 'predictable',
 'id',
 'seconds_since_report',
 'run_id',
 'heading',
 'longitude',
 'latitude',
 'time']

# writing to csv file ('w') 
with open(args.filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  

# create an empty df
df = pd.DataFrame(columns = fields)

########################################

#     Create the function

########################################

def get_bus(route=args.route):
    # api url for metro stops
    metro_url = 'https://api.metro.net/agencies/lametro/routes/'+str(args.route)+'/vehicles/'

    # call the api and bring the data in
    with urllib.request.urlopen(metro_url) as url:
        data = json.loads(url.read().decode())

    # convert json data to temp dataframe, and add a timestamp
    df_new = pd.json_normalize(data, 'items')
    
    # add the timestamp
    now = datetime.now(timezone('US/Pacific'))
    df_new['time'] = now.strftime('%Y-%m-%d %H:%M:%S')
    
    # append the new data to csv file (add the bus route to the file name)
    with open(args.filename, 'a') as busfile: 

        dictwriter = DictWriter(busfile, fieldnames=fields) 

        for index, row in df_new.iterrows():
            dictwriter.writerow(row.to_dict()) 

        busfile.close()

    # rest
    time.sleep(args.rest)
    

########################################

#     Automate the call

########################################

# set a counter
i = 1

# start the loop
while i <= args.times:
    # timestamp to print out
    now = datetime.now(timezone('US/Pacific'))
    now = now.strftime('%Y-%m-%d %H:%M:%S')

    print(str(i) + ': ' + now)
    get_bus()
    i += 1
