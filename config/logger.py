# import logging

# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

# handler =  logging.FileHandler('myapp.log')
# handler.setFormatter(logging.Formatter(
#     '%(levelname)s:%(name)s     %(message)s'
# ))
# handler.setLevel(logging.INFO)

# log.addHandler(handler)
# log.addHandler(logging.StreamHandler())

# log.debug('Debug message')
# log.info('Info message')
# log.warning('Warning message')

from loguru import logger

logger.add('myapp.log', format='{time} {level} {message}',
level='DEBUG', rotation='5 MB')

logger.debug("hello")
logger.info("hello")
logger.error("hello")