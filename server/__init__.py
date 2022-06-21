import logging

from flask import Flask
from statsd import StatsClient


stats = StatsClient(host='telegraf', port=8125)
app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)
for handler in app.logger.handlers:
    handler.setLevel(logging.DEBUG)


import server.api
import server.views
