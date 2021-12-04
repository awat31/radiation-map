# This script outputs all the GPS Points as red markers.

# Import Required packages and scripts
import dms_to_dd
import json
import altitude_to_int
import output_to_geojson
import output_to_geojson_polygon
import os
import get_data


def main():
    # Declare Variables and Lists
    json_output = 'temp.json'
    final_output = 'coords.geojson'
    latitude = ''
    converted_latitude = ''
    longitude = ''
    converted_longitude = ''
    altitude = ''
    PPM = 0
    sql_data = 0
    items = 0
    safe = []
    okay = []
    notgood = []
    dangerous = []
    deadly = []
    yadead = []
    polygondict = []
    polyend = []
    alloptions = [safe, okay, notgood, dangerous, deadly, yadead]

    # Call the script that connects to the SQL Database and pulls data
    get_data.main()

    # Open the temp JSON file and begin the top of file formatting
    geojsonfile = open(json_output, "w")
    geojsonfile.write(r'{"type": "FeatureCollection","features":[ ')
    geojsonfile.close()

    # For each line in the data.json file (from the SQL GET)
    # Break it down to exctract the individual data points
    with open('data.json') as json_file:
        fullfile = json.load(json_file)
        for sql_data in fullfile['particle-data']:
           data = sql_data['data']
           # Second Level looks at the actual data entries within the 'Data' from SQL
           secondlevel = json.loads(data)
           PPM = (secondlevel['ppm'])
           intPPM = float(PPM)

    # Writes the whole data element to a list depending on it's PPM Level
           if intPPM < 400:
               safe.append(secondlevel)
           elif intPPM > 400 and intPPM < 1000:
               okay.append(secondlevel)
           elif intPPM > 1000 and intPPM < 2000:
               notgood.append(secondlevel)
           elif intPPM > 2000 and intPPM < 5000:
               dangerous.append(secondlevel)
           elif intPPM > 5000 and intPPM < 10000:
               deadly.append(secondlevel)
           elif intPPM > 10000:
               yadead.append(secondlevel)

    # For each list in the alloptions list of lists (Divided by their PPM)
    # If the length of the list is empty (No reading with PPM in that range), skip it.
    for sql_data in alloptions:
        PPM = 0
        if len(sql_data) == 0:
            continue
        else:
            # Pull the necessary data from the SQL entry and write it to a variable
            for i in sql_data:
                dictdata = i
                latitude = dictdata['latitude']
                longitude = dictdata['longitude']
                altitude = dictdata['altitude']
                # Calls script to convert Sensor DMS to DD (WebApp renders DD, not DMS)
                finals = dms_to_dd.main(latitude, longitude)
                PPM = (dictdata['ppm'])
                # Take the returned DD Coordinates and write ti variables
                final_latitude = finals[0]
                final_longitude = finals[1]
                # Remove the Altitude Indicator from the Altitude (*THIS COULD BE REMOVED FROM THE ARGON*)
                final_altitude = altitude_to_int.main(altitude)
                # Write the converted variables to the GeoJSON File
                output_to_geojson.main(json_output, final_latitude, final_longitude, final_altitude, PPM)

    # Open the JSON Output file from the last command
    with open (json_output) as jsonfile:
        for line in jsonfile:
        # There is only one line
        # This section removes the comma from the final entry so the json doesn't expect more data
        # It splits the whole string at either side of the comma, then puts them together.
            length = len(line)
            lengthend = length - 1
            final_data = line[0:lengthend]
            finalfile = open(final_output, "w")
            finalfile.write(final_data)
            finalfile.write(r'] }')
    #os.remove(json_output)
    # ^ This was commented out to prevent permissions errors on the cloud instance.


if __name__ == '__main__':
    main()
