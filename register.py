from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import json


def RegisterWindow():
    def close():
        dialog.close()

    dialog = QDialog()
    mainLine = QVBoxLayout()
    btnLineW = QHBoxLayout()
    dialog.setWindowIcon(QIcon("signup_icon.png"))

    loginTextW = QLabel("New username:")
    passwordTextW = QLabel("Password:")
    townTextW = QLabel("Your Town:")
    loginEditW = QLineEdit()
    passwordEditW = QLineEdit()
    townEditW = QLineEdit()

    signBtnW = QPushButton("Sign Up")
    cancelBtnW = QPushButton("Cancel")




    mainLine.addWidget(loginTextW)
    mainLine.addWidget(loginEditW)
    mainLine.addWidget(passwordTextW)
    mainLine.addWidget(passwordEditW)
    mainLine.addWidget(townTextW)
    mainLine.addWidget(townEditW)

    btnLineW.addWidget(signBtnW)
    btnLineW.addWidget(cancelBtnW)

    mainLine.addLayout(btnLineW)
    dialog.setLayout(mainLine)

    cancelBtnW.clicked.connect(close)

    def reg():
        with open("data.json", 'r', encoding="utf-8") as file:
            json_data = json.load(file)
        userSign = loginEditW.text()
        passwordSign = passwordEditW.text()
        town = townEditW.text()
        if userSign in json_data:
            QMessageBox.warning(dialog, "LOH", "NO, NO")

        else:
            json_data[userSign] = {
                "password": passwordSign,
                "town": town
            }
            QMessageBox.warning(dialog, "Success", "Successfully")
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(json_data, file, indent=4)

            dialog.close()

    signBtnW.clicked.connect(reg)
    dialog.show()
    dialog.exec_()


