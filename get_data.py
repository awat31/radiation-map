import pymysql.cursors
import json
def main():
    # Connect to the database
    connection = pymysql.connect(host='34.142.25.93',
                                 user='root',
                                 password='KingH1ghl4nd3r21!',
                                 database='sensor_data',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
        # Read a single record
            sql = "SELECT `data` FROM `data`"
            cursor.execute(sql)
            result = cursor.fetchall()
            data = open('data.json', "w")
            data.write(r'{ "particle-data": ')
            info = json.dump(result, data)
            data.write(r' }')
            data.close()
           
if __name__ == '__main__':
    main()
