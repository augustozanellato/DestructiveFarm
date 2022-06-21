import requests

from server import app, stats
from server.models import FlagStatus, SubmitResult


RESPONSES = {
    FlagStatus.QUEUED: [],
    FlagStatus.ACCEPTED: ['accepted'],
    FlagStatus.REJECTED: ['own', 'too old', 'nop', 'invalid'],
}


TIMEOUT = 5

def match_flag(flag, flags):
    for item in flags:
        if flag == item.flag:
            return item
    return None

def submit_flags(flags, config):
    r = requests.put(config['SYSTEM_URL'],
                     headers={'X-Team-Token': config['TEAM_TOKEN']},
                     json=[item.flag for item in flags], timeout=TIMEOUT)

    unknown_responses = set()
    with stats.pipeline() as pipe:
        for item in r.json():
            response = item['msg'].strip()
            response = response.replace('[{}] '.format(item['flag']), '')

            response_lower = response.lower()
            for status, substrings in RESPONSES.items():
                if any(s in response_lower for s in substrings):
                    found_status = status
                    break
            else:
                found_status = FlagStatus.QUEUED
                if response not in unknown_responses:
                    unknown_responses.add(response)
                    app.logger.warning('Unknown checksystem response (flag will be resent): %s', response)
            orig_flag = match_flag(item['flag'], flags)
            if orig_flag is not None:
                pipe.incr(f'df.flag_out.{orig_flag.team}.{orig_flag.sploit.replace(".py", "").replace(".", "")}.{found_status.name}')
            else:
                pipe.incr(f'df.flag_out.unmatched.unmatched.{found_status.name}')
            yield SubmitResult(item['flag'], found_status, response)
