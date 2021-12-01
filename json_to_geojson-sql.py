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
        if len(sql_data) == 0:
            continue
    # If The length of the list is 1 or two, put the data as a point (Need 3 to make a polygon)    
        elif len(sql_data) == 1 or len(sql_data) == 2:
            dictdata = sql_data[0]
            latitude = dictdata['latitude']
            if latitude == "":
                    items = items + 1
                    continue
            longitude = dictdata['longitude']
            altitude = dictdata['altitude']
            # Calls script to convert Sensor DMS to DD (Read by WebApp)
            finals = dms_to_dd.main(latitude, longitude)
            PPM = (dictdata['ppm'])
            final_latitude = finals[0]
            final_longitude = finals[1]
            final_altitude = altitude_to_int.main(altitude)
            output_to_geojson.main(json_output, final_latitude, final_longitude, final_altitude, PPM)

    # If the length of the list is 3 or more, write the data into polygon format.
        elif len(sql_data) > 2 :
            
            while items < len(sql_data):
                dictdata2 = sql_data[items]
                latitude = dictdata2['latitude']
                # Removes Entries that have NULL Data
                if latitude == "":
                    items = items + 1
                    continue
                #------------------------------------
                longitude = dictdata2['longitude']
                altitude = dictdata2['altitude']
                PPM = (dictdata2['ppm'])
                finals = dms_to_dd.main(latitude, longitude)
                final_latitude = float((finals[0]))
                final_longitude = float(finals[1])
                coordinates = [final_longitude, final_latitude]
                polygondict.append(coordinates)
    # If it's the first co-ordinate reaading ([0]), write to variable so it's added at the end to complete the Polygon
                if items == 0:
                    polyend = coordinates
                items = items + 1
    # Add the First Polygon entry to the end to complete the shape
            polygondict.append(polyend)
            output_to_geojson_polygon.main(json_output, polygondict, PPM)
                
            

    geojsonfile = open(json_output, "a")
    geojsonfile.write(r'] }')
    geojsonfile.close()
    with open (json_output) as jsonfile:
        for line in jsonfile:
        # This section removes the comma from the final entry so the json doesn't expect more
        # It splits the whole string at either side of the comma, then puts them together.
            length = len(line)
            lengthstart = length - 4
            lengthend = length - 3
            final_data = line[0:lengthstart]
            final_data2 = line[lengthend:length]
            endtowrite = final_data + final_data2
            finalfile = open(final_output, "w")
            finalfile.write(endtowrite)
            finalfile.close()
    os.remove(json_output)
            

if __name__ == '__main__':
    main()
