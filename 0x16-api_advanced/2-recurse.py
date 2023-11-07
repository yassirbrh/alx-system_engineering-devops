#!/usr/bin/python3
'''
    Importing Modules
'''
import requests


def recurse(subreddit, hot_list=[], after="", counter=0):
    '''
        Recursive function that queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit.
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': '2-recurse.py/1.0 (by https://github.com/yassirbrh;)'
    }
    params = {
        "after": after,
        "counter": counter
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    counter += results.get("dist")
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, counter)
    return hot_list
