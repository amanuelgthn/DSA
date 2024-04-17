#!/usr/bin/env python3
"""Request to extract specific information from API requests"""


import requests
from sys import argv

if len(argv) >= 2:
    url = argv[1]
else:
     print(f"Usage: QualificationTask.py <url>")
     exit(1)

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"Error fetching data: {e}")
    exit(1)
titles = [item["title"] for item in data if "libero" in item["title"]]
for title in titles:
    if isinstance(title, str):
        print(f"{title}")
    if isinstance(title, int):
        print(f"int: {title}")
        
