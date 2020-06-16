from datetime import datetime, time
from typing import Type

import requests
from PyQt5 import QtWidgets, QtCore

import clientui

class MessengerWindow(QtWidgets.QMainWindow, clientui.Ui_Messenger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.sendMessage)
        self.last_message_time = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getUpdates)
        self.timer.start(1000)


    def sendMessage(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.textEdit.toPlainText()

        if not username:
            self.addText('Error: username is empty!')
            self.addText('')
            return
        if not password:
            self.addText('Error: password is empty!')
            self.addText('')
            return
        if not text:
            self.addText('Error: text is empty!')
            self.addText('')
            return

        response = requests.post(
            'http://127.0.0.1:5000/send',
            json={"username": username, "password": password, "text": text,}
        )
        if not response.json()['ok']:
            self.addText('Error: Access denied!')
            self.addText('')
            return

        self.textEdit.clear()
        self.textEdit.repaint()

    def addText(self, text):
        self.textBrowser.append(text)
        self.textBrowser.repaint()

    def getUpdates(self):
        response = requests.get(
            "http://127.0.0.1:5000/messages",
            params={'after': self.last_message_time}
        )
        data = response.json()

        for message in data['messages']:
            beauty_time = datetime.fromtimestamp(message["time"])
            beauty_time = beauty_time.strftime('%d/%m/%Y %H:%M:%S')
            self.addText(beauty_time + '' + message["username"], )
            self.addText(message["text"])
            self.addText('')
            self.last_message_time = message["time"]


app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec_()
