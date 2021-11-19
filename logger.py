import sys
import time


class Logger:

    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w')

    def write(self, message):
        self.console.write(message)
        self.file.write(message)

    def flush(self):
        self.console.flush()
        self.file.flush()

    @staticmethod
    def _log(level, message):
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} [{level}]: {message}")

    @classmethod
    def info(cls, message):
        cls._log('INF', message)

    @classmethod
    def debug(cls, message):
        cls._log('DBG', message)

    @classmethod
    def warning(cls, message):
        cls._log('WRN', message)

    @classmethod
    def error(cls, message):
        cls._log('ERR', message)