from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
import requests
import urllib.request
# ------------------------------------------------------------------------------------------------------------------------

def weather_app(local):
    location = local
    api_key = "8fd6f775df7f422781d164050232303"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    request = requests.get(url)
    data = request.json()
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
                background-color:#333333;
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
                font-size:14px;
                font-weight:bold;
                color:white;
                margin-bottom:10px;
            }

            QLabel#town{
                font-size:18px;
                margin-bottom:50px;
            }

            QPushButton#search_btn{
                border:1px solid white;
                padding:7px 12px;
                margin-top:10px;
                border-radius: 5px;
                font-weight:bold;
                color:white;  
                   
            }
        
            QPushButton#search_btn:hover{
                background-color:white;
                color:#333333;
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






    urlIm = f"https:{str(data_weather['condition']['icon'])}"
    dataIm = urllib.request.urlopen(urlIm).read()

    imagel = QLabel()
    image = QPixmap()
    image.loadFromData(dataIm)
    image = image.scaled(100, 100)
    imagel.setPixmap(image)


    town = QLabel(location)
    town.setObjectName("town")
    temperature = QLabel(f"Температура: {str(data_weather['temp_c'])}")
    humidity = QLabel(f"Вологість: {str(data_weather['humidity'])}")
    wind_kph = QLabel(f"Вітер км/г: {str(data_weather['wind_kph'])}")
    cloud = QLabel(f"Хмарність: {str(data_weather['cloud'])}")
    pressure_mb = QLabel(f"Тиск: {str(data_weather['pressure_mb'])}")
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
    weatherV_line.addWidget(pressure_mb, alignment=Qt.AlignHCenter)
    mainV_line.addLayout(mainH_line)
    mainV_line.addWidget(update_text, alignment=Qt.AlignHCenter | Qt.AlignBottom)

    mainH_line.addLayout(searchV_line)
    mainH_line.addLayout(weatherV_line)

    #-------------------------------------------------------------------------------------------------------------------

    def changeTown():
        try:
            location_ = search_line.text()
            api_key_ = "8fd6f775df7f422781d164050232303"
            url_ = f"http://api.weatherapi.com/v1/current.json?key={api_key_}&q={location_}&aqi=no"
            request_ = requests.get(url_)
            data_ = request_.json()
            data_weather_ = data_['current']

            town.setText(location_)
            temperature.setText(f"Температура: {str(data_weather_['temp_c'])}")
            humidity.setText(f"Вологість: {str(data_weather_['humidity'])}")
            wind_kph.setText(f"Вітер км/г: {str(data_weather_['wind_kph'])}")
            cloud.setText(f"Хмарність: {str(data_weather_['cloud'])}")
            pressure_mb.setText(f"Тиск: {str(data_weather_['pressure_mb'])}")
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
        pressure_mb.setText("")


    search_btn.clicked.connect(changeTown)
    # ------------------------------------------------------------------------------------------------------------------------
    main_win.setLayout(mainV_line)
    main_win.exec_()

