#!/usr/bin/python3
"""
Using reddit's API
"""

import requests


def number_of_subscribers(subreddit):
    """returning top ten post titles"""
    headers = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    res = requests.get(url, params=parameter, headers=headers,
                       allow_redirects=False)

    if res.status_code == 200:
        titles_ = res.json().get("data").get("children")
        for title_ in titles_:
            print(title_.get("data").get("title"))
    else:
        print(None)
