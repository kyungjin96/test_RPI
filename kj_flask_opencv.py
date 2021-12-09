from flask import Flask
import numpy as np
app = Flask(__name__)

@app.route("/")
def helloworld():
    str = 'hello world! kj'
    return str

# app.run(host="0.0.0.0",port='8000')

import cv2

if __name__ == '__main__' : 

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret,frame = cap.read()
        cv2.imshow('cap',frame)
        z =  cv2.waitKey(1)
        if z == 27:
            break
        pass
    cv2.destroyAllWindows()
    app.run(host="0.0.0.0",port='8000')
    