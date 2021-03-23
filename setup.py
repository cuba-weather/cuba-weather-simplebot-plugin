# -*- coding: utf-8 -*-
import re

from setuptools import setup


MODULE_NAME = 'simplebot_cubaweather'
with open(MODULE_NAME + '.py', 'rt', encoding='utf8') as fh:
    VERSION = re.search(
        r'__version__ = \'(.*?)\'', fh.read(), re.M).group(1)

setup(
    name=MODULE_NAME,
    version=VERSION,
    author='The SimpleBot Contributors',
    author_email='correaleyval@gmail.com, adbenitez@nauta.cu',
    description='Cuba Weather plugin for SimpleBot (https://github.com/simplebot-org/simplebot), a Delta Chat bot (http://delta.chat/)',
    long_description='For more info visit https://github.com/simplebot-org/simplebot and https://github.com/cuba-weather',
    long_description_content_type='text/x-rst',
    url='https://github.com/cuba-weather/cuba-weather-simplebot-plugin',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    keywords='deltachat simplebot plugin cuba-weather',
    py_modules=[MODULE_NAME],
    install_requires=['simplebot', 'cuba-weather'],
    python_requires='>=3.6',
    entry_points={
        'simplebot.plugins': '{0} = {0}'.format(MODULE_NAME)
    },
    include_package_data=True,
    zip_safe=False,
)
