#!/usr/bin/python3
"""This script contains a recursive function that queries the Reddit
API and returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given
subreddit, the function should return None"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """This function returns a list containing the titles of all hot
    articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    response = response.json()
    response = response.get('data')
    after = response.get('after')
    children = response.get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
