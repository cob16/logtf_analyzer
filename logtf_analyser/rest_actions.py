# coding=utf-8
from requests import get
import logging

ENDPOINT = 'https://logs.tf'


def get_search_url():
    return f"{ENDPOINT}/json_search"


def get_log_url(log_id):
    return f"{ENDPOINT}/json/{log_id}"


def search_logs(player=None, uploader=None, title=None, limit=1000, full_json=False):
    """
    title	 Title text search
    uploader Uploader SteamID as 64-bit integer
    player   Player SteamID as 64-bit integer
    limit    Number of results to get (Max 1000)
    """

    if not (player or uploader or title):
        logging.critical('No params applied to search')
        exit(2)

    params = {'limit': limit}
    if player:
        params['player'] = player
    if uploader:
        params['uploader'] = uploader
    if title:
        params['title'] = title

    request = get(get_search_url(), params=params)
    request.raise_for_status()
    request = request.json()
    if full_json:
        return request
    return request['logs']


def get_log(log_id):
    request = get(get_log_url(log_id))
    request.raise_for_status()
    return request.json()

