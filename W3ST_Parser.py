import requests

api = 'Your_oklink_api_key'

headers = {'Ok-Access-Key': api}


def read_file(filename):
    result = []
    with open(filename, 'r') as file:
        for tmp in file.readlines():
            result.append(tmp.replace('\n', ''))

    return result


def write_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(f'{text}\n')


def total_count_of_w3st(page, address):
    tw = 0
    params = {
        'chainShortName': 'BSC',
        'address': address,
        'protocolType': 'token_721',
        'limit': '50',
        'page': page
    }

    data = requests.get(
        'https://www.oklink.com/api/v5/explorer/address/address-balance-fills',
        params=params,
        headers=headers,
    ).json()['data'][0]

    total_pages = int(data['totalPage'])
    tokenList = data['tokenList']

    for token in tokenList:
        if token['token'] == 'WΞST':
            tw += 1

    return total_pages, tw


for address in read_file('addresses.txt'):
    total_w3sts = 0
    total_pages, tw = total_count_of_w3st(1, address)
    total_w3sts += tw

    for i in range(2, total_pages+1):
        total_pages, tw = total_count_of_w3st(i, address)
        total_w3sts += tw
    print(f'{address};{total_w3sts}')
    write_to_file('Result.txt', f'{address};{total_w3sts}')