"""Module which sets up logging handler and format."""
import logging.config


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '[%(levelname)s:%(asctime)s] ---  %(message)s'
        },
    },

    'handlers': {
        'debug_console_handler': {
            'level': 'DEBUG',
            'formatter': 'default_formatter',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'info_rotating_file_handler': {
            'level': 'INFO',
            'formatter': 'default_formatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'info.log',
            'mode': 'a',
            'maxBytes': 1048576,
            'backupCount': 10
        },
        'error_file_handler': {
            'level': 'WARNING',
            'formatter': 'default_formatter',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'mode': 'a',
        },
    },

    'loggers': {
        'console': {
            'handlers': ['debug_console_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'info_file': {
            'handlers': ['info_rotating_file_handler', 'debug_console_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'error_file': {
            'handlers': ['error_file_handler', 'debug_console_handler'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}


def setup_logger() -> None:
    """Setup the common logger."""
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger('common')
    logger.debug("Setup logger.")
