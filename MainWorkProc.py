
# MainWorkProc.py
import random
import time
import sys
import servicemanager


from pathlib import Path
from MainClassService import WSWLservice 
from FolderEvents import Handler
from watchdog.observers import Observer


class WatcherServiceWebLibrary(WSWLservice):
    _svc_name_ = 'WatcherService'
    _svc_display_name_ = 'Watcher Service for Web Library'
    _svc_description_ = 'Выгрузка измененных файлов в Web библиотеку'
    _observer: Observer = None
    _handler: Handler = None

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False
        
    def main(self):
        self._handler = Handler()
        self._observer = Observer()
        self._observer.schedule(self._handler, path='C:\\Log\\Temp', recursive=True)
        self._observer.start()
        while self.isrunning:
            time.sleep(0.1)

        self._observer.stop()        
        self._observer.join()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(WatcherServiceWebLibrary)
        servicemanager.StartServiceCtrlDispatcher()
        
    else:
        WatcherServiceWebLibrary.parse_command_line()
        

