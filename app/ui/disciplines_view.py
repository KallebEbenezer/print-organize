from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QInputDialog,
    QMessageBox
)

from models import Discipline

class DisciplinesView(QWidget):

    def __init__(self, area_id: int, area_name: str):
        super().__init__()
        self.area_id = area_id

        self.setWindowTitle(f"Disciplinas — {area_name}")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        buttons = QHBoxLayout()

        add_btn = QPushButton("Adicionar")
        del_btn = QPushButton("Remover")

        buttons.addWidget(add_btn)
        buttons.addWidget(del_btn)

        layout.addLayout(buttons)

        add_btn.clicked.connect(self.add_discipline)
        del_btn.clicked.connect(self.remove_discipline)

        self.load()

    def load(self):
        self.list_widget.clear()
        for d_id, name, path in Discipline.list_by_area(self.area_id):
            label = f"{d_id} - {name}"
            if path:
                label += f" | {path}"
            self.list_widget.addItem(label)

    def add_discipline(self):
        name, ok = QInputDialog.getText(
            self,
            "Nova disciplina",
            "Nome da disciplina:"
        )

        if ok and name.strip():
            Discipline.create(self.area_id, name.strip())
            self.load()

    def remove_discipline(self):
        item = self.list_widget.currentItem()
        if not item:
            return

        discipline_id = int(item.text().split(" - ")[0])

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            "Remover esta disciplina?"
        )

        if confirm == QMessageBox.Yes:
            Discipline.delete(discipline_id)
            self.load()
