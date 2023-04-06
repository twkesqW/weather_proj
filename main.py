from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon,QPixmap
import requests

# ------------------------------------------------------------------------------------------------------------------------

def weather_app(local):

    location =local
    api_key = "8fd6f775df7f422781d164050232303"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    request = requests.get(url)
    data = request.json()
    datalocal = data['location']
    data_weather = data['current']

    # -----------------------------------------------------------------------------------------------------------------------

    main_win = QDialog()
    main_win.setGeometry(250, 250, 500, 400)
    main_win.setFixedWidth(500)
    main_win.setFixedHeight(400)
    main_win.setWindowTitle('Weather App')
    main_win.setWindowIcon(QIcon("weather.png"))
    main_win.setStyleSheet('''
            QWidget{
                background-color: #333333;
            }
             QLabel#welcome{
                color:white;
                font-size:20px;
                font-weight:bold;
                margin:0;
                padding:0;
             }

             QLineEdit#search{
                padding:10px 15px;
                background-color:white;
                color:grey;
                border-radius:10px;
                font-size:13px;
             }

            QLabel{
                font-size:15px;
                font-weight:bold;
                color:white;
                margin-bottom:10px;
            }

            QLabel#town{
                font-size:18px;
                margin-bottom:50px;
            }

            QPushButton#search_btn{
                background-color:white;
                padding:5px 10px;
                margin-top:20px;
                border-radius:10px;
                font-weight:bold;
            }

        ''')

    # ------------------------------------------------------------------------------------------------------------------------

    mainV_line = QVBoxLayout()
    mainH_line = QHBoxLayout()
    searchV_line = QVBoxLayout()
    weatherV_line = QVBoxLayout()

    # -----------------------------Elements-----------------------------------------------------------------------------------

    search_line = QLineEdit()
    search_line.setObjectName("search")
    search_line.setFixedWidth(200)
    search_line.setPlaceholderText("Search...")
    search_btn = QPushButton("Search")
    search_btn.setObjectName("search_btn")
    search_btn.setFixedWidth(200)

    welcome_text = QLabel("WELCOME!")
    welcome_text.setObjectName("welcome")

    imagel = QLabel()
    image = QPixmap("weather.png")
    image = image.scaled(100, 100)
    imagel.setPixmap(image)

    town = QLabel(location)
    town.setObjectName("town")
    temperature = QLabel(f"Temperature: {str(data_weather['temp_c'])}")
    humidity = QLabel(f"Humidity: {str(data_weather['humidity'])}")
    wind_kph = QLabel(f"Wind kph: {str(data_weather['wind_kph'])}")
    cloud = QLabel(f"Cloud: {str(data_weather['cloud'])}")

    update_text = QLabel(str(data_weather['last_updated']))

    # -----------------------------Add elements-------------------------------------------------------------------------------

    searchV_line.addWidget(search_line, alignment=Qt.AlignLeft)
    searchV_line.addWidget(search_btn, alignment=Qt.AlignTop)

    weatherV_line.addWidget(imagel, alignment=Qt.AlignHCenter)
    weatherV_line.addWidget(town, alignment=Qt.AlignHCenter)
    weatherV_line.addWidget(temperature, alignment=Qt.AlignHCenter)
    weatherV_line.addWidget(humidity, alignment=Qt.AlignHCenter)
    weatherV_line.addWidget(wind_kph, alignment=Qt.AlignHCenter)
    weatherV_line.addWidget(cloud, alignment=Qt.AlignHCenter)

    mainV_line.addLayout(mainH_line)
    mainV_line.addWidget(update_text, alignment= Qt.AlignHCenter | Qt.AlignBottom)

    mainH_line.addLayout(searchV_line)
    mainH_line.addLayout(weatherV_line)

    #-------------------------------------------------------------------------------------------------------------------

    def changeTown():
        try:
            location = search_line.text()
            api_key = "8fd6f775df7f422781d164050232303"
            url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
            request = requests.get(url)
            data = request.json()
            datalocal = data['location']
            data_weather = data['current']

            town.setText(location)
            temperature.setText(f"Temperature: {str(data_weather['temp_c'])}")
            humidity.setText(f"Humidity: {str(data_weather['humidity'])}")
            wind_kph.setText(f"Wind kph: {str(data_weather['wind_kph'])}")
            cloud.setText(f"Cloud: {str(data_weather['cloud'])}")
            welcome_text.setText('Welcome!')
            search_line.setText("")

        except:
            clearAll()
            town.setText("Введіть справжнє місто")

    def clearAll():
        town.setText("")
        temperature.setText(f"")
        humidity.setText(f"")
        wind_kph.setText(f"")
        cloud.setText(f"")
        welcome_text.setText('')
        search_line.setText("")

    search_btn.clicked.connect(changeTown)
    # ------------------------------------------------------------------------------------------------------------------------
    main_win.setLayout(mainV_line)
    main_win.exec_()

