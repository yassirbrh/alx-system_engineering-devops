#!/usr/bin/python3
'''
    Importing modules.
'''
import requests


def number_of_subscribers(subreddit):
    '''
        Queries the Reddit API and returns the number of subscribers
    '''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': '0-subs.py/1.0 (by https://github.com/yassirbrh;)'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        num_of_subs = data.get('data').get('subscribers')
        if num_of_subs is None:
            return 0
        return num_of_subs
