from watchdog.events import FileSystemEventHandler
from PySide6.QtCore import QObject, Signal

class ScreenshotSignal(QObject):
    screenshot = Signal(str)

signal_bus = ScreenshotSignal()

class ScreenshotHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.lower().endswith(".png"):
            signal_bus.screenshot.emit(event.src_path)
