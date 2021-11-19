from flask import Flask, request

app = Flask(__name__)

@app.route('./index.js/initMap(latitude, longitude)', methods=['POST'])
def result():
    print(request.data)  # raw data
    print(request.json)  # json (if content-type of application/json is sent with the request)
    print(request.get_json(force=True)) # json (if content-type of application/json is not sent)
    latitude = -12.543
    longitude = 131.036
    return latitude, longitude
