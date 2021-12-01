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

    get_data.main()
    
    geojsonfile = open(json_output, "w")
    geojsonfile.write(r'{"type": "FeatureCollection","features":[ ')
    geojsonfile.close()
           
    with open('data.json') as json_file:
        fullfile = json.load(json_file)
        for sql_data in fullfile['particle-data']:
           data = sql_data['data']
           print(data)
           print(type(data))
           
           secondlevel = json.loads(data)          
           PPM = (secondlevel['ppm'])
           intPPM = float(PPM)

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

    for sql_data in alloptions:
        
        if len(sql_data) == 0:
            continue
        elif len(sql_data) == 1 or len(sql_data) == 2:
            dictdata = sql_data[0]
            latitude = dictdata['latitude']
            longitude = dictdata['longitude']
            altitude = dictdata['altitude']
            print(len(latitude))
            if len(latitude) == 0:
                break
            finals = dms_to_dd.main(latitude, longitude)
            PPM = (dictdata['ppm'])
            final_latitude = finals[0]
            final_longitude = finals[1]
            final_altitude = altitude_to_int.main(altitude)
            output_to_geojson.main(json_output, final_latitude, final_longitude, final_altitude, PPM)

        elif len(sql_data) > 2 :
            
            while items < len(sql_data):
                dictdata2 = sql_data[items]
                latitude = dictdata2['latitude']
                longitude = dictdata2['longitude']
                altitude = dictdata2['altitude']
                PPM = (dictdata2['ppm'])
                finals = dms_to_dd.main(latitude, longitude)
                final_latitude = float((finals[0]))
                final_longitude = float(finals[1])
                if final_latitude == 0 and final_longitude == 0:
                    break
                coordinates = [final_longitude, final_latitude]
                polygondict.append(coordinates)
                if items == 0:
                    polyend = coordinates
                items = items + 1
            polygondict.append(polyend)
            output_to_geojson_polygon.main(json_output, polygondict, PPM)
                
            

    geojsonfile = open(json_output, "a")
    geojsonfile.write(r'] }')
    geojsonfile.close()
    with open (json_output) as jsonfile:
        for line in jsonfile:
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
