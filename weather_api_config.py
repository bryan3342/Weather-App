import requests
from tkinter import *

api_key = 'd7ee11bdee9e375fe2eaba56f73dbcb5'


def api_config(user_input):
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q='
                                f'{user_input}&units=imperial&APPID={api_key}')
    if user_input == "":
        return False
    else:

        if weather_data.json()['cod'] == '404':
            return False
        else:
            return True


def climate(user_input):
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q='
                                f'{user_input}&units=imperial&APPID={api_key}')
    return weather_data.json()['weather'][0]['main']


def temperature(user_input):
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q='
                                f'{user_input}&units=imperial&APPID={api_key}')
    return round(weather_data.json()['main']['temp'])



