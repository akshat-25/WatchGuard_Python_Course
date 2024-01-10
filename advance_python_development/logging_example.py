import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.DEBUG,
    datefmt='%d-%m-%Y',
    filename='logs.txt',
    )
logger = logging.getLogger('test_logger')

logger.info('This will not show up')
logger.warning('This will...')
logger.critical("This is critical")
logging.debug("This is debug")

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""