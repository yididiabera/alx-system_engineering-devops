#!/usr/bin/python3
"""This script has a function that queries the Reddit API and returns the
number of all subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit"""
    if not subreddit or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    data = response.get('data', {}).get('subscribers', 0)
    return data
