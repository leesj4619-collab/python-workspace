import folium
from folium.plugins import MarkerCluster as mc, MarkerCluster
import pandas as pd
from pandas.conftest import dropna
import hypothesis
import pytest


def 주유소_지도():

    # todo 1 : CSV 파일 읽기
    # 힌트 : read_excel 이 아니라 read_csv 를 사용하시면 됩니다.
    #        엑셀처럼 skiprows, header=None 없어도 컬럼명이 자동으로 잡힙니다.
    df = pd.read_csv('서울특별시_중랑구_주유소_20260213.csv',encoding='utf-8')

    # todo 2 : 컬럼명 확인하기
    # 힌트 : print(df.columns) 로 찍어보시고
    #        위도, 경도 컬럼 이름이 정확히 뭔지 확인하세요.
    print(df.columns)
    '''
    Index(['주유소명', '시도명', '시군구명', '소재지도로명주소', '소재지지번주소', '전화번호', '위도', '경도',
       '상표구분명', '대표자명', '총직원수', '데이터기준일자'],
      dtype='str')
    '''
    # todo 3 : 위도 경도 NaN 있는 행 제거
    # 힌트 : dropna(subset=[...]) 오늘 배운 것 그대로 사용하시면 됩니다.
    #        컬럼명만 todo 2 에서 확인한 이름으로 바꿔주세요.
    df = df.dropna(subset=['위도','경도'])
    # todo 4 : 지도 생성
    # 힌트 : 중랑구 중심 위도경도는 37.6063, 127.0928 입니다.
    #        zoom_start 는 본인이 원하는 숫자로 설정해보세요.
    m = folium.Map(location=[37.6063, 127.0928],
               zoom_start=16)
    # todo 5 : 클러스터링으로 마커 찍기
    # 힌트 : MarkerCluster 와 iterrows 오늘 배운 것 그대로입니다.
    cluster = mc().add_to(m)
    # iterrows() csv 엑셀 등 데이터를 한 행씩 추출할 때 많이 사용!
    for _, row in df.iterrows():
        folium.Marker(
            location=[row['위도'],row['경도']]
        ).add_to(cluster)
    # todo 6 : html 파일로 저장
    # 힌트 : m.save("주유소지도.html")
    m.save("주유소지도.html")

#주유소_지도()

def 공중화장실_지도():

    # todo 1 : CSV 파일 읽기
    # 힌트 : read_csv 를 사용하기
    #        파일이 깨진다면 encoding='cp949' 를 추가하기
    #        pd.read_csv('파일명.csv', encoding='cp949')
    df = pd.read_csv('데이터실습파일/공중화장실정보.csv', encoding='cp949')
    # todo 2 : 컬럼명 확인하기
    # 힌트 : print(df.columns) 로 찍어보세요.
    #        위도 경도 컬럼 이름 특이합니다.
    print(df.columns)
    '''
    Index(['개방자치단체코드', '관리번호', '구분명', '근거법령명', '화장실명', '소재지도로명주소', '소재지지번주소',
       '남성용-대변기수', '남성용-소변기수', '남성용-장애인용대변기수', '남성용-장애인용소변기수', '남성용-어린이용대변기수',
       '남성용-어린이용소변기수', '여성용-대변기수', '여성용-장애인용대변기수', '여성용-어린이용대변기수', '관리기관명',
       '전화번호', '개방시간', '개방시간상세', '설치연월', 'WGS84위도', 'WGS84경도', '화장실소유구분명',
       '오물처리방식', '안전관리시설설치대상여부', '비상벨설치여부', '비상벨설치장소', '화장실입구CCTV설치유무',
       '기저귀교환대유무', '기저귀교환대장소', '리모델링연월', '데이터기준일자', '데이터갱신구분', '데이터갱신시점',
       '최종수정시점'],
      dtype='str')
    '''
    # todo 3 : 위도 경도 NaN 있는 행 제거
    # 힌트 : dropna(subset=[...]) 컬럼명이 다르니 주의하기
    df = df.dropna(subset=['WGS84위도','WGS84경도'])
    # todo 4 : 지도 생성
    # 힌트 :  zoom_start : 7
    #        대한민국 중심 위도경도 36.5, 127.5
    m = folium.Map(
        location=[36.5,127.5],
        zoom_start=7
    )
    # todo 5 : 클러스터링으로 마커 찍기
    cluster = MarkerCluster().add_to(m)
    # todo 6 : 마커에 화장실 이름 popup 으로 추가해보기
    # 힌트 : folium.Marker(location=[...], popup=row["화장실명"])
    for _, row in df.iterrows():
        folium.Marker(
            location=[row['WGS84위도'],row['WGS84경도']],
            popup=row['화장실명']
        ).add_to(cluster)
    # todo 7 : html 파일로 저장
    # 힌트 : m.save("화장실지도.html")
    m.save("화장실지도.html")
공중화장실_지도()