import time
import os
import hashlib
from urllib.request import urlopen, Request
from dotenv import load_dotenv
from email_alert import sendEmail

load_dotenv()

uri = os.environ.get('URL_VERIFY')
url = Request(uri, headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()

print("running")

time.sleep(30)

while True:
    try:
        newResponse = urlopen(url).read()
        newHash = hashlib.sha224(newResponse).hexdigest()

        if newHash == currentHash:
            time.sleep(30)
            print("not changed")
            continue
        else:
            print("something changed")
            sendEmail()
            break
    except Exception as e:
        print("error")
