import requests


url = "https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=f3dfdc9e5b3a993a17dd"

data = requests.get(url=url)
print(data.text)
