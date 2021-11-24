import Flask
import js2py

app = Flask(__name__)

    latitude = 55.93371222222222
    longitude = -3.233636388888889

@app.route('/')
def index_render():
return render_template("index.html")

@app.route('/index')
def test_page_view():
    return render_template('js/index.js', latitude=latitude)
    return render_template('js/index.js', longitude=longitude)

# @app.route('/js.html', methods=['POST'])
# def result():
#     print(request.data)  # raw data
#     print(request.json)  # json (if content-type of application/json is sent with the request)
#     print(request.get_json(force=True)) # json (if content-type of application/json is not sent)
#     data = { 'latitude': -12.543, 'longitude': 131.036 }
#     print(data)

#     return render_template('js/index.html', latitude=0.00)
#     return render_template('js/index.js', longitude=0.00)


# Add a section to use the dd conversion script to fix data

if __name__ == '__main__':
    result()
