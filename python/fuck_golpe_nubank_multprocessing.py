import requests
from multiprocessing import Pool
import random


def golpe(data):
    print(data)
    url = "https://admportal.covenantuniversity.edu.ng/class/api.nubank/telsc2.php"

    payload = {
        'cpf': random.randrange(10000000000, 99999999999),
        'senhacard': random.randrange(1000, 9999),
        'senhacard1': random.randrange(100, 999)
    }
    files = []
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response)

    return


def pool_handler(data):
    p = Pool(1000)
    p.map(golpe, data)


if __name__ == '__main__':
    size_data = [i for i in range(0, 1000000)]
    pool_handler(size_data)


# golpe()
