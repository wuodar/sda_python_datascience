import logging # paczka pythonowa służąca do logowania przebiegu programu

# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def some_function(arg):
    logger.info(arg)