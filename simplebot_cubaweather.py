"""
Search weather info using cuba-weather from redcuba.cu
"""

import simplebot
from cuba_weather import RCApiClient

__version__ = '1.0.0'
template = '\n\n'.join((
    '🌐 {}',
    '📅 {}',
    '⛅ Estado: {}',
    '🌡 Temperatura: {}°C',
    '💧 Humedad: {}%',
    'Presión atmosférica: {} hpa',
    '🌬 Vientos:\n{}',
))


@simplebot.command
def cuwtr(payload, replies):
    """Buscar información del estado del tiempo en Cuba usando cuba-weather de redcuba.cu"""
    if not payload:
        replies.add(
            text='Envíame una localidad de Cuba, ej.: /cuwtr Santiago')
    else:
        api = RCApiClient()

        weather = api.get(payload, suggestion=True)

        replies.add(
            text=template.format(
                weather.city_name,
                weather.timestamp,
                weather.general,
                weather.temperature,
                weather.humidity,
                weather.pressure,
                weather.wind,
            )
        )


class TestCuwtr:
    def test_cuwtr(self, mocker):
        msg = mocker.get_one_reply('/cuwtr')
        assert 'Envíame una localidad' in msg.text

        msg = mocker.get_one_reply('/cuwtr Santiago')
        assert 'Temperatura:' in msg.text
