# Minimum working example to approximately geocode Channel Islands postcodes.
# Source data is from Wikipedia: 
# https://en.wikipedia.org/wiki/JE_postcode_area
# https://en.wikipedia.org/wiki/GY_postcode_area
# Coordinates were manually added by looking at parish boundaries on OSM

# import packages 
import re
import pandas as pd

# open the geocoding CSV - must be in the same directory as the script. 
postcode_ref = pd.read_csv("./channel_islands_postcodes_geocoding.csv")

# create a list of postcodes to geocode - any list of postcodes can go here (e.g. extracted from an existing dataset as a list)
pcds = ['JE2 4GG', 'JE3 6AB', 'JE2 6FD', 'JE2 3LB', 'JE2 3JZ']

# Make a list of regex patterns from the column in the spreadsheet
regexes = postcode_ref['Regex']

# Turn these into a list of `re` regex queries 
reg_list = []
for i in regexes.values: reg_list.append(re.compile(i))

# create an empy dict to hold the geocoding results (is this better as a df? it's easy to swap)
results_dict = {}

# for each postcode, run each regex query in turn until there is a match. When there is a match, add the lat, long and parish name to the results dict. 
for i in pcds: 
    for j in reg_list: 
        result = re.search(j, i)
        if  result == None: 
            pass
        else: 
            results_dict[i] = result.re.pattern
            results_dict[i] = {'lat': postcode_ref.loc[postcode_ref["Regex"] == j.pattern].Lat.values[0], 
                               'long': postcode_ref.loc[postcode_ref["Regex"] == j.pattern].Long.values[0], 
                               'parish': postcode_ref.loc[postcode_ref["Regex"] == j.pattern]['Parish or island'].values[0]
                               }


# view the results
results_dict