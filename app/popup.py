from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)
import sys
import shutil
from models import Area

BASE_SAVE_DIR = "/home/ebenezer/Documents/QUESTOES"

def show_popup(file_path: str):
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Salvar print em:")

    layout = QVBoxLayout(window)
    layout.addWidget(QLabel("Escolha a área:"))

    areas = Area.list_all()

    for area_id, name in areas:
        btn = QPushButton(name)

        def handler(_, area=name):
            dest = f"{BASE_SAVE_DIR}/{area}"
            shutil.move(file_path, dest)
            window.close()

        btn.clicked.connect(handler)
        layout.addWidget(btn)

    window.show()
    app.exec()
