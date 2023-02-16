import requests 
import os
from PyQt5.QtWidgets import QMessageBox
from dotenv import load_dotenv
# -24.058906201692693, -46.84559548727812
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def createMsg(type, text):
    msg = QMessageBox()
    if type == 'Error':
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        return msg
    elif type == 'Info':
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        return msg
    elif type == 'Warn':
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        return msg

def get_latLon(c):
    url =  f"http://api.openweathermap.org/geo/1.0/direct?q={c}&&appid={SECRET_KEY}"
    response = requests.get(url)
    response = response.json()
    lat = response[0]['lat']
    lon = response[0]['lon']
    return lat, lon


def get_response(city):
    c = city

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={c}&appid=3f008eaded8c742da704e2b081283f7b&lang=pt_br"

        response = requests.get(url)
        response = response.json()

        if response['cod'] == '404':
            msg = createMsg('Error', f'Erro! Cidade {c} não encontrada')
            msg.exec_()
            return
        


        temp = response['main']['temp']
        temp = temp - 273.15

        return response['weather'][0]['description'], str(int(temp)), response['weather'][0]['main']
    except Exception as e:
        msg = createMsg('Error', f'Erro, verifique o nome da cidade e tente novamente {e}')
        msg.exec_()
        return

    



def get_temp():
    t = response['main']['temp']
    t = t - 273.15
    return int(t)


url = "https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=3f008eaded8c742da704e2b081283f7b&lang=pt_br"

response = requests.get(url)
response = response.json()



if __name__ == '__main__':
    print(response)