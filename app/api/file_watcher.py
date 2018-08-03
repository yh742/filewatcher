from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from app import logger

class FileHandler(FileSystemEventHandler):

    def __init__(self, observer, ret_params):
        super(FileHandler, self).__init__()
        self.observer = observer
        self.params = ret_params

    def process(self, event):
        if not event.is_directory:
            self.params['src_path'] = event.src_path
            self.params['type'] = event.event_type
            self.params['is_dir'] = event.is_directory
            logger.debug(self.params)
            self.observer.stop()

    def on_modified(self, event):
        logger.debug('File modified')
        self.process(event)
    
    def on_created(self, event):
        logger.debug('File created')
        self.process(event)
    

class FileWatcher(object):

    def __init__(self):
        self.watcher = Observer()
        self.params = {}
    
    def watch(self, path):
        self.watcher.schedule(FileHandler(self.watcher, self.params), path=path)
        self.watcher.start()

    def wait(self):
        self.watcher.join()
        logger.debug('Exiting from wait')
        return self.params



