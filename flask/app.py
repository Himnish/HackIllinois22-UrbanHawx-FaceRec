from flask import Flask, render_template, Response, request
from flask_mail import Mail, Message
import cv2
import os

from faceDetect import facedetection

app = Flask(__name__)

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
    return render_template('add.html')

@app.route('/video_feed')
def video_feed():
    return Response (facedetection(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)