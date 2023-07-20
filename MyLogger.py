import logging

class MyLogger:

    FORMAT = '%(clientip)-15s %(message)s'
    # logging.basicConfig(format=FORMAT)
    handler = logging.FileHandler('app.log', 'w', 'utf-8')
    logger = logging.getLogger('taskStudent')
    logger.setLevel('WARNING')
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)