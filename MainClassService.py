# MainClassService.py
import socket
import servicemanager
import win32serviceutil
import win32event
import win32service
import win32timezone


class WSWLservice(win32serviceutil.ServiceFramework):
    '''Base class to create WatcherService in Python'''

    _svc_name_ = 'WatcherService'
    _svc_display_name_ = 'Watcher Service for Web Library'
    _svc_description_ = 'Выгрузка измененных файлов в Web библиотеку'

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        '''
        Constructor of the WatcherService
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Вызов когда службе передают команду stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Вызов когда службе передают команду start
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                            servicemanager.PYS_SERVICE_STARTED,
                            (self._svc_name_, ''))
        self.main()

    def start(self):
        '''
        Override to add logic before the start eg. running condition
        '''
        pass

    def stop(self):
        '''
        Override to add logic before the stop eg. invalidating running condition
        '''
        pass

    def main(self):
        '''
        Main class to be ovverridden to add logic
        '''
        pass


# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
    WSWLservice.parse_command_line()