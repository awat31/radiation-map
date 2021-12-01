import json

def main(json_output, polygondict, ppm):
    colour = ''
    ppm = float(ppm)
    if ppm < 400:
        colour = 'green'
    elif ppm > 400 and ppm < 1000:
        colour = 'darkgreen'
    elif ppm > 1000 and ppm < 2000:
        colour = 'yellow'
    elif ppm > 2000 and ppm < 5000:
        colour = 'orange'
    elif ppm > 5000 and ppm < 10000:
        colour = 'red'
    elif ppm > 10000:
        colour = 'darkred'
        
    geojson = open(json_output, "a")
    geojson.write(r'{ "type": "Feature", "geometry": { "type": "Polygon",')
    geojson.write(f'"coordinates": [ {polygondict} ]')
    geojson.write(r'}, "properties": {')
    geojson.write(f'"PPM": "{ppm}"')
    geojson.write(r' }, "style": { ')
    geojson.write(f'"fill":"{colour}"')
    geojson.write(r'} } },')
    

if __name__ == '__main__':
    main()
