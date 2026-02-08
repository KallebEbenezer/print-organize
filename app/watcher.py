from watchdog.events import FileSystemEventHandler
from PySide6.QtCore import QObject, Signal
import traceback

class ScreenshotSignal(QObject):
    screenshot = Signal(str)

signal_bus = ScreenshotSignal()

class ScreenshotHandler(FileSystemEventHandler):

    def on_created(self, event):
        try:
            print("EVENTO DETECTADO:", event.src_path)

            if event.is_directory:
                return

            if event.src_path.lower().endswith(".png"):
                print("PRINT DETECTADO")
                signal_bus.screenshot.emit(event.src_path)

        except Exception:
            print("ERRO NO WATCHER:")
            traceback.print_exc()
