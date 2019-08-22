
favorite_colors = ['red', 'blue', 'pink', 'brown']

file = open('c:\python\hello.txt', 'w', encoding='utf-8')

new_colors = []
for color in favorite_colors :
    new_colors.append(color + '\n')


file.writelines(new_colors)
file.close()

print('file operation ok..')

