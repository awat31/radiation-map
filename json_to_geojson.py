import dms_to_dd
import json
import altitude_to_int
import output_to_geojson


def main():
    latitude = ''
    converted_latitude = ''
    longitude = ''
    converted_longitude = ''
    altitude = ''
    PPM = 0
    json_output = 'coords.geojson'

    geojsonfile = open(json_output, "w")
    geojsonfile.write(r'{"type": "FeatureCollection","features":[ ')
    geojsonfile.close()
           
    with open('example_data.json') as json_file:
        fullfile = json.load(json_file)
        for i in fullfile['particle-data']:
           data = i['data']
           secondlevel = json.loads(data)
           latitude = (secondlevel['latitude'])
           longitude = (secondlevel['longitude'])
           altitude = (secondlevel['altitude'])
           PPM = (secondlevel['ppm'])
           finals = dms_to_dd.main(latitude, longitude)
           final_latitude = finals[0]
           final_longitude = finals[1]
           final_altitude = altitude_to_int.main(altitude)
           print(f'{final_latitude}  {final_longitude}  {final_altitude} {PPM}')
           output_to_geojson.main(json_output, final_latitude, final_longitude, final_altitude, PPM)
    
    geojsonfile = open(json_output, "a")
    geojsonfile.write(r'] }')
    geojsonfile.close()         
               

           
           
           

if __name__ == '__main__':
    main()
