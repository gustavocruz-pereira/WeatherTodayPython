from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys
from PyQt5.QtGui import QPixmap
from apiweather import get_response, get_temp, get_latLon


def search_city(c):
    cidade = txtbx.text()
    result = get_response(cidade)
    return result

def on_button_clicked():
    result = search_city(txtbx.text())
    try:
        r, t, m = result
        lbl_weather.setText(f'{r.capitalize()}') 
        lbl_temp.setText(f'{t} °C')
        insert_png(m)
    except:
        print('Erro durante o processo')


def insert_png(desc):
    lbl_icone.setVisible(True)
    if desc == 'Clouds':
        pixmap = QPixmap('img/clouds.png')
    elif desc == 'Clear':
        pixmap = QPixmap('img/sun.png')
    elif desc == 'Rain':
        pixmap = QPixmap('img/rain.png')
    elif desc == 'Mist':
        pixmap = QPixmap('img/mist.png')
    elif desc == 'Snow': 
        pixmap = QPixmap('img/snowflake.png')
    
    lbl_icone.setPixmap(pixmap)

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Weather Today')
window.setFixedSize(450, 400)

txtbx = QLineEdit('...', parent=window)
txtbx.setGeometry(20, 35, 360, 30)

btn = QPushButton('Pesquisar cidade', parent=window)
btn.setGeometry(20, 75, 200, 30)

lbl_weather = QLabel('Teste', parent=window)
lbl_weather.move(20, 120)

lbl_temp = QLabel('Graus', parent=window)
lbl_temp.move(20, 140)


lbl_icone = QLabel(parent=window)
lbl_icone.setGeometry(110, 140, 250, 250)

lbl_icone.setVisible(False)

btn.clicked.connect(on_button_clicked)

if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())
