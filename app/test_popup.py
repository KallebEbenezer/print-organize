# app/test_popup.py
import sys
from PySide6.QtWidgets import QApplication
from popup import Popup

app = QApplication(sys.argv)
p = Popup("/tmp/test.png")
p.show()
sys.exit(app.exec())
