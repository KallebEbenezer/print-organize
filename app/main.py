import sys
import threading
import time
from PySide6.QtWidgets import QApplication
from watchdog.observers import Observer

from database import init_db
from watcher import ScreenshotHandler, signal_bus
from popup import Popup

SCREENSHOTS_DIR = "/home/ebenezer/Pictures/Screenshots"

def start_watcher():
    try:
        observer = Observer()
        observer.schedule(ScreenshotHandler(), SCREENSHOTS_DIR, recursive=False)
        observer.start()
        print("Watcher staretd in:", SCREENSHOTS_DIR)

        while True:
            time.sleep(1)
    
    except Exception as e:
        print("Error in watcher thread:" e)

if __name__ == "__main__":
    init_db()

    app = QApplication(sys.argv)

    def open_popup(path):
        popup = Popup(path)
        popup.show()

    signal_bus.screenshot.connect(open_popup)

    watcher_thread = threading.Thread(target=start_watcher, daemon=True)
    watcher_thread.start()

    sys.exit(app.exec())
