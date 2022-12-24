from datetime import datetime
from time import time

def temperature_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                   .format(time, data))

def preasure_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};preasure;{}\n'
                   .format(time, data))

def wind_speed_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                   .format(time, data))