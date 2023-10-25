# Channel Islands geocoding script / lookup table
Script to geocode postcodes from the Channel Islands (GY and JE)

BRC operates in the Channel Islands, but there is a lack of open data on postcodes in these areas that would allow us to assign locations to records using postcodes. For the UK, comprehensive postcode geocoding/lookups are provided by the ONS Postcode directory. 

This lookup table and processing script uses open data from Wikipedia to assign approximate latitude and longitude to postcodes from the Channel Islands, with approximate accuracy at the parish level. It is suitable for giving a rough indication of where a postcode is but not suitable for locating specific streets or addresses. 

## How to use it 
This example is in Python, but the workflow should be repeatable using the same CSV file with any language that supports relational joins and regular expression matching. 
* Open the `channel-islands-postcodes.py` file in an editor
* On line 15, there is a sample of postcodes to geocode. This can be edited with any list of postcodes, either hard coded or read from another data source
* After the postcode source has been defined, save the file and run it with `python3 channel-islands-postcodes.py`
* The script will output a json file with the results (a lat/lng coordinate pair), that can be used for further processing/analysis
In the example in the Python script, the postcodes `JE2 4GG`, `JE3 6AB`, `JE2 6FD`, `JE2 3LB`, `JE2 3JZ` are returned as: 
```{json}
{"JE2 4GG": {"lat": 49.18, "long": -2.11, "parish": "Saint Helier"},
 "JE3 6AB": {"lat": 49.22, "long": -2.05, "parish": "Saint Martin"},
 "JE2 6FD": {"lat": 49.17, "long": -2.06, "parish": "Saint Clement"},
 "JE2 3LB": {"lat": 49.18, "long": -2.11, "parish": "Saint Helier"},
 "JE2 3JZ": {"lat": 49.18, "long": -2.11, "parish": "Saint Helier"}}
```

## How it was made
* Wikipedia has a breakdown of the locations referred to by the [`GY`](https://en.wikipedia.org/wiki/GY_postcode_area) and [`JE`](https://en.wikipedia.org/wiki/JE_postcode_area) postcodes, which helps to narrow postcodes down to a parish
* Coordinates were assigned manually at what looked to be the approximate population or cultural centre of each parish - e.g. the church a parish is named after (from OpenStreetMap), or if there was a very obvious populated area (from satellite imagery). 
* The incomplete postcodes were added to a lookup table alongside their coordinates
* A regular expression checks any inputted postcodes against the most complete match it can find in the lookup table - so for the `JE2 4GG` postcode, it will match in the lookup table to the regex `JE2 4[A-Z][A-Z]`. 
