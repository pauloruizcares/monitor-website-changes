import time
import os
import hashlib
from urllib.request import urlopen, Request
from dotenv import load_dotenv

def isPageChange(url):
    response = urlopen(url).read()
    currentHash = hashlib.sha224(response).hexdigest()

    print("running")

    time.sleep(30)

    change=False

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
                change=True
                break
        except Exception as e:
            print("error", e)

    return change