import sys
import threading
import time
from PySide6.QtWidgets import QApplication
from watchdog.observers import Observer

from database import init_db
from watcher import ScreenshotHandler, signal_bus
from popup import Popup

SCREENSHOTS_DIR = "/home/ebenezer/Pictures/Screenshots"

class PopupManager:
    def __init__(self):
        self.queue = []
        self.active = False

    def enqueue(self, path):
        self.queue.append(path)
        self.process()

    def process(self):
        if self.active or not self.queue:
            return

        self.active = True
        path = self.queue.pop(0)

        self.popup = Popup(path)
        self.popup.destroyed.connect(self.on_close)
        self.popup.show()

    def on_close(self):
        self.active = False
        self.process()

def start_watcher():
    observer = Observer()
    observer.schedule(ScreenshotHandler(), SCREENSHOTS_DIR, recursive=False)
    observer.start()
    print("Watcher ativo:", SCREENSHOTS_DIR)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    init_db()

    app = QApplication(sys.argv)

    manager = PopupManager()
    signal_bus.screenshot_ready.connect(manager.enqueue)

    watcher_thread = threading.Thread(
        target=start_watcher,
        daemon=True
    )
    watcher_thread.start()

    sys.exit(app.exec())
