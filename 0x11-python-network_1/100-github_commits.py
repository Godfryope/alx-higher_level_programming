#!/usr/bin/python3

import requests
import sys

# get the repository name and owner name from command line arguments
repo = sys.argv[1]
owner = sys.argv[2]

# set up the API endpoint URL
url = f"https://api.github.com/repos/{owner}/{repo}/commits"

# make a GET request to the API endpoint
response = requests.get(url)

# check if the response was successful (status code 200)
if response.status_code == 200:
    # get the list of commits from the response JSON data
    commits = response.json()

    # loop through the 10 most recent commits and print the SHA and author name
    for commit in commits[:10]:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
else:
    # if the response was not successful, print the error message
    print(f"Error: {response.status_code} - {response.reason}")

