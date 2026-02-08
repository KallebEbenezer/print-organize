import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from popup import show_popup

SCREENSHOTS_DIR = "/home/ebenezer/Pictures/Screenshots"

class ScreenshotHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.lower().endswith(".png"):
            show_popup(event.src_path)

def start_watcher():
    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, SCREENSHOTS_DIR, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
