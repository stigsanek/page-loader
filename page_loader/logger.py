import logging.config

CONFIG = {
    "version": 1,
    "formatters": {
        "consoled": {
            "format": "%(asctime)s :: %(levelname)s :: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "consoled"
        },
    },
    "loggers": {
        __name__: {
            "handlers": ["console"],
            "level": "DEBUG",
        }
    }
}

logging.config.dictConfig(CONFIG)
log = logging.getLogger(__name__)
