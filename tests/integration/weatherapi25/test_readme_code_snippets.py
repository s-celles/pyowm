#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
from pyowm.config import DEFAULT_CONFIG


class IntegrationTestsREADMESnippets(unittest.TestCase):

    __API_key = os.getenv('OWM_API_KEY', DEFAULT_CONFIG['api_key'])

    def test_free_subscription_snippets(self):

        import pyowm
        from pyowm.weatherapi25.weather import Weather

        owm = pyowm.OWM(self.__API_key)  # You MUST provide a valid API key

        # Search for current weather in London (Great Britain)
        observation = owm.weather_at_place('London,GB')
        w = observation.get_weather()
        self.assertIsInstance(w, Weather)

        # Weather details
        w.get_wind()
        w.get_humidity()
        w.get_temperature('celsius')

        # Search current weather observations in the surroundings of
        # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
        observation_list = owm.weather_around_coords(-22.57, -43.12)
        self.assertIsInstance(observation_list, list)


if __name__ == '__main__':
    unittest.main()
