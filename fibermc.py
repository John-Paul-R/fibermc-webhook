
import requests
import json
from sys import argv

import os
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL_FIBERMC = os.getenv("WEBHOOK_URL_FIBERMC")

post_headers = {
    "content-type": "application/json",
}

with open(argv[1]) as f:
    post_data = json.load(f)

res = requests.post(WEBHOOK_URL_FIBERMC, json=post_data, headers=post_headers)

print(res)
