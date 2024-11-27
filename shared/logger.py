import logging

class Logger:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.setup_logger() 
        return cls._instance

    @staticmethod
    def setup_logger():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

    @staticmethod
    def log(message):
        logging.info(message)
