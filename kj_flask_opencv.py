from flask import Flask


app = Flask(__name__)

@app.route("/")
def helloworld():
    str = 'hello world! kj'
    return str



# app.run(host="0.0.0.0",port='8000')

import cv2

def cam() :
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret,frame = cap.read()
        cv2.imshow('cap',frame)
        z =  cv2.waitKey(1)
        if z == 27:
            break
        pass
    cv2.destroyAllWindows()
    return


import threading

if __name__ == '__main__' : 
    cap_thread = threading.Thread(target=cam)
    cap_thread.daemon =True
    cap_thread.start()

    app.run(host="0.0.0.0",port='8000')
    

