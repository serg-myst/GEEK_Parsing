import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
params = {'latitude': '55.794492',
          'longitude': '37.982199',
          'query': 'манты'}
url = 'https://api.delivery-club.ru/api1.2/vendors/search'

response = requests.get(url, params=params, headers=headers, verify=True)
