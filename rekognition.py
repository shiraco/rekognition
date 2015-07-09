# coding:utf-8

import os
import sys
import requests
import json
import base64
from base64 import b64encode

rekognition_key = os.environ.get("REKOGNITION_KEY")
rekognition_secret = os.environ.get("REKOGNITION_SECRET")

def recognize(filename):

    # API-Keys
    url = "http://rekognition.com/func/api/"

    response = requests.post(
        url,
        data = {
            'api_key': rekognition_key,
            'api_secret': rekognition_secret,
            'jobs': 'face_recognize',
            'name_space': 'multify',
            'user_id': 'demo',
            'base64': b64encode(open(filename, 'rb').read()),
        }
    )

    res = json.loads(response.text)

    return res

if __name__ == '__main__':
    print(recognize(sys.argv[1]))
