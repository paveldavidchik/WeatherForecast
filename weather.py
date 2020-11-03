
from City import City
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', help='City name')
    att = parser.parse_args()
    city = City(att.city)
    print(city.get_weather())


if __name__ == '__main__':
    run()
