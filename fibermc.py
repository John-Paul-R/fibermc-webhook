
import requests

import os
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL_FIBERMC = os.getenv("WEBHOOK_URL_FIBERMC")


message_content = """
This is a test of a custom Discord webhook! -JP
"""

post_headers = {
    "content-type": "application/json",
}

post_data = {
    "content": message_content,
}


res = requests.post(WEBHOOK_URL_FIBERMC, json=post_data, headers=post_headers)

print(res)
