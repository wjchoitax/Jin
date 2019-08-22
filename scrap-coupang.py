import requests
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup


PRICE_PATH = 'a > dl > dd > div.price-area > div.price-wrap > div.price > em > strong'
LIKE_PATH = 'a > dl > dd > div.other-info > div.rating-star > span.rating-total-count'
IMG_PATH = 'a > dl > dt > img'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
res = requests.get('https://www.coupang.com/np/campaigns/82/components/178155', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# 2. 데이터를 수집하여 list of list로 만든다 [상품명, 가격, 좋아요, URL]
product_list = []

for li_tag in soup.select('#productList > li'):
    likes = 0
    try:
        likes = li_tag.select_one(LIKE_PATH).text.strip()[1:-1]
    except:
        pass

    product_list.append([
        li_tag.select_one('a > dl > dd > div.name').text.strip(),
        int(li_tag.select_one(PRICE_PATH).text.strip().replace(',','')),
        int(likes),
        'http:' + li_tag.select_one(IMG_PATH)['src']
    ])


# 3. 엑셀로 저장한다.
df = pd.DataFrame(product_list)                           # Product list 를 데이터프레임으로
df.columns = ['상품명', '가격', '좋아요', '이미지링크']      # 컬럼명칭 삽입
df.to_excel('Product list with pandas.xlsx')              # 데이터프레임을 엑셀로 저장
print('save ok..')


# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = 'Product List'
#
# # 헤더추가
# sheet['A1'] = '상품명'
# sheet['B1'] = '가격'
# sheet['C1'] = '좋아요'
# sheet['D1'] = '이미지링크'
#
# for i, row in enumerate(product_list):
#     for j, cell in enumerate(row):
#         sheet.cell(i + 2, j + 1, cell)
#
# wb.save('Product list.xlsx')
# print('save ok..')

# 이때 Pandas를 사용하여 엑셀로 저장