#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests

def count_words(subreddit, word_list, after='', word_dict=None):
    """A function that queries the Reddit API, parses the titles of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    """
    
    # Initialize the word dictionary on the first call
    if word_dict is None:
        word_dict = {}
        for word in word_list:
            word_lower = word.lower()
            if word_lower not in word_dict:
                word_dict[word_lower] = 0

    # Base case: If after is None, the recursion ends
    if after is None:
        # Sort and print the word count dictionary
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f'{word}: {count}')
        return

    # Make a request to the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    # Parse the response JSON
    try:
        data = response.json().get('data', {})
        after = data.get('after')
        posts = data.get('children', [])
        
        # Process each post's title
        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_dict.keys():
                word_dict[word] += title.count(word)

    except Exception:
        return
    
    # Recursive call to process the next page
    count_words(subreddit, word_list, after, word_dict)


