import sys
from typing import Iterable
import requests
from lxml import html

exploit_name = sys.argv[0]
team_ip = sys.argv[1]
user_agent = None
if len(sys.argv) < 3:
    print("No user agent provided, falling back to requests default, it'll probably be blocked tho", file=sys.stderr, flush=True)
else:
    user_agent = sys.argv[2]

session: requests.Session


def reset_session():
    global session
    session = requests.Session()
    if user_agent is not None:
        session.headers.update({
            "User-Agent": user_agent
        })

reset_session()

def get_text_from_html_css(html_text: str, css_selector: str) -> str:
    return html.fromstring(html_text).cssselect(css_selector)[0].text_content().strip()

def get_text_from_html_xpath(html_text: str, xpath: str) -> str:
    return html.fromstring(html_text).xpath(xpath)[0].text.strip()

def print_flag(exploit_name: str, flag: str):
    print(f">>{exploit_name}:{flag}", flush=True)

def print_flags(exploit_name: str, flags: Iterable[str]):
    for flag in flags:
        print_flag(exploit_name, flag)