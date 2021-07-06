from PySide2.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.tela_login()
        self.label_botoes()


    def tela_login(self):
        self.setWindowTitle('Tela de Login')
        self.setGeometry(500, 150, 400, 500)
        self.setMaximumSize(400, 500)
        self.setMinimumSize(400, 500)
        self.setToolTip('Tela de Login')
        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color:#00beb0')


    def label_botoes(self):
        self.bt1 = QPushButton('Login', self)
        self.bt1.setGeometry(170, 300, 121, 51)
        self.bt1.setStyleSheet('background-color: rgb(46, 255, 242); border-color: black; border-style: outset; border-width: 2px; border-radius: 15px')
        


tela = QApplication(sys.argv)

janela = App()
janela.show()
tela.exec_()
sys.exit()
