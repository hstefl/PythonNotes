"""
https://edube.org/learn/pcpp1-5/logging-lab-01
"""
import logging
from logging import FileHandler, Formatter
from random import randint
from time import sleep

#FORMAT="%(levelname)s = %(message)s"
#logging.basicConfig(level=logging.DEBUG, filename='battery_temperature.log', filemode='a', format=FORMAT)

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

file_handler = FileHandler(filename='batter_temperature.log', mode='a')
file_handler.setLevel(level=logging.DEBUG)

formatter = Formatter(fmt="%(levelname)s = %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def get_temperature():
    return randint(20, 40)

def check_temperature():
    current_temp = get_temperature()

    if current_temp < 25:
        logger.debug(f'temperature {current_temp}')
    elif 25 <= current_temp < 35:
        logger.info(f'temperature {current_temp}')
    else:
        logger.critical(f'temperature {current_temp}')


while True:
    check_temperature()
    sleep(1)