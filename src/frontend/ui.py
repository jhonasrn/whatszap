# src/frontend/ui.py

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys
from .whatsapp_actions import WhatsAppActions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl("https://web.whatsapp.com/"))

        # Inicializando a classe WhatsAppActions
        self.whatsapp_actions = WhatsAppActions(self.browser)
        # Chama a função para listar as conversas após a página carregar
        self.browser.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            self.whatsapp_actions.list_conversations()  # Lista as conversas após o carregamento

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
