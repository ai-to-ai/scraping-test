import requests
from lxml.html import fromstring
import re

PROXY = ''
proxies = {
   'http': PROXY,
   'https': PROXY
}

cookies = {
   'AXIOMID2':'LF73KJHXCUUFL6KTYT33TWHAF9PA44J6',
   'AXIOMID':'8lypgs8ljui21rugohrmrm3g7208198'
}
URL = 'https://www.quora.com/qemail/tc?al_imp=eyJ0eXBlIjogMzMsICJoYXNoIjogIjEzOTA3MTgyNzY2MjcxNzIzODJ8MXwxfDM5MDM3MTkxOSJ9&al_pri=1&aoid=zAGnk0HMhfU&aoty=2&aty=4&cp=1&et=2&id=9911ccb58f1a400d842ec2fe10301bc0&q_aid=4CTrKSowbWA&uid=VOFXbF6MshZ'




r = requests.get(url = URL, proxies = proxies)
print(r.text)
root = fromstring(r.content)
print(r.url)