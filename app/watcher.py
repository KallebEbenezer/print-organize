import time
from watchdog.events import FileSystemEventHandler
from PySide6.QtCore import QObject, Signal

class ScreenshotSignal(QObject):
    screenshot_ready = Signal(str)

signal_bus = ScreenshotSignal()

class ScreenshotHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_event = {}

    def on_modified(self, event):
        if event.is_directory:
            return

        if not event.src_path.lower().endswith((".png", ".jpg", ".jpeg")):
            return

        now = time.time()
        last_time = self.last_event.get(event.src_path, 0)

        if now - last_time < 1:
            return

        self.last_event[event.src_path] = now

        time.sleep(0.5)

        signal_bus.screenshot_ready.emit(event.src_path)
