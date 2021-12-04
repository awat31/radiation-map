import dms_to_dd
import json
import altitude_to_int
import output_to_geojson
import output_to_geojson_polygon
import os
import get_data


def main():
    latitude = ''
    converted_latitude = ''
    longitude = ''
    converted_longitude = ''
    altitude = ''
    PPM = 0
    json_output = 'temp.json'
    final_output = 'coords.geojson'
    safe = []
    okay = []
    notgood = []
    dangerous = []
    deadly = []
    fucked = []
    alloptions = [safe, okay, notgood, dangerous, deadly, fucked]
    sql_data = 0
    items = 0
    polygondict = []
    polyend = []

    #get_data.main()
    
    geojsonfile = open(json_output, "w")
    geojsonfile.write(r'{"type": "FeatureCollection","features":[ ')
    geojsonfile.close()
           
    with open('data.json') as json_file:
        fullfile = json.load(json_file)
        for sql_data in fullfile['particle-data']:
           data = sql_data['data']
           # Second Level looks at the actual data entries
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
               fucked.append(secondlevel)

    # For each list in the alloptions list of lists (Divided by their PPM)
    # If the length of the list is empty (No reading with PPM in that range), skip it.
    for sql_data in alloptions:
        PPM = 0
        if len(sql_data) == 0:
            continue
    # If The length of the list is 1 or two, put the data as a point (Need 3 to make a polygon)    
        else: 
    # The data exists as a single list entry, this selects it so we can look at the data inside
            for i in sql_data:
                dictdata = i
                latitude = dictdata['latitude']
                longitude = dictdata['longitude']
                altitude = dictdata['altitude']
                # Calls script to convert Sensor DMS to DD (Read by WebApp)
                finals = dms_to_dd.main(latitude, longitude)
                PPM = (dictdata['ppm'])
                final_latitude = finals[0]
                final_longitude = finals[1]
                final_altitude = altitude_to_int.main(altitude)
                output_to_geojson.main(json_output, final_latitude, final_longitude, final_altitude, PPM)
            
    with open (json_output) as jsonfile:
        for line in jsonfile:
        # This section removes the comma from the final entry so the json doesn't expect more
        # It splits the whole string at either side of the comma, then puts them together.
            length = len(line)
            lengthend = length - 1
            final_data = line[0:lengthend]
            finalfile = open(final_output, "w")
            finalfile.write(final_data)
            finalfile.write(r'] }')
    #os.remove(json_output)
            

if __name__ == '__main__':
    main()
