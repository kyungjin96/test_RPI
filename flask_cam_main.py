from flask import Flask
from flask import Response


app = Flask(__name__)

@app.route("/")

def helloworld():
    str = 'hello world! kj'
    return str

global video_frame

def encodeframe(): # img encode
    global video_frame
    while True:
        ret, encoded_image = cv2.imencode('.jpg', video_frame)
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')

    return

@app.route('/streaming')

def streaframe():
    return Response(encodeframe(), mimetype='multipart/x-mixed-replace; boundary=frame')



import cv2

def cam() :
    global video_frame
    cap = cv2.VideoCapture(0)

    while cap.isOpened():

        ret,frame = cap.read()
        video_frame = frame.copy()
        cv2.waitKey(20)
        pass
    return


import threading

if __name__ == '__main__' : 
    cap_thread = threading.Thread(target=cam)
    cap_thread.daemon =True
    cap_thread.start()

    app.run(host="0.0.0.0",port='8000')
    pass
    