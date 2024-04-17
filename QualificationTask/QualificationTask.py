#!/usr/bin/env python3
"""get request to extract specific information from a given url"""


import requests
from sys import argv

if len(argv) >= 2:
    url = argv[1]
else:
    print("Usage: QualificationTask.py <url>")
    exit(1)

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"Error fetching data: {e}")

titles = [item["title"] for item in data if "quia" in item["title"]]
for title in titles:
    if isinstance(title, str):
        print(f"{title}")
    if isinstance(title, int):
        print(f"this is an integer {title}")