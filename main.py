import qrcode
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtGui import QPixmap
from random import choice



class gui(QtWidgets.QWidget):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.show_gui()
    
    def show_gui(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('d.png'))

        self.setFixedSize(660, 330)
        self.setWindowTitle('QrCode Gen')
        self.setStyleSheet("background-color: #999966;")
        
        
        
        self.urlinput = QtWidgets.QTextEdit(self)
        self.urlinput.setFixedSize(200, 40)
        self.urlinput.setStyleSheet("background-color: #000000; color: white; border-radius: 5px; padding: 7px;")
        self.urlinput.setPlaceholderText("URL For The QrCode")
        self.urlinput.setFont(QtGui.QFont('Arial', 12))
        self.urlinput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) 
        self.urlinput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.urlinput.move(165//2, 115//2+50)
        
        
        
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Generate QrCode")
        self.button.setFixedSize(200, 40)
        self.button.setStyleSheet("background-color: #000000; color: white; border-radius: 5px; padding: 7px;")
        self.button.setCursor(QtCore.Qt.PointingHandCursor)
        self.button.setFont(QtGui.QFont('Arial', 12))
        self.button.clicked.connect(self.generate_qrcode)
        
        self.button.move(165//2, 445//2-50)

        self.pic = QtWidgets.QLabel(self)
        self.pic.resize(330, 330)
        self.pic.move(self.width()-330,0)
        self.show()
        self.app.exec_()
    def generate_qrcode(self):
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
        self.url = self.urlinput.toPlainText()
        self.filename = ''.join(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(8))
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="#999966")
        img.save(self.filename)

        self.pic.setPixmap(QPixmap(self.filename))
        os.remove(self.filename)


if __name__ == '__main__': 
    g = gui()
    
    
#add place holders