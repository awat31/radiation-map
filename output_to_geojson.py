import json

def main(json_output, latitude, longitude, altitude, ppm):
    geojson = open(json_output, "a")
    geojson.write(r'{ "type": "Feature", "geometry": { "type": "Point",')
    geojson.write(f'"coordinates": [{longitude}, {latitude}, {altitude}]')
    geojson.write(r'}, "properties": {')
    geojson.write(f'"PPM": "{ppm}"')
    geojson.write(r' } },')
    

if __name__ == '__main__':
    main()
