from flask import Flask, request

app = Flask(__name__)

@app.route('https://api.particle.io', methods=['POST'])
def result():
    print(request.data)  # raw data
    print(request.json)  # json (if content-type of application/json is sent with the request)
    print(request.get_json(force=True))
