# coding=utf-8
from requests import get

from logtf_analyser_cli.utils import exit_and_fail

ENDPOINT = 'https://logs.tf'


def get_search_url():
    return F"{ENDPOINT}/json_search"


def get_log_url(log_id):
    return F"{ENDPOINT}/json/{log_id}"


def search_player(player=None, uploader=None, title=None, limit=1000):
    """
    title	 Title text search
    uploader Uploader SteamID as 64-bit integer
    player   Player SteamID as 64-bit integer
    limit    Number of results to get (Max 1000)
    """

    if not (player or uploader or title):
        exit_and_fail('No params applied to search')

    params = {'limit': limit}
    if player:
        params['player'] = player
    if uploader:
        params['uploader'] = uploader
    if title:
        params['title'] = title

    request = get(get_search_url(), params=params)
    request.raise_for_status()
    return request.json()


def get_log(log_id):
    request = get(get_log_url(log_id))
    request.raise_for_status()
    return request.json()


def raise_for_nocontent(reply):
    if reply.status_code == 204:
        exit_and_fail('No content returned from the server')
