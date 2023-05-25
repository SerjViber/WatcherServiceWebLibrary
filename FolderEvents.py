# FolderEvent.py

from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    
    def __init__(self) -> None:
        super().__init__()
        self.fileslog = 'C:\\Log\\log.txt'
        with open(self.fileslog, 'a', encoding="utf-8") as f:
            f.writelines('Start logging\n')
            f.close()
        return

    def on_created(self, event):
        self.strOutput = 'Event '+ event.event_type + ' file '+event.src_path + '\n'
        with open(self.fileslog, 'a', encoding="utf-8") as e:
            e.writelines(self.strOutput)
            e.close()
        return

    def on_deleted(self, event1):
        self.strOutput = 'Event '+ event1.event_type + ' file '+event1.src_path + '\n'
        with open(self.fileslog, 'a', encoding="utf-8") as g:
            g.writelines(self.strOutput)
            g.close()
        return

    def on_moved(self, event2):
        self.strOutput = 'Event '+ event2.event_type + ' file '+event2.src_path + ' where '+ event2.dest_path + '\n'
        with open(self.fileslog, 'a', encoding="utf-8") as h:
            h.writelines(self.strOutput)
            h.close()
        return