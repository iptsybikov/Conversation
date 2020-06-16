from datetime import datetime, timedelta
import flask


from flask import Flask
serverstarttime = datetime.now()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    serverlivetime = datetime.now()
    delta = serverlivetime - serverstarttime
    upmin = (delta.seconds % 3600) // 60
    return {
        'status': True,
        'startalive': serverstarttime,
        'uptime': str(delta)
    }

app.run()
