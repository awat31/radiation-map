import json

# Writes the variables to the correct place in a geojson file
# This is necessary as we need to swap between literal and variable-passing writing, as there are many {} involved
def main(json_output, latitude, longitude, altitude, ppm):
    # Append the output file so we can add every entry and not overwrite them
    geojson = open(json_output, "a")
    # Initial Formatting
    geojson.write(r'{ "type": "Feature", "geometry": { "type": "Point",')
    # Write the variables
    geojson.write(f'"coordinates": [{longitude}, {latitude}, {altitude}]')
    # CLose the section and open Properties
    geojson.write(r'}, "properties": {')
    # Attach the PPM value
    geojson.write(f'"PPM": "{ppm}"')
    # Close the section
    geojson.write(r' } },')
    geojson.close()


if __name__ == '__main__':
    main()
