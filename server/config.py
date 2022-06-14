import json
import requests

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {team["name"]: f"10.60.{id}.1" for (id, team) in enumerate(json.loads(requests.get("http://10.10.0.1/api/game.json").text)["teams"]) if "nop" not in team and "Padova" not in team["name"]},
    'FLAG_FORMAT': r'[A-Z0-9]{31}=',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    # 'SYSTEM_PROTOCOL': 'ructf_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',

    'SYSTEM_PROTOCOL': 'ccit_http',
    'SYSTEM_URL': 'http://10.10.0.1:8080/flags',
    'TEAM_TOKEN': 'ef26fc9047b03c6961b330eb66597f4e',

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
    'SERVER_PASSWORD': 'xdqqrXRqeNK1wpNUfGGej9uvVtcBMOsw',

    # Use authorization for API requests
    'ENABLE_API_AUTH': True,
    'API_TOKEN': 'BsmyF04YhB4l9LWd3adPGXif2sjfVOrH'
}
