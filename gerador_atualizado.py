import sys
from config.interface import *
from config.gerador import Repositorio
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class Relatorio(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QtGui.QIcon('imagens/icone.ico'))

        self.btnEscolherArquivo.clicked.connect(self.abrir_arquivo)
        self.btnGerarRelatorio.clicked.connect(self.gera_arquivo)

    def abrir_arquivo(self):
        self.texto, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Texto',
            'C:/',
        )
        self.inputAbrirArquivo.setText(self.texto)
        with open(self.texto, 'r') as usuarios:
            self.labeltxt.setText(usuarios.read())

    def gera_arquivo(self):
        gerar = Repositorio(self.texto)
        gerar.open_file()
        gerar.b_to_mb()
        gerar.repositorio_file()

        relatorio_criado = r'C:\Users\Gabriel\Desktop\repositorio.txt',

        with open(r'..\relatorio.txt', 'r') as relatorio:
            self.labeltxt.setText(relatorio.read())




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    relatorio = Relatorio()
    relatorio.show()
    qt.exec()