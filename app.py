import os
from asyncio import create_task
from unicodedata import name
from urllib import response
from flask import Flask, make_response,send_file,render_template,request,jsonify
import pymysql
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_mail import Mail, Message
import smtplib
from werkzeug.utils import secure_filename

# klheuklzofurhpfs

app = Flask(__name__, template_folder="./templates")

# Configurations
app.config.from_object('config')

GoogleMaps(app)
mail = Mail(app)

ALLOWED_EXTENSIONS = set(['txt', 'docx' ,'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

try:
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='password',
        db='minna_local',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
except:
    print('db not connected')

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

@app.route("/process_form")
def process_form():
    return render_template("process_form.html")

@app.route("/view", methods = ['GET', 'POST'])
def view():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        organization = request.form.get('organization')
        message = request.form.get('message')
        # sender = MAIL_USERAME, recipients = ["'alemaniacamilleite111@gmail.com'"]

        f = request.files['file']
        filename = f.filename
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        with connection.cursor() as cursor:
                prepared_qry = 'INSERT INTO `requestdataset` (name, email, organization, message, file) VALUES (%s, %s, %s, %s, %s)'
                cursor.execute(prepared_qry,(name, email, organization, message, filename))
                connection.commit()

        try:
            msg = Message(
                subject  = f"Mail from {name}",
                body = f" Name: {name} E-Mail: {email}\n Organization:{organization}\n\nMessage: {message}",
                sender = email,
                recipients = ["alemaniacamilleite111@gmail.com"]
            )
            res = mail.send(msg)
            pring(res)
        except Exception as e:
                print(msg)

        resp = {'message': 'Successfull request'}
        return make_response(jsonify(resp), 200)

    return render_template("view.html")


@app.route("/req")
def req():
    return render_template('req.html')


@app.route("/cebuano")
def cebuano():
    return render_template('cebuano.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

@app.route("/technology")
def technology():
    return render_template('technology.html')

@app.route("/activities")
def activities():
    return render_template('activities.html')

@app.route("/news")
def news():
    return render_template('news_list.html')

@app.route("/news#news01")
def news01():
    return render_template('./news/news_1.html')

@app.route("/news#news02")
def news02():
    return render_template('./news/news_2.html')

@app.route("/news#news03")
def news03():
   return render_template('./news/news_3.html')

# @app.route("/process_form", methods = ['POST'])
# def process_form():
#     return render_template('./process_form')

@app.route("/download_files")
def download_files():
    p = "../sample.txt"
    return send_file(p, as_attachment=True)

if __name__ == "__main__":
        app.run(debug=True)
