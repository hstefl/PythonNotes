"""
https://edube.org/learn/pcpp1-5/lab-xml-lab-1
"""

import xml.etree.ElementTree


class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(in_c):
        return round(9 / 5 * in_c + 32, 2)


class ForecastXmlParser:
    DAY = 0
    TEMPERATURE = 1

    def __init__(self, file):
        self.loadedXml = xml.etree.ElementTree.parse(file)

    def parse(self):
        for items in self.loadedXml.getroot():
            day = items[ForecastXmlParser.DAY].text
            in_c = items[ForecastXmlParser.TEMPERATURE].text
            in_f = TemperatureConverter.convert_celsius_to_fahrenheit(int(in_c))

            print(f'{day}: {in_c} Celsius, {in_f} Fahrenheit')


ForecastXmlParser('forecast.xml').parse()
