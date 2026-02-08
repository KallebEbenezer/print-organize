import sys
from PySide6.QtWidgets import QApplication
from database import init_db
from ui.areas_view import AreasView

if __name__ == "__main__":
    init_db()

    app = QApplication(sys.argv)
    window = AreasView()
    window.show()
    sys.exit(app.exec())