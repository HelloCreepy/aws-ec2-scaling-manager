import logging
from functools import wraps

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

logging.basicConfig(
    format='%(asctime)s ~ %(levelname)-10s %(name)-25s %(message)s',
    datefmt='%Y-%m-%d %H:%M', level=DEBUG)  # , filename='*.log')

logging.getLogger('boto3').setLevel(WARNING)
logging.getLogger('botocore').setLevel(WARNING)
logging.getLogger('requests').setLevel(WARNING)
logging.getLogger('urllib3').setLevel(WARNING)

logging.addLevelName(DEBUG, '🐛 DEBUG')
logging.addLevelName(INFO, '📑 INFO')
logging.addLevelName(WARNING, '🤔 WARNING')
logging.addLevelName(ERROR, '🚨 ERROR')
logging.addLevelName(CRITICAL, '💥 CRITICAL')

def get_logger(name):
    return logging.getLogger(name)


def log(level=DEBUG, params=True, result=True):
    def wrapped(func):
        logger = logging.getLogger(func.__module__)

        @wraps(func)
        def inner_wrapped(*args, **kwargs):
            message = f"Calling {func.__name__} "
            if params:
                message += f"with {args} and {kwargs} "
            logger.log(level, message)

            result = func(*args, **kwargs)
            if result:
                message = f"Return {func.__name__} equals {result} "
                logger.log(level, message)

            return result
        return inner_wrapped
    return wrapped
