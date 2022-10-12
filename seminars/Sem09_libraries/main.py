# Программа - Прогноз погоды
# ------------------------------------------------------------------------------------------------

import json
import telebot
import requests as req
from geopy import geocoders
from os import environ


token = environ['token_bot']
token_accu = environ['token_accu']
token_yandex = environ['5bca2db9-28b3-43de-9194-aa435607aded'] # token_yandex
