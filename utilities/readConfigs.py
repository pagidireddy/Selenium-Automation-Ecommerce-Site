import os
import configparser
import random
current_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(current_dir, '..', 'Configurations', 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getUrl():
        return config.get('Settings', 'url')
    @staticmethod
    def get_random_product():
        products = config['Settings']['products'].split(', ')
        return random.choice(products)

    @staticmethod
    def get_random_min_price():
        minprice = config['Settings']['minprice'].split(', ')
        return random.choice(minprice)

    @staticmethod
    def get_random_max_price():
        maxprice = config['Settings']['maxprice'].split(', ')
        return random.choice(maxprice)
