#!/usr/bin/python3
"""
Module for num of subs in a subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    results = response.json().get("data")
    return results.get("subscribers")
