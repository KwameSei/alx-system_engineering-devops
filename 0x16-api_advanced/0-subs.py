#!/usr/bin/python3
"""
Using reddits API
"""

import requests


def number_of_subscribers(subreddit):
    """returning the number of subscribers for reddit's subreddits"""
    headers = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return (res.json().get("data").get("subscribers"))
    return (0)
