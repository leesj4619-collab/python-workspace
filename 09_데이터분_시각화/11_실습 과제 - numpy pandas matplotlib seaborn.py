import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac 사용자
plt.rcParams['axes.unicode_minus'] = False

# 저장 폴더 생성
저장폴더 = "seaborn_homework"
os.makedirs(저장폴더, exist_ok=True)

# 데이터 불러오기
tips     = pd.read_csv("seaborn_tips.csv")
titanic  = pd.read_csv("seaborn_titanic.csv")
iris     = pd.read_csv("seaborn_iris.csv")
penguins = pd.read_csv("seaborn_penguins.csv")
flights  = pd.read_csv("seaborn_flights.csv")
diamonds = pd.read_csv("seaborn_diamonds.csv")
mpg      = pd.read_csv("seaborn_mpg.csv")


# ═══════════════════════════════════════════════
# 난이도 ★☆☆  기초 문제
# ═══════════════════════════════════════════════

def 문제1_데이터구조확인():
    """
    [tips 데이터]
    tips 데이터의 기본 구조를 확인하세요.
    출력 항목: 상위 5행 / 행열 크기 / 컬럼명 / 데이터타입 / 기초통계
    """
    print("▶ 상위 5행", tips.head())
    # TODO: 상위 5행 출력

    print("▶ 데이터 크기",tips.shape)
    # TODO: shape 출력

    print("▶ 컬럼명",tips.columns)
    # TODO: columns 출력

    print("▶ 데이터 타입",tips.dtypes)
    # TODO: dtypes 출력

    print("▶ 기초 통계",tips.dtypes())
    # TODO: describe() 출력


문제1_데이터구조확인()


def 문제2_scatterplot_tips():
    """
    [tips 데이터] 산점도
    x축 : total_bill (계산서 금액)
    y축 : tip (팁)
    hue : smoker (흡연 여부로 색 구분)
    제목 : "흡연 여부에 따른 계산서 vs 팁"
    저장 : 저장폴더/문제2_산점도.png
    """
    plt.figure(figsize=(8, 5))
    # TODO: sns.scatterplot() 작성
    sns.scatterplot('tips')
    # TODO: 제목 설정

    # TODO: x축 레이블 → "계산서 금액"

    # TODO: y축 레이블 → "팁"

    plt.tight_layout()
    # TODO: png 저장
    plt.show()


문제2_scatterplot_tips()


def 문제3_histplot_tips():
    """
    [tips 데이터] 히스토그램
    x축 : tip (팁 금액)
    bins : 15
    kde  : True (분포 곡선 포함)
    color: "tomato"
    제목 : "팁 금액 분포"
    저장 : 저장폴더/문제3_히스토그램.png
    """
    plt.figure(figsize=(8, 5))
    # TODO: sns.histplot() 작성

    # TODO: 제목 설정

    plt.tight_layout()
    # TODO: png 저장
    plt.show()


문제3_histplot_tips()


# ═══════════════════════════════════════════════
# ⭐ 난이도 ★★☆  중급 문제
# ═══════════════════════════════════════════════

def 문제4_barplot_titanic():
    """
    [titanic 데이터] 바 그래프
    x축 : pclass (객실 등급)
    y축 : survived (생존율)
    hue : sex (성별 구분)
    제목 : "객실 등급 & 성별에 따른 생존율"
    저장 : 저장폴더/문제4_바그래프.png

    힌트: pclass 컬럼을 확인해보세요 → titanic['pclass'].unique()
    """
    plt.figure(figsize=(8, 5))
    # TODO: sns.barplot() 작성

    # TODO: 제목 설정

    plt.tight_layout()
    # TODO: png 저장
    plt.show()


문제4_barplot_titanic()


def 문제5_boxplot_iris():
    """
    [iris 데이터] 박스플롯
    x축 : species (붓꽃 종류)
    y축 : sepal_length (꽃받침 길이)
    palette : "pastel"
    제목 : "붓꽃 종류별 꽃받침 길이 분포"
    저장 : 저장폴더/문제5_박스플롯.png

    힌트: 이상치(동그라미)가 보이면 정상입니다
    """
    plt.figure(figsize=(8, 5))
    # TODO: sns.boxplot() 작성

    # TODO: 제목 설정

    plt.tight_layout()
    # TODO: png 저장
    plt.show()


문제5_boxplot_iris()


def 문제6_lineplot_flights():
    """
    [flights 데이터] 선 그래프
    x축 : year (연도)
    y축 : passengers (승객 수)
    hue : month (월별 선 구분)
    제목 : "연도별 월별 항공 승객 수 변화"
    저장 : 저장폴더/문제6_선그래프.png

    힌트: flights 데이터 구조를 먼저 print 해서 확인해보세요
    """
    plt.figure(figsize=(10, 5))
    # TODO: sns.lineplot() 작성

    # TODO: 제목 설정

    plt.tight_layout()
    # TODO: png 저장
    plt.show()


문제6_lineplot_flights()