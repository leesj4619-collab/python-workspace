# pip install qrcode[pil] -> 터미널 cmd 창에서 작성!
# pypi에서 qrcode가 세팅된 주소에서 나의 컴퓨터로 모듈 세팅
import qrcode

# QR 코드 만들기
qr = qrcode.QRCode(version=1,   # 크기 조절 (1~40) 숫자가 클수록 큼
                   box_size=10, # QR 코드의 각 박스 크기
                   border=4)    # QR 코드의 테두리 크기 (박스 단위)

# QR 코드에 데이터 추가
data = "https://www.naver.com"
qr.add_data(data)
qr.make(fit=True) # QR 코드의 크기를 데이터에 맞게 자동 조절

# QR 코드 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png") # QR 코드 이미지 저장
print("qr_code.png 파일이 생성되었습니다.")
