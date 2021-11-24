import Flask
import js2py

app = Flask(__name__)

@app.route('/js.html', methods=['POST'])
def result():
    print(request.data)  # raw data
    print(request.json)  # json (if content-type of application/json is sent with the request)
    print(request.get_json(force=True)) # json (if content-type of application/json is not sent)
    data = { 'latitude': -12.543, 'longitude': 131.036 }
    print(data)
    latitude = 55.93371222222222
    longitude = -3.233636388888889
    #return render_template('./index.html', latitude=0.00)
    #return render_template('./index.html', longitude=0.00)
    js2py.eval_js(latitude, longitude)

# Add a section to use the dd conversion script to fix data

if __name__ == '__main__':
    result()
