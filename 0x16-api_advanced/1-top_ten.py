#!/usr/bin/python3
'''
    Importing modules.
'''
import requests


def top_ten(subreddit):
    '''
        Queries the Reddit API and prints the titles of
        the first 10 hot posts listed for a given subreddit.
    '''
    url = "https://www.reddit.com/r/{}/hot.json?limit={}".format(subreddit, 10)
    headers = {
        'User-Agent': '0-subs.py/1.0 (by https://github.com/yassirbrh;)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print(None)
    if response.status_code == 200:
        data = response.json()
        for hot_post in data['data']['children']:
            print(hot_post['data']['title'])
