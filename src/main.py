import time
import os
import hashlib
from urllib.request import urlopen, Request
from dotenv import load_dotenv
from email_alert import sendEmail
from verify_hash import isPageChange
from extract_html import extractDateInformation

load_dotenv()

uri = os.environ.get('URL_VERIFY')
url = Request(uri, headers={'User-Agent': 'Mozilla/5.0'})

if isPageChange(url):
    html_doc = urlopen(url).read()
    message = extractDateInformation(html_doc)
    print(message)
    sendEmail(message)

