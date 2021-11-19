import sys

from logger import Logger


LOG_FILE = 'foo.log'


if __name__ == '__main__':
    sys.stdout = Logger(LOG_FILE)
    Logger.info('Script started...')
    Logger.debug('Some debug info')
    Logger.warning('Some useful VARS are not set')
    Logger.error('Some error')
    Logger.info('Script stopped!')
