#!/usr/bin/python3
"""This script queries the first 10 hot posts listed for
a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Lists the first 10 hot posts for a given subreddit"""
    if not subreddit or type(subreddit) is not str:
        print(None)
        return
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    posts = response.get('data', {}).get('children', [])
    if not posts:
        print(None)
        return
    for post in posts:
        print(post.get('data', {}).get('title', None))
