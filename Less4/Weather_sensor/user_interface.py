import data_provider
import logger

def temperature_view(sensor):
    data = data_provider.get_temperature(sensor)
    logger.temperature_logger(data)
    return data

def preasure_view(sensor):
    data = data_provider.get_preasure(sensor)
    logger.preasure_logger(data)
    return data

def wind_speed_view(sensor):
    data = data_provider.get_wind_speed(sensor)
    logger.wind_speed_logger(data)
    return data