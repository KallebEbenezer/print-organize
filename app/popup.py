from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import shutil
from models import Area

BASE_SAVE_DIR = "/home/ebenezer/Documents/QUESTOES"

class Popup(QWidget):

    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path
        self.setWindowTitle("Salvar print em:")

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Escolha a área:"))

        for area_id, name in Area.list_all():
            btn = QPushButton(name)
            btn.clicked.connect(lambda _, n=name: self.save(n))
            layout.addWidget(btn)

    def save(self, area_name):
        dest = f"{BASE_SAVE_DIR}/{area_name}"
        shutil.move(self.file_path, dest)
        self.close()
