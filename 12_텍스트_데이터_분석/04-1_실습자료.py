from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter

text = """
game player character level skill attack defense magic sword shield
warrior mage archer knight paladin ranger assassin monk wizard priest
quest dungeon boss monster enemy battle victory defeat reward experience
item weapon armor potion gold treasure map village castle dragon
team strategy strength speed agility intelligence stamina power ability
"""

def 실습3():
    wc = WordCloud(
    background_color='black',# TODO: 배경색 검정
    width=1000,
    height=500,# TODO: 너비 1000, 높이 500
    max_words=50# TODO: 최대단어 50개
    ).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def 실습4():
    # TODO: colormaps 리스트 ['plasma', 'inferno', 'cool'] 로 선언
    colormaps = ['plasma', 'inferno', 'cool']
    plt.figure(figsize=(15, 5))

    # TODO: enumerate로 colormaps 순회, 반복변수 i, cmap
    for i, cmap in enumerate(colormaps):
        wc = WordCloud(
        # TODO: colormap 을 반복변수 cmap 으로 설정
        colormap=cmap
        ).generate(text)

        # TODO: subplot 1행 3열, i+1 번째 위치
        plt.subplot(1,3,i+1)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(cmap)
    plt.tight_layout()
    plt.show()

def 실습5():
    wc = WordCloud(
    width=800,
    height=400,# TODO: 너비 800, 높이 400
    background_color='white'# TODO: 배경색 흰색
    ).generate(text)
    # TODO: plt 없이 'wc_file.png' 로 저장
    wc.to_file('wc_file.png')


def 실습6_형태소분석():
    # TODO: Okt 객체 생성
    okt = Okt()
    text = "나는 파이썬으로 자연어 처리를 공부하고 있어요"

    # TODO: 형태소 분리 출력
    print(okt.morphs(text))

    # TODO: 명사만 추출 출력
    print(okt.nouns(text))

    # TODO: 어간추출(stem=True) 형태소 분리 출력
    print(okt.morphs(text,stem=True))

def 실습7_wordcloud연결():
    text = """
파이썬은 데이터 분석과 머신러닝에 많이 사용됩니다.
데이터 과학자들은 파이썬으로 딥러닝 모델을 학습시킵니다.
자연어 처리와 컴퓨터 비전 분야에서도 파이썬이 인기입니다.
인공지능 시대에 데이터 분석 능력은 매우 중요합니다.
"""
    # TODO: Okt 객체 생성
    okt = Okt()
    ###### nouns 거치기전 파이썬은 데이터 분석과 머신러닝에 많이 사용됩니다.
    # TODO: 명사 추출
    nouns = okt.nouns(text)
    ###### nouns 거친 후 파이썬 데이터 분석 머신러닝
    ###### nouns로 거르지 못한 단어를 2차적으로 거르기 위해서 추가해놓은 옵션
    # TODO: 불용어 집합 선언 {'것', '수', '등', '및', '더', '이', '그', '저', '때', '년', '들'}
    # 불용어 의미가 없는 단어 / 자주 나오지만 분석에 도움이 안되는 단어들
    stopwords = {'것','수','등','및','더','이','그','저','때','년','들'}

    # TODO: 불용어 제거 + 2글자 이상 필터링 (리스트 컴프리헨션)
    filtered = [w for w in nouns if w not in stopwords and len(w) > 1]
    '''
    filtered = []
    for w in nouns():
        if w not in stopwords and len(w) > 1:
            filtered.append(w)
    '''
    # TODO: Counter 로 단어 빈도 계산
    counts = Counter(filtered)

    # TODO: 한글 폰트 경로 설정
    font_path = 'C:/Windows.Fonts/malgun.ttf'

    wc = WordCloud(
    # TODO: font_path 설정
    font_path= font_path,
    width=800,
    height=400,# TODO: 너비 800, 높이 400
    background_color='white',# TODO: 배경색 흰색
    max_words=100,# TODO: 최대단어 100개
    # TODO: 색상테마 Set2
    colormap='Set2'
    # TODO: 빈도 딕셔너리로 WordCloud 생성
    ).generate_from_frequencies(counts)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    # TODO: 'korean_wordcloud.png' 저장, dpi=150
    plt.savefig('korean_wordcloud.png', dpi=150)
    plt.show()
실습7_wordcloud연결()