import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import json
import register
import main

#-----------------------------------------------------------------------------------------------------------------------

login_app = QApplication([])
login_win = QWidget()
login_win.setObjectName("login_win")
login_app.setApplicationName("Login")
login_app.setWindowIcon(QIcon("login_icon.png"))
login_app.setStyleSheet('''


        QWidget{
            background-color: #333333;
            color:white;
            font-weight:bold;
        }
        
    
        
        
        QLineEdit{
            background:#333333;
            font-size:14px;
            color:white;
            font-family:sans-serif;
            border-radius:2px;
            padding:3px 8px;
            font-size:11px;
            border:1px solid white;
            
        }
        
        QPushButton{
            background:#333333;
            padding:5px 7px;
            border-radius:2px;
            margin:5px;
            color:white;
            border:1px solid white;
    
        }
        
        QPushButton:hover{
                background-color:white;
                color:#333333;
                
            }
        
        QLabel{
            color:white;
           
        }
        

''')

#-----------------------------------------------------------------------------------------------------------------------

main_Vline = QVBoxLayout()
btn_line = QHBoxLayout()

#-----------------------------------------------------------------------------------------------------------------------

loginText = QLabel("Login:")
passwordText = QLabel("Password:")
loginEdit = QLineEdit()
passwordEdit = QLineEdit()
loginBtn = QPushButton("Login")
signBtn = QPushButton("Sign Up")
cancelBtn = QPushButton(" Exit ")
text_err = QLabel("")
#-----------------------------------------------------------------------------------------------------------------------

main_Vline.addWidget(loginText)
main_Vline.addWidget(loginEdit)
main_Vline.addWidget(passwordText)
main_Vline.addWidget(passwordEdit)
main_Vline.addWidget(text_err, alignment=Qt.AlignVCenter | Qt.AlignHCenter)
btn_line.addWidget(loginBtn)
btn_line.addWidget(signBtn)
btn_line.addWidget(cancelBtn)

#-----------------------------------------------------------------------------------------------------------------------

def ClickReg():
    register.RegisterWindow()

def CloseApp():
    login_app.exit()

def loginGame():
    with open("data.json", 'r', encoding='utf8') as file:
        jsonD = json.load(file)
    login = loginEdit.text()
    password = passwordEdit.text()

    if login in jsonD:
        if password == jsonD[login]['password']:
            login_win.hide()
            main.weather_app(jsonD[login]['town'])

    else:
        text_err.setText("Помилка! Неправильний логін чи пароль")

#-----------------------------------------------------------------------------------------------------------------------


signBtn.clicked.connect(ClickReg)
cancelBtn.clicked.connect(CloseApp)
loginBtn.clicked.connect(loginGame)
main_Vline.addLayout(btn_line)
login_win.setLayout(main_Vline)

login_win.show()
login_app.exec_()