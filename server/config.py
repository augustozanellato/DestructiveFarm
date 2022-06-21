import json
import sys
import requests
import os
from server import app

get_ip = lambda id: os.environ["TEAM_IP_PREFIX"] + str(id) + os.environ["TEAM_IP_SUFFIX"]

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {},
    'FLAG_FORMAT': os.environ['FLAG_REGEX'],

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    # 'SYSTEM_PROTOCOL': 'ructf_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',

    'SYSTEM_PROTOCOL': 'ccit_http',
    'SYSTEM_URL': f"http://{os.environ['SCOREBOARD_IP']}:8080/flags",
    'TEAM_TOKEN': os.environ['TEAM_TOKEN'],

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'your_secret_token',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 100,
    'SUBMIT_PERIOD': 1,
    'FLAG_LIFETIME': 10 * 60,  # 10 minutes

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': os.environ['DESTRUCTIVEFARM_PASSWORD'],

    # Use authorization for API requests
    'ENABLE_API_AUTH': True,
    'API_TOKEN': 'BsmyF04YhB4l9LWd3adPGXif2sjfVOrH'
}
try:
    CONFIG['TEAMS'].update({team["logo"]: get_ip(id) for (id, team) in enumerate(json.loads(requests.get(f"http://{os.environ['SCOREBOARD_IP']}/api/game.json", timeout=1).text)["teams"]) if "nop" not in team and "Padova" not in team["name"]})
except Exception as e:
    app.logger.error(f"Exception while fetching teams from scoreboard: {e}")
    app.logger.error(f"Falling back to default teams")
    CONFIG['TEAMS'].update({f"team{id:02}": get_ip(id) for id in range(1, 40)})
