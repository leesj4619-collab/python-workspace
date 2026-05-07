import folium
### 서울특별시 종로구 관철동 위도 경도를 검색하여 위치 설정하거나
#### 나의 동네 위도 경도로 변경해서 진행
### 주변 카페 3가지의 위도 경도를 알아내고, myLocationMap.html로 생성하기
# TODO 1. 지도 만들기 (내 동네 위도/경도로 바꿔보기)
m = folium.Map(
    location=[37.5691048202295, 126.985986580352],  # 위도, 경도
    zoom_start=16       # 동네 보기 좋은 줌 레벨
)

# TODO 2. 첫 번째 카페 마커
folium.Marker(
    location=[37.569998882903576, 126.98457996034828],
    popup='스타벅스',   # 카페 이름
    tooltip='첫 번째 카페'  # 마우스 올렸을 때 텍스트
).add_to(m)

# TODO 3. 두 번째 카페 마커
folium.Marker(
    location=[37.56899652101077, 126.98454620883463],
    popup='빽다방',
    tooltip='두 번째 카페'
).add_to(m)

# TODO 4. 세 번째 카페 마커
folium.Marker(
    location=[37.56851924344135,126.98659227331991],
    popup='할리스',
    tooltip='세 번째 카페'
).add_to(m)

# TODO 5. 저장
m.save('myLocationMap.html')  # 파일 이름