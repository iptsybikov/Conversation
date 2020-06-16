import time
from datetime import datetime, timedelta
import flask

from flask import Flask, request
# apps server
app = Flask(__name__)
messages = [
    {"username": "Ivan", "text": "Hello!", "time": time.time()},
    {"username": "Ayuna", "text": "Hello Ivan!", "time": time.time()}
]
# 'username': 'password'
users = {
    'Ivan': '12345',
    'Ayuna': '54321'
}

# main page 127.0.0.1
@app.route("/")
def hello():
    return "Hello World!<a href=/status>Show status</a>"

# status page 127.0.0.1/status
@app.route("/status")
def status():
    return {
        'status': True,
        'time': datetime.now().strftime('%y/%m/%d %H:%M:%S'),
        'messages_count': len(messages),
        'user_count': len(users)
    }

@app.route("/messages")
def messages_view():
    """
    Получение сообщений после отметки after
    input: after - отметка времени
    output:{
        "messages": [
        {"username": str, "text": str, "time": float},
        ...
        ]
    }
    """
    after = float(request.args['after'])
    new_messages = [message for message in messages if message['time'] > after]
    return {'messages': new_messages}

@app.route("/send", methods=['Post'])
def send_view():
    """
    Отправка сообщений
    input: {
        "username": str,
        "text": str
    }
    output:{"ok": true}
    """
    data = request.json
    username = data["username"]
    password = data["password"]

    if username not in users or users[username] !=password:
        return {"ok": false}


    text = data["text"]

    messages.append({"username": username, "text": text, "time": time.time()})
    return {'ok': True}

@app.route("/auth", methods=['Post'])
def auth_view():
    """
    Авторизовать или выдать ошибку
    input: {
        "username": str,
        "password": str
    }
    output:{"ok": bool}
    """
    data = request.json
    username = data["username"]
    password = data["password"]
    if username not in users:
        users[username] = password
        return {"ok": True}
    elif users[username] == password:
        return {"ok": True}
    else:
        return {"ok": False}

app.run()
