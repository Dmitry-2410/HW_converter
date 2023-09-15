import requests

URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = 'fca_live_KMXB7B82vPafDq1Olx40kQm7hn7FtLZCoUG0g94F&currencies='


def get_actual_currencies():
    response = requests.get(URL + API_KEY)
    result = response.json()
    return result['data']

