import os

try:
    os.mkdir('c:\\python\work-for-python')

except:
    print('디렉토리가 있으므로 만들지 않습니다.')

os.chdir('c:\\python\work-for-python')
print(os.getcwd())

for i in range(200):
    file = open('scan-000' + str(i) + '-fax', 'w')
    print(file.name + ' created..')
    file.close()

print('job completed..')