
favorite_colors = ['red', 'blue', 'pink', 'brown']
print(favorite_colors)


# for문 문법

result_list = []
for color in favorite_colors:
    if len(color) >= 5:
        result_list.append(color)

print(result_list)

# range 는 수열을 만들어주는 함수
# 파이썬에서는 2차원 데이터(tabula data)를 다루는 Pandas 라는 라이브러리를 제공한다.
# list comprehention

# create.. add item

favorite_colors.append('white')
print(favorite_colors)

# update item

favorite_colors.insert(2, 'black')
print(favorite_colors)

# delete item
# favorite_colors.remove('black')
del favorite_colors[1]
print(favorite_colors)

# seacrch item(s)

print(favorite_colors[2:4])
