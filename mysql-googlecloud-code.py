import base64
import pymysql
from pymysql.err import OperationalError
from os import getenv

# TODO(developer): specify SQL connection details by replacing
# root_password, database_name and connection_name with your values
mysql_config = {
  'user': 'root',
  'password': 'KingH1ghl4nd3r21!',
  'db': 'sensor_data',
  'charset': 'utf8mb4',
  'cursorclass': pymysql.cursors.DictCursor,
  'autocommit': True
}
CONNECTION_NAME = 'gps-monitoring-system-329610:europe-west2:gps-project'

# Create SQL connection globally to enable reuse
# PyMySQL does not include support for connection pooling
mysql_conn = None


def __get_cursor():
    """
    Helper function to get a cursor
      PyMySQL does NOT automatically reconnect,
      so we must reconnect explicitly using ping()
    """
    try:
        return mysql_conn.cursor()
    except OperationalError:
        mysql_conn.ping(reconnect=True)
        return mysql_conn.cursor()


def save_data(event, context):

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    datestring = event['attributes']['published_at']

    query  = "INSERT INTO data VALUES ('"
    query += context.event_id + "', '"
    query += event['attributes']['device_id'] + "', '"
    query += event['attributes']['event'] + "', '"
    query += pubsub_message + "', "
    query += "STR_TO_DATE('" + datestring[0:len(datestring)-1] + "000', '%Y-%m-%dT%H:%i:%s.%f')" + ");"
    print(query)

    global mysql_conn

    if not mysql_conn:
        try:
            mysql_conn = pymysql.connect(**mysql_config)
        except OperationalError:
            # If production settings fail, use local development ones
            mysql_config['unix_socket'] = f'/cloudsql/{CONNECTION_NAME}'
            mysql_conn = pymysql.connect(**mysql_config)

    # Remember to close SQL resources declared while running this function.
    # Keep any declared in global scope (e.g. mysql_conn) for later reuse.
    with __get_cursor() as cursor:
        cursor.execute(query)
