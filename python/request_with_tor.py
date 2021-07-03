# Open directory TOR -> cd "C:\Users\bruno\Tor Browser\Browser\TorBrowser\Tor"
# Deactivate service -> tor --service remove
# Activate service -> tor --service install -options ControlPort 9151
# List all conections -> netstat -an

import random
import requests

step_change = 2


def check_ip(control):
    global creds
    session = requests.session()
    if control % step_change == 0:
        creds = str(random.randint(10000, 0x7fffffff)) + ":" + "foobar"
    session.proxies = {
        'http': 'socks5h://{}@localhost:9050'.format(creds),
        'https': 'socks5h://{}@localhost:9050'.format(creds)
    }
    r = session.get('http://httpbin.org/ip')
    print(r.text)


for i in range(5):
    check_ip(i)
