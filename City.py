import requests


class City:
    """Класс, представляющий город"""
    _apikey = '94b1a9588c11982d1a1e215562a10960'

    def __init__(self, name: str):
        self._name = name
        self._city_id = self._get_id()

    @property
    def name(self):
        return self._name

    @property
    def city_id(self):
        return self._city_id

    def __str__(self) -> str:
        return f'Город: {self._name}\tid: {self._city_id}'

    def _get_id(self) -> int:
        info = requests.get('http://api.openweathermap.org/data/2.5/find',
                            params={'q': self._name, 'type': 'like', 'units': 'metric', 'APPID': City._apikey}).json()
        return info['list'][0]['id']

    def get_weather(self) -> str:
        info = requests.get('http://api.openweathermap.org/data/2.5/weather',
                            params={'id': self._city_id, 'units': 'metric', 'lang': 'ru',
                                    'APPID': City._apikey}).json()
        weather = f'Сейчас:\n' \
                  f'{info["main"]["temp"] if info["main"]["temp"] <= 0 else ("+" + str(info["main"]["temp"]))} {info["weather"][0]["description"]}\n' \
                  f'Ощущается {info["main"]["feels_like"] if info["main"]["feels_like"] <= 0 else ("+" + str(info["main"]["feels_like"]))}\n' \
                  f'Влажность {info["main"]["humidity"]}%\n' \
                  f'Давление {info["main"]["pressure"]}гПа\n' \
                  f'Ветер {info["wind"]["speed"]}м/с'
        return weather
