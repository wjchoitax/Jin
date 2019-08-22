
import requests as req      # alias 한다. 판다스/텐서플로 # import : 실행해서 메모리에 올린다.
                            # 통째로 올린다. 모듈로 올린다. 알리아싱해서 올린다.


def add(height=170, weight=60, age=20):
    return height, weight, age        # 함수의 블럭은 들여쓰기가 끝나는 지점

''' javascript 함수 정의
function add(a, b) {
    return a + b
}
'''

print(add(age=40, weight=70))       # position base parameter vs keyword 기반 파라메타 호출방식(파이썬에만 있는 기능)


print('hello', 'world', 'hi', 'good', sep='---', end='...end of file')