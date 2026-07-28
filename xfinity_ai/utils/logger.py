import logging


class Logger:

    def __init__(self):
        self.logger = logging.getLogger("XfinityAI")

        self.logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "[%(levelname)s] %(message)s"
        )

        handler.setFormatter(formatter)

        self.logger.addHandler(handler)


    def info(self, message):
        self.logger.info(message)


    def error(self, message):
        self.logger.error(message)


    def warning(self, message):
        self.logger.warning(message)
