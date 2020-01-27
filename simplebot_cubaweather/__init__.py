# -*- coding: utf-8 -*-
import gettext
import os

from simplebot import Plugin, PluginCommand
from cuba_weather import RCApiClient

res_msg ="""
🌐 {0}\n
📅 {6}\n
{1}\n
🌡 Temperatura: {2}°C\n
💧 Humedad: {3}%\n
Presión atmosférica: {4} hpa\n
🌬 Vientos: \n
{5}
"""

class CubaWeather(Plugin):

    name = 'CubaWeather'
    version = '0.1.0'

    @classmethod
    def activate(cls, bot):
        super().activate(bot)

        localedir = os.path.join(os.path.dirname(__file__), 'locale')
        lang = gettext.translation('simplebot_cubaweather', localedir=localedir,
                                   languages=[bot.locale], fallback=True)
        lang.install()
        cls.description = _('Search weather info using cuba-weather from redcuba.cu')
        cls.commands = [
            PluginCommand('/cuwtr', ['[text]'], _('Search weather info using cuba-weather from redcuba.cu'), cls.cuwtr_cmd)]
        cls.bot.add_commands(cls.commands)

    @classmethod
    def cuwtr_cmd(cls, ctx):
        chat = cls.bot.get_chat(ctx.msg)

        if not ctx.text:
            chat.send_text('Send me a cuban location ej: /cuwtr Santiago')
        else:
            api = RCApiClient()

            weather = api.get(ctx.text, suggestion=True)

            chat.send_text(
                res_msg.format(
                    weather.city_name,
                    gemoji + ' ' + weather.general,
                    weather.temperature,
                    weather.humidity,
                    weather.pressure,
                    weather.wind,
                    weather.timestamp
                )
            )
