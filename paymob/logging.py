import logging

logger = logging.getLogger("paymob-next")


def log(msg, level, **kwargs):
    getattr(logger, level)(msg, **kwargs)
