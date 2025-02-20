
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsZap")
        self.setGeometry(100, 100, 600, 400)  # Posição x, y e tamanho largura, altura

        label = QLabel("Bem-vindo ao WhatsZap!", self)
        label.setGeometry(200, 150, 200, 50)  # Posição e tamanho do label

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
