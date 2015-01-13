import os
import json
import aiohttp


def get_api_key():
    with open(os.path.expanduser("~/.wmata.key"), 'r') as fd:
        fskey = fd.read().strip()
    key = os.environ.get("WMATA_API_KEY", fskey)
    return key


API_KEY = get_api_key()


def get_json(service, path, params):
    url = "http://api.wmata.com/{}.svc/json/{}".format(service, path)
    url += "?api_key={}".format(API_KEY)
    response = yield from aiohttp.request('GET', url)
    return json.loads((yield from response.read()).decode('utf-8'))
