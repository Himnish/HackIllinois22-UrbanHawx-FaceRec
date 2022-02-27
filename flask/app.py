from flask import Flask, render_template, Response, request
import cv2


from faceDetect import facedetection

app = Flask(__name__)

camera = cv2.VideoCapture(0)


def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        frame = cv2.flip(frame, 1)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            
@app.route('/')
def index():
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