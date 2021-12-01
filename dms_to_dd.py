# Convert DMS Co-Ordinates to DD
# Aaron Watkins

def main(latitude, longitude):

    latitude_start = ''
    longitude_start = ''
    latitude_fixed = ''
    longitude_fixed = ''
    lat1 = ''
    lat2 = ''
    lat3 = ''
    long1 = ''
    long2 = ''
    long3 = ''

    #---------Fixing Latitude -----------------------------    
    if latitude[0] == 'S':
        latitude_start = '-'
    
    latitude_fixed = latitude[1:len(latitude)]

    lat1 = latitude_fixed[0:2]
    lat2 = latitude_fixed[2:4]
    lat3 = latitude_fixed[5:len(latitude)]
    lat3 = lat3[0] + '.' + lat3[1:len(lat3)]

    lat1 = int(lat1)
    lat2 = int(lat2)
    lat3 = float(lat3)


    final_latitude_float = lat1 + lat2/60 + lat3/3600
    final_latitude_str = str(final_latitude_float)
    final_latitude = latitude_start + final_latitude_str


    #---------Fixing Longitude -----------------------------------
    if longitude[0:3] == 'W00':
        longitude_start = '-'
        longitude_fixed = longitude[3:len(longitude)]
    else:
        longitude_fixed = longitude[1:len(longitude)]
    long1 = longitude_fixed[0:1]
    long2 = longitude_fixed[1:3]
    long3 = longitude_fixed[4:len(latitude)]
    long3 = long3[0] + '.' + long3[1:len(long3)]

    long1 = int(long1)
    long2 = int(long2)
    long3 = float(long3)

    final_longitude_float = long1 + long2/60 + long3/3600
    final_longitude_str = str(final_longitude_float)
    final_longitude = longitude_start + final_longitude_str

    #---------Print Finals-------------------------------------------

    return(final_latitude, final_longitude)


if __name__ == '__main__':
    main('N5556.1364', 'W00314.1091')
