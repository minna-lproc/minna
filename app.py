from asyncio import create_task
from unicodedata import name
from urllib import response
from flask import Flask, make_response,send_file,render_template,request,jsonify

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_mail import Mail, Message
from config import mail_username, mail_password
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import (create_engine, MetaData, Table,Column, Integer, String)
from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, DateTime)



# klheuklzofurhpfs

app = Flask(__name__, template_folder="./templates")

app.config['GOOGLEMAPS_KEY'] = "AIzaSyDNc_aHa9fNKbTS1amE0gSO2ouOj9trU8U"
GoogleMaps(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/user_info'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
meta_data = MetaData()

requestdataset = Table(
    'requestdataset', 
    meta_data, 
    Column('id', Integer(), primary_key = True),
    Column('name', String(255), nullable = False),    
    Column('email', String(255), nullable = False),
    Column('organization', String(255), nullable = False),
    Column('message', String(255), nullable = False),
    Column('attachment', String(255), nullable = False),
) 

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
meta_data.create_all(engine)

try:
    conn = engine.connect()
    print('db connected')
    print('connection object is :{}' .format(conn))
except:
    print('db not connected')
    
# class requestdataset(db.Model):
#     id = db.Column(db.Integer, primary_key=True),
#     name = db.Column(db.String(255), nullable = True),
#     email = db.Column(db.String(255), nullable = True),
#     organization = db.Column(db.String(255), nullable=True),
#     message = db.Column(db.String(255), primary_key=True),
#     attachment = db.Column(db.String(255), primary_key=True),



mail = Mail(app)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = "587"
app.config['MAIL_USE_TLS'] = "True"
app.config['MAIL_USE_SSL'] = "False"
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

# HOST_NAME = "localhost"
# username = "joe.clio001@gmail.com"
# password = "!purps#9932CC"
# mail_from = "joe.clio001@gmail.com"
# mail_to = "alemaniacamilleite111@gmail.com"
# mail_subject = "Requested datasets"
# mail_body = "This is a test message"

# mimemsg = MIMEMultipart()
# mimemsg['From']=mail_from
# mimemsg['To']=mail_to
# mimemsg['Subject']=mail_subject
# mimemsg.attach(MIMEText(mail_body, 'plain'))
# connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
# connection.starttls()
# connection.login(username,password)
# connection.send_message(mimemsg)
# connection.quit()

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

# @app.route("/send", methods=["POST"])
# def send(): 
#     mail = MIMEMultipart("alternative")
#     mail["Subject"] = mail_subject
#     mail["From"] = mail_from
#     mail["To"] = mail_to
    
#     data = dict(request.form)
#     msg = "<html><head></head><body>"
#     for key, value in data.items(): 
#         msg += key + " : " + value + "<br>"
#         msg += "</body></html>"
#         mail.attach(MIMEText(msg, "html"))

#         mailer = smtplib.SMTP("localhost")
#         mailer.sendmail(mail_from. mail_to, mail.as_string())
#         mailer.quit()
        
#         res = make_response("OK", 200)
#         return res


@app.route("/view", methods = ['GET', 'POST'])
def view():
    if request.method == 'POST': 
        name = request.form.get('name')
        email = request.form.get('email')
        organization = request.form.get('organization')
        message = request.form.get('message')
        # msg = Message(subject  = f"Mail from {name}", body = f" Name: {name}\n E-Mail: {email}\n Organization:{organization}\n\nMessage: {message}",  sender = mail_username, recipients = ['alemaniacamilleite111@gmail.com'])
        # # mail.send(msg)

        qry = requestdataset.insert().values(
            name = request.form.get('name'), 
            email = request.form.get('email'),
            organization = "CCS", 
            message = "hello world", 
            attachment = "dataset.csv", 
        )

        # print(str(ins))
        # print(ins.compile().params)
        result = conn.execute(qry)
    
        print(result)
        # print('Last inserted key:')
        # print(result.inserted_primary_key)

        resp = {'message': 'Successfull request', 'name': name}
        return make_response(jsonify(resp), 200)
    return render_template("view.html")

    #     # name = request.form.get('name')
    #     # email = request.form.get('email')
    #     # organization = request.form.get('organization')
    #     # message = request.form.get('message')
    #     # msg = Message(subject  = f"Mail from {name}", body = f" Name: {name} E-Mail: {email}\n Organization:{organization}\n\nMessage: {message}", 
    #     # sender = mail_username, recipients = ['"alemaniacamilleite111@gmail.com"'])
    #     # mail.send(msg)
    # # try:
    # #     mail = mail.send.get('MAIL_USERNAME')
    # #     print(response.status_code)
    # #     print(response.body)
    # #     print(response.headers)
    # # except Exception as e:
    # #         print(e.message)
    # #     result = {}
    # #     result ['name'] = request.form['name']
    # #     result ['email'] = request.form['email'].replace(' ', '').lower()
    # #     result ['message'] = request.form['message']
    
    # # sendTestEmail(result)
  
    # return render_template('view.html', success=True)
    # # return render_template('view.html', ** locals())

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

    
