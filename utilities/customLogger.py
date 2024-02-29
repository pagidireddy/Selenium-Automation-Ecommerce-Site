import logging
import os


class LogGenerator:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__file__)
        logger.setLevel(logging.INFO)
        try:
            handler = logging.FileHandler(".\\Logs\\automation.log")
        except:
            handler = logging.FileHandler(os.path.dirname(os.getcwd())+"\\Logs\\automation.log")
        handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        logger.addHandler(handler)
        return logger
