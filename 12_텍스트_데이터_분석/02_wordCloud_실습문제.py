from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = """
game player character level skill attack defense magic sword shield
warrior mage archer knight paladin ranger assassin monk wizard priest
quest dungeon boss monster enemy battle victory defeat reward experience
item weapon armor potion gold treasure map village castle dragon
team strategy strength speed agility intelligence stamina power ability
"""
def 문제1():
    wc = WordCloud(
        background_color='black',# TODO: 배경색 검정으로 설정
        width=1000,# TODO: 이미지 너비 1000
        height=500,# TODO: 이미지 높이 500
        max_words=50# TODO: 최대 단어 50개
    ).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
문제1()

def 문제2():
    colormaps = ['plasma', 'inferno', 'cool']
    plt.figure(figsize=(15, 5))
    for i, cmap in enumerate(colormaps):
        wc = WordCloud(
            colormap=cmap# TODO: colormap을 반복변수 cmap으로 설정
        ).generate(text)
        plt.subplot(1, 3, i + 1)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(cmap)
    plt.tight_layout()
    plt.show()
문제2()

def 문제3():
    wc = WordCloud(
        width=800, height=400,# TODO: 너비 800, 높이 400
        background_color='white'# TODO: 배경 흰색
    ).generate(text)
    plt.savefig('game_wordcloud.png',dpi=200)# TODO: 'game_wordcloud.png' 로 저장, dpi=200
문제3()

def plt_없이_이미지저장하기():
    wc = WordCloud(
        width=800, height=400,# TODO: 너비 800, 높이 400
        background_color='white'# TODO: 배경 흰색
    ).generate(text)
    wc.to_file('game_wordcloud.png',dpi=200)