import sys
from typing import Iterable, Optional
import requests
from lxml import html
from start_sploit import get_pivoted_flag_ids
import json
import os
import string
import random

__RANDOM_ALPHABET = string.ascii_letters + string.digits

def random_string(n):
    return ''.join(random.choices(__RANDOM_ALPHABET, k=n))

__default_exploit_name = os.path.basename(sys.argv[0]).removesuffix(".py")
team_ip = sys.argv[1]
__user_agent = None
if len(sys.argv) < 3:
    print("No user agent provided, falling back to requests default, it'll probably be blocked tho", file=sys.stderr, flush=True)
else:
    __user_agent = sys.argv[2]

flag_ids: dict[str, list[str]]

if len(sys.argv) < 4:
    print("No flag ids provided, asking gamesystem")
    flag_ids = get_pivoted_flag_ids().get(team_ip, {})
else:
    flag_ids = json.loads(sys.argv[3])


session: requests.Session


def reset_session():
    global session
    session = requests.Session()
    if __user_agent is not None:
        session.headers.update({
            "User-Agent": __user_agent
        })

reset_session()

def get_text_from_html_css(html_text: str, css_selector: str) -> str:
    return html.fromstring(html_text).cssselect(css_selector)[0].text_content().strip()

def get_text_from_html_xpath(html_text: str, xpath: str) -> str:
    return html.fromstring(html_text).xpath(xpath)[0].text.strip()


def print_flag(flag: str, exploit_name: Optional[str]=None):
    if exploit_name is None:
        exploit_name = __default_exploit_name
    print(f">>{exploit_name}:{flag}", flush=True)

def print_flags(flags: Iterable[str], exploit_name: Optional[str]=None):
    for flag in flags:
        print_flag(flag, exploit_name)

def print_error(*args, **kw_args):
    print(*args, flush=True, file=sys.stderr, **kw_args)