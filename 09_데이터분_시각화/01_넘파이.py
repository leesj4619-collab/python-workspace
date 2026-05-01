'''
pip install numpy

import numpy as np # np는 numpy라는 이름이 길어서 줄임말
'''

import numpy as np
# 일반 파이썬에선 숫자 목록
기본파이썬 = [1,2,3,4,5]
# np로 만들어진 array = 배열이다.
넘파이 = np.array([1,2,3,4,5])

print(type(기본파이썬)) #<class 'list'>
print(type(넘파이))    #<class 'numpy.ndarray'>

# Numpy로 자주 사용하는 배열 생성 방법
영_5개 = np.zeros(5)                             # [0. 0. 0. 0. 0.]         원하는 개수 만큼 0만 있는 목록 만들 때 사용
일_5개 = np.ones(5)                              #[1. 1. 1. 1. 1.]          원하는 개수 만큼 1만 있는 목록 만들 때 사용
이_5개 = np.arange(0,10,2)  #[0 2 4 6 8]                0부터 10-1까지 2씩 건너뛰어 생성
균등간격_5개 = np.linspace(0,1,5)  #[0.   0.25 0.5  0.75 1.  ] 실수형태로 0부터 1까지 n만큼 균등하게 생성

print(영_5개)
print(일_5개)
print(이_5개)
print(균등간격_5개)

