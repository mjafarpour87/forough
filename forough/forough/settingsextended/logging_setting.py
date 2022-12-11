import os
import logging

from ..settings import BASE_DIR

# Get an instance of a logger
logger = logging.getLogger('settings')
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)



# Logging Config
LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_FILE = '/api.log'
LOG_PATH = LOG_DIR + LOG_FILE

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

if not os.path.exists(LOG_PATH):
    f = open(LOG_PATH, 'a').close() #create empty log file
else:
    # f = open(LOG_PATH,"w").close() #clear log file
    f = open(LOG_PATH,'a').close() #clear log file

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'verbose': {
            'format': '%(levelname)s %(filename)s %(funcName)s %(module)s %(name)s %(message)s [PID:%(process)d:%(threadName)s]',
        },
        'brief' : {
            'format': '%(asctime)s  %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',

        },
        'json': {
            '()': 'logging_json.JSONFormatter',
            'fields':{
                "level_name": "levelname",
                "thread_name": "threadName",
                "process_name": "processName"
            }
        },
        
    },
    'handlers': {
        # console logs to stderr
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'django.server': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'briefconsole': {
            'class': 'logging.StreamHandler',
            'formatter': 'brief',
        },
        'jsonconsole' : {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': LOG_PATH ,
        },
       'smtp': {
        'level': 'ERROR',
        'class': 'logging.handlers.SMTPHandler',
        'formatter': 'default',
        'mailhost': ['127.0.0.1', 60025],
        'credentials' : ['u','p'],
        'fromaddr': 'bitaraf.e@iums.ac.ir',
        'toaddrs': ['recipient@example.com'],
        'subject': 'Something went wrong'
      },
      'http': {
        'level': 'DEBUG',
        'class': 'logging.handlers.HTTPHandler',
        'formatter': 'json',
        'host' : '172.18.244.130:9002' , 
        'url': '',
        'secure' : False ,
        'method': 'POST',
      },
    },
    'loggers': {
        # default for all undefined Python modules
        '': {
            'level': 'WARNING',
            'handlers': ['console'],
        },
        'distance_http_log': {
            'level': 'DEBUG',
            'handlers': ['http'],
            # Avoid double logging because of root logger
            'propagate': False,
        },
        # Our application code
        'app': {
            'level': 'DEBUG',
            'handlers': ['django.server'],
            # Avoid double logging because of root logger
            'propagate': False,
        },
        # Default runserver request logging
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['django.server'],
            # Avoid double logging because of root logger
            'propagate': False,
        },
       
    },
}


# for define new logger in other part of project
# from .settings import LOGGING
# import logging
# logging.config.dictConfig(LOGGING)
# logger = logging.getLogger('app')