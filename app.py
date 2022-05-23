
import os
from asyncio import create_task
from unicodedata import name
from urllib import response
from flask import Flask, make_response,send_file,render_template,request,jsonify
from jinja2 import TemplateNotFound
import pymysql
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_mail import Mail, Message
import smtplib
from werkzeug.utils import secure_filename
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from config import MAIL_SERVER, MAIL_USERNAME, MAIL_PASSWORD

# from mailer import *

# klheuklzofurhpfs

app = Flask(__name__, template_folder="./templates")

# Configurations
app.config.from_object('config')


app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = COMMASPACE.join(receiver_email)
# msg['Date'] = formatdate(localtime=True)
# msg['Subject'] = subject
# msg['file'] = file
# msg.attach(MIMEText(message))


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

# @app.route('/', defaults={'page': 'index'})
# @app.route('/<page>')
# def show(page):
#     try:
#         return render_template('%s.html' % page)
#     except TemplateNotFound:
#         abort(404)

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
        subject = "News Article Datasets request: " + name
        message = request.form.get('message')
        sender = app.config['MAIL_USERNAME']

        # server.login("joe.clio001@gmail.com", "Wysiwyg15!")
        # server.sendmail("alemaniacamilleite111@gmaail.com",name,email,organization, subject, message)


        # recipients = ['']

        f = request.files['file']
        filename = f.filename
        fullFilePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(fullFilePath)

        with connection.cursor() as cursor:
                prepared_qry = 'INSERT INTO `requestdataset` (name, email, organization, message, file) VALUES (%s, %s, %s, %s, %s)'
                cursor.execute(prepared_qry,(name, email, organization, message, filename))
                connection.commit()
        try:
            msg = Message(
                subject  = f"Mail from {name} ",
                body = f" Name: {name}\nE-Mail: {email}\n Organization:{organization}\n\nMessage: {message}",
                sender = MAIL_USERNAME,
                recipients = ['joe.clio001@gmail.com']
            )


            # for path in f:
            # part = MIMEBase('application', "octet-stream")
            # with open(fullFilePath, 'rb') as file:
            #     part.set_payload(file.read())
            #     encoders.encode_base64(part)
            #     part.add_header('Content-Disposition',
            #         'attachment; filename={}'.format(Path(path).name))
            # msg.attach(part)
            mail.send(msg)
        # smtp = smtplib.SMTP(server, port)
        # if use_tls:
        #     smtp.starttls()
        #     smtp.login(username, password)
        #     smtp.sendmail(send_from, send_to, msg.as_string())
        # smtp.quit()

        # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        #         smtp.ehlo()
        #         smtp.starttls
        #         smtp.ehlo()
        #     smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
        #         server.starttls()
        #     smtp.sendmail(email, sender, subject, message,msg,[fullFilePath])
        #     if use_tls:
        # smtp.starttls()
        # smtp.login(username, password)
        # smtp.sendmail(send_from, send_to, msg.as_string())
        # smtp.quit()
        except Exception as e:
                print(e)

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
