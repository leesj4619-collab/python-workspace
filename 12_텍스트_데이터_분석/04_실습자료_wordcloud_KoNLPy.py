import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = """
Python machine learning data science artificial intelligence
deep learning neural network programming code development
algorithm model training dataset feature engineering
"""

def 실습1():
    # TODO: WordCloud 객체 생성 (기본값으로)
    wc = WordCloud(

    ).generate(text)
    # TODO: text 로 WordCloud 생성


def 실습2():
    wc = WordCloud(
    width=800,
    height=400,# TODO: 너비 800, 높이 400
    background_color='white',# TODO: 배경색 흰색
    max_words=100,# TODO: 최대단어 100개
    colormap='plasma'# TODO: 색상테마 plasma
    ).generate(text)

    # TODO: figure 사이즈 (10, 5)
    plt.figure(figsize=(10,5))
    # TODO: wc 이미지 출력, 보간법 bilinear
    plt.imshow(wc,interpolation='bilinear')
    # TODO: 축 끄기
    plt.axis('off') # x축 y축 그릴 필요 없으므로 축 제거 axis 축
    # TODO: 여백 자동조정
    plt.tight_layout
    # TODO: 'wordcloud.png' 로 저장, dpi=150
    plt.savefig('wordcloud.png', dpi=150)
    # TODO: 화면에 출력
    plt.show()
실습1()
실습2()