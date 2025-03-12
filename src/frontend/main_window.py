# src/frontend/main_window.py

import sys
import json
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QToolBar, QAction, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer
from frontend.settings_window import SettingsWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsZap")
        self.setGeometry(100, 100, 800, 600)

        # Criar barra de ferramentas
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # Adicionar ações à barra de ferramentas
        back_action = QAction("Voltar", self)
        back_action.triggered.connect(self.back)
        self.toolbar.addAction(back_action)

        forward_action = QAction("Avançar", self)
        forward_action.triggered.connect(self.forward)
        self.toolbar.addAction(forward_action)

        refresh_action = QAction("Atualizar", self)
        refresh_action.triggered.connect(self.refresh)
        self.toolbar.addAction(refresh_action)

        settings_action = QAction("Configurações", self)
        settings_action.triggered.connect(self.open_settings)
        self.toolbar.addAction(settings_action)

        # Criar WebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://web.whatsapp.com/"))

        # Configurando o layout
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Carregar configurações
        self.settings = self.load_settings()
        
        # Timer para verificar novas mensagens
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_for_new_messages)
        self.timer.start(10000)  # Verifica a cada 10 segundos

    def load_settings(self):
        # Carregar configurações do arquivo JSON
        try:
            with open("config.json", "r") as config_file:
                return json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"notifications_enabled": True}  # Retorna valores padrão

    def back(self):
        self.browser.back()

    def forward(self):
        self.browser.forward()

    def refresh(self):
        self.browser.reload()

    def check_for_new_messages(self):
        self.browser.page().runJavaScript(
            "document.querySelectorAll('span[data-testid=\"msg-notification\"]')",
            self.handle_notification
        )

    def handle_notification(self, notifications):
        if notifications and len(notifications) > 0 and self.settings["notifications_enabled"]:
            QMessageBox.information(self, "Nova Mensagem", "Você tem novas mensagens!")

    def open_settings(self):
        settings_window = SettingsWindow(self, self.settings)
        settings_window.exec_()  # Abre a janela de configurações
