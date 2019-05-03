# -*- coding: utf-8 -*-

import settings
import json
import requests

SLACK_WEBHOOK = settings.WH

payload_dir = {
    "channel": "#webhook-test",
    "username": "@tatsushi.matsuda",
    "text": "This is post test to #webhook-test おはようございます。<http://www.yahoo.co.jp|ここ>", 
    "icon_emoji": ":ghost:"
}

r = requests.post(SLACK_WEBHOOK, data=json.dumps(payload_dir))