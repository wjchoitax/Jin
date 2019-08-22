import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
res = requests.get('https://www.coupang.com/np/campaigns/82/components/178155', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')    # text를 확보해서 파싱하기 좋게 객체로 만든다.
tag = soup.select_one('#\\31 37145559 > a > dl > dd > div.name')

print(tag)

