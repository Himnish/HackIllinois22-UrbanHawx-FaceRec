from flask import Flask, render_template, Response, request
from flask_mail import Mail, Message
import cv2

from faceDetect import facedetection

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'urbanhawks0@gmail.com'
app.config['MAIL_PASSWORD'] = 'Login@2003'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/',  methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template('recognized.html')
    else:
        return render_template('index.html')


@app.route('/recognized')
def home():
    return render_template('recognized.html')

@app.route('/add')
def away():
    return render_template('add.html')

@app.route('/video_feed')
def video_feed():
    return Response (facedetection(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)