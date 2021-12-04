# Convert DMS Co-Ordinates to DD
# Aaron Watkins

def main(latitude, longitude):

    latitude_start = ''
    longitude_start = ''
    latitude_fixed = ''
    longitude_fixed = ''
    degrees = ''
    minutes = ''
    seconds = ''
    longdegrees = ''
    longminutes = ''
    longseconds = ''

    #---------Fixing Latitude -----------------------------
    # If the latitude is in the south, the coordinates need to start with a '-'
    if latitude[0] == 'S':
        latitude_start = '-'

    # Remove the N/S Indicator
    latitude_fixed = latitude[1:len(latitude)]

    # This section splits the DMS into it's parts - Degrees, Minutes Seconds
    degrees = latitude_fixed[0:2]
    minutes = latitude_fixed[2:4]
    seconds = latitude_fixed[5:len(latitude)]
    seconds = seconds[0] + '.' + seconds[1:len(seconds)]

    # Convert to int/float so we can do maths
    degrees = int(degrees)
    minutes = int(minutes)
    seconds = float(seconds)

    # The conversion calculation to DD
    final_latitude_float = degrees + minutes/60 + seconds/3600
    final_latitude_str = str(final_latitude_float)
    # Add the '-' if necessary
    final_latitude = latitude_start + final_latitude_str


    #---------Fixing Longitude -----------------------------------
    # If the longitude is in the west, the coordinates need to start with a '-'
    if longitude[0:3] == 'W00':
        longitude_start = '-'
        longitude_fixed = longitude[3:len(longitude)]
    else:
        longitude_fixed = longitude[1:len(longitude)]
    # This section splits the DMS into it's parts - Degrees, Minutes Seconds
    longdegrees = longitude_fixed[0:1]
    longminutes = longitude_fixed[1:3]
    longseconds = longitude_fixed[4:len(latitude)]
    longseconds = longseconds[0] + '.' + longseconds[1:len(longseconds)]

    # Convert to int/float so we can do maths
    longdegrees = int(longdegrees)
    longminutes = int(longminutes)
    longseconds = float(longseconds)

    # The conversion calculation to DD
    final_longitude_float = longdegrees + longminutes/60 + longseconds/3600
    final_longitude_str = str(final_longitude_float)
    # Add the '-' if necessary
    final_longitude = longitude_start + final_longitude_str

    #---------Print Finals-------------------------------------------
    
    return(final_latitude, final_longitude)


if __name__ == '__main__':
    main('N5556.1364', 'W00314.1091')
