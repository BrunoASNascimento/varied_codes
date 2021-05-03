# Open directory TOR -> cd "C:\Users\bruno\Tor Browser\Browser\TorBrowser\Tor"
# Deactivate service -> tor --service remove
# Activate service -> tor --service install -options ControlPort 9151
# List all conections -> netstat -an

import random
import requests


def check_ip():
    session = requests.session()
    creds = str(random.randint(10000, 0x7fffffff)) + ":" + "foobar"
    session.proxies = {
        'http': 'socks5h://{}@localhost:9050'.format(creds),
        'https': 'socks5h://{}@localhost:9050'.format(creds)
    }
    r = session.get('http://httpbin.org/ip')
    print(r.text)


for _ in range(5):
    check_ip()
