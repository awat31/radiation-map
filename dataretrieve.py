import Flask

app = Flask(__name__)

@app.route('/index.html', methods=['POST'])
def result():
    print(request.data)  # raw data
    print(request.json)  # json (if content-type of application/json is sent with the request)
    print(request.get_json(force=True)) # json (if content-type of application/json is not sent)
    data = { 'latitude': -12.543, 'longitude': 131.036 }
    print(data)
    return render_template('./index.html', latitude=0.00)
    return render_template('./index.html', longitude=0.00)

# Add a section to use the dd conversion script to fix data
