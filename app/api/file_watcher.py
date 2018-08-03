import threading

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from app import logger

class FileHandler(FileSystemEventHandler):

    def __init__(self, changed_event, ret_params):
        super(FileHandler, self).__init__()
        self.changed_event = changed_event
        self.params = ret_params

    def process(self, event):
        if not event.is_directory:
            self.params['src_path'] = event.src_path
            self.params['type'] = event.event_type
            self.params['is_dir'] = event.is_directory
            logger.debug(self.params)
            self.changed_event.set()

    def on_modified(self, event):
        logger.debug('File modified')
        self.process(event)
    
    def on_created(self, event):
        logger.debug('File created')
        self.process(event)
    

class FileWatcher(object):

    def __init__(self):
        self.watcher = Observer()
        self.changed_event = threading.Event()
        self.params = {}
    
    def watch(self, path):
        self.watcher.schedule(FileHandler(self.changed_event, self.params), path=path)
        self.watcher.start()

    def stop(self):
        self.watcher.stop()
    
    def reset(self):
        self.changed_event.clear()

    def wait(self):
        self.changed_event.wait()
        logger.debug('Exiting from wait')
        return self.params



