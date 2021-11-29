import json

def main(json_output, polygondict, ppm):
    geojson = open(json_output, "a")
    geojson.write(r'{ "type": "Feature", "geometry": { "type": "Polygon",')
    geojson.write(f'"coordinates": [ {polygondict } ]')
    geojson.write(r'}, "properties": {')
    geojson.write(f'"PPM": "{ppm}"')
    geojson.write(r' } },')
    

if __name__ == '__main__':
    main()
