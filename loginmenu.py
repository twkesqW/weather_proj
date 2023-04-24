import sys
from PyQt5.QtWidgets import *
import json
import register
import main

#-----------------------------------------------------------------------------------------------------------------------

login_app = QApplication([])
login_win = QWidget()
login_win.setObjectName("login_win")
login_app.setApplicationName("Login")
login_app.setStyleSheet('''


        QWidget{
            background-color: #333333;
            color:white;
            font-weight:bold;
        }
        
        QWidget#login_win{
            padding:5px 10px;
        }
        
        QLineEdit{
            background:white;
            font-size:14px;
            color:black;
            font-family:sans-serif;
            border-radius:2px;
            padding:3px 8px;
            font-size:11px;
        }
        
        QPushButton{
            background:white;
            padding:5px 7px;
            border-radius:2px;
            margin:5px;
            color:grey;
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
cancelBtn = QPushButton("Cancel")

#-----------------------------------------------------------------------------------------------------------------------

main_Vline.addWidget(loginText)
main_Vline.addWidget(loginEdit)
main_Vline.addWidget(passwordText)
main_Vline.addWidget(passwordEdit)
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
        print("No")
        sys.exit()

#-----------------------------------------------------------------------------------------------------------------------


signBtn.clicked.connect(ClickReg)
cancelBtn.clicked.connect(CloseApp)
loginBtn.clicked.connect(loginGame)
main_Vline.addLayout(btn_line)
login_win.setLayout(main_Vline)

login_win.show()
login_app.exec_()