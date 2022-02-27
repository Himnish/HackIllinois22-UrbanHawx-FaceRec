from flask import Flask, render_template, Response, request
from flask_mail import Mail, Message
import cv2
import os
import time
from faceDetect import facedetection
from recognition import recog
from inputs import names
import sys
import inputs

app = Flask(__name__)

prev_time = 0

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'urbanhawks0@gmail.com'
app.config['MAIL_PASSWORD'] = 'Login@2003'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

people = ['Apoorva', 
          'Himnish',
          'Kushal', 
          'Malay', 
          'Ribhav']

def send_email():
    msg = Message('Hello from the other side!', sender =   'urbanhawks0@gmail.com', recipients = ['urbanhawks0@gmail.com'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    mail.send(msg)

@app.route('/',  methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form['check'] == 'home':
            return render_template('away.html')
        elif request.form['check'] == 'away':
            return render_template('home.html')
    else:
        return render_template('home.html')

@app.route('/recognized')
def home():
    return render_template('recognized.html', recognized=people)

@app.route('/add',  methods=["GET", "POST"])
def away():
    if request.method == "POST":
        newname = request.form.get('name')
        inputs.append_list(newname)
        # print(newname, flush=True, file=sys.stdout)
    return render_template('add.html')

@app.route('/video_feed_train')
def video_feed_train():
    global prev_time
    # img = train()
    # if found_unknown and (time.time() - prev_time) >= 10 * 10e6:
    #     prev_time = time.time()
    #     send_email()
    return Response (facedetection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_recog')
def video_feed_recog():
    return Response (recog(names), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_facedetect')
def video_feed_facedetect():
    return Response (facedetection(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)