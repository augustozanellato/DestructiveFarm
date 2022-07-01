import requests

def get_pivoted_flag_ids() -> dict[str, dict[str, list[str]]]:
    ids = requests.get("http://10.10.0.1:8081/flagIds").json()
    pivoted: dict[str, dict[str, list[str]]] = {}
    for service in ids:
        for team in ids[service]:
            if team not in pivoted:
                pivoted[team] = {}
            pivoted[team][service] = ids[service][team]
    return pivoted