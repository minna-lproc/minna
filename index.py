from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__, template_folder="./templates")

app.config['GOOGLEMAPS_KEY'] = "AIzaSyDNc_aHa9fNKbTS1amE0gSO2ouOj9trU8U"

GoogleMaps(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/index#map")
def map():
    return render_template('index.html')

@app.route("/publications")
def publications():
    return render_template('publications.html')

@app.route("/people")
def people():
    return render_template('people.html')

@app.route("/activities")
def activities():
    return render_template('activities.html')

@app.route("/news")
def news():
    return render_template('news_list.html')
@app.route("/news#news01")
def news01():
    return render_template('news_1.html')
@app.route("/news#news02")
def news02():
    return render_template('news_2.html')

if __name__ == "__main__":
    app.run(debug=True)