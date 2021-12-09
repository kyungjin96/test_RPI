from flask import Flask
import numpy as np
app = Flask(__name__)

@app.route("/")
def helloworld():
    str = 'hello world! kj'
    return str

app.run(host="0.0.0.0",port='8000')
