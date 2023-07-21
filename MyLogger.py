import logging, inspect

class MyLogger:
    logger: logging.Logger = None
    
    @staticmethod
    def configure():
        FORMAT = '%(clientip)-15s %(name)-4s %(message)s'
        # logging.basicConfig(format=FORMAT)
        logger_name = inspect.stack()[1][3]
        handler = logging.FileHandler('app.log', 'w', 'utf-8')
        logger = logging.getLogger('taskStudent')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        MyLogger.logger = logger
   