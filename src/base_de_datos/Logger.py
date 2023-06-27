import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s]%(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('data_layer.log'),
                    log.StreamHandler()
                ])

if __name__=='__main__':
    log.debug('Debug level log')
    log.info('Info level log')
    log.warning('Warning level log')
    log.error('Error level log')
    log.critical('Critical level log')