from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__, template_folder="./templates")

app.config['GOOGLEMAPS_KEY'] = "AIzaSyDNc_aHa9fNKbTS1amE0gSO2ouOj9trU8U"

GoogleMaps(app)

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)