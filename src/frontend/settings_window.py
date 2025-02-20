# src/frontend/settings_window.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QCheckBox, QPushButton
import json

class SettingsWindow(QDialog):
    def __init__(self, parent=None, settings=None):
        super().__init__(parent)
        self.setWindowTitle("Configurações")
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout()

        self.notification_checkbox = QCheckBox("Habilitar notificações")
        self.notification_checkbox.setChecked(settings["notifications_enabled"])  # Carregar configuração
        layout.addWidget(self.notification_checkbox)

        save_button = QPushButton("Salvar")
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_settings(self):
        # Salvar configurações
        settings = {
            "notifications_enabled": self.notification_checkbox.isChecked()
        }
        with open("config.json", "w") as config_file:
            json.dump(settings, config_file)
        self.accept()  # Fecha a janela de configurações
