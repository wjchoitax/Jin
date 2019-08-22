'''
my_friends = {
    'soongon' : 'seoul',
    'chanho': 'busan',
    'seri': 'daejun',
    'youna' : 'suwon'
}

print(my_friends['soongon'])

my_friends['seri'] = 'seoul'
my_friends['iu'] = 'kawngju'

print(my_friends)

'''

# dictionary는 jason 데이터구조와 동일한 구조를 지니고 있다

post = {
    'title': '오늘은 좋은날',
    'content': '좋아요',
    'tag': ['good', 'pyhton', 'pycharm'],
    'replies': [
        {
            'author':'iu',
            'content':'good',
        },
        {
            'author': 'kim',
            'content': 'bad',
        }
    ]
}

print(post.get('replies'))

# depth 를 가지고 파싱 할 수 있다. 웹에 접근하기 용이함.
# print(post['replies'][0]['author'])