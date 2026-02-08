from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QInputDialog,
    QMessageBox
)

from models import Area

class AreasView(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Áreas de Questões")
        self.resize(400, 300)

        self.layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        buttons_layout = QHBoxLayout()

        self.add_button = QPushButton("Adicionar Área")
        self.remove_button = QPushButton("Remover Área")

        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.remove_button)

        self.layout.addLayout(buttons_layout)

        self.add_button.clicked.connect(self.add_area)
        self.remove_button.clicked.connect(self.remove_area)

        self.load_areas()

    def load_areas(self):
        self.list_widget.clear()
        areas = Area.list_all()

        for area_id, name in areas:
            self.list_widget.addItem(f"{area_id} - {name}")

    def add_area(self):
        name, ok = QInputDialog.getText(
            self,
            "Nova Área",
            "Nome da área:"
        )

        if ok and name.strip():
            Area.create(name.strip())
            self.load_areas()

    def remove_area(self):
        item = self.list_widget.currentItem()

        if not item:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma área para remover."
            )
            return

        area_id = int(item.text().split(" - ")[0])

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            "Deseja remover esta área?"
        )

        if confirm == QMessageBox.Yes:
            Area.delete(area_id)
            self.load_areas()
