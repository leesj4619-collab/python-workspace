from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import json

app = Flask(__name__)

# TODO 1: 모델 파일 이름을 채우세요
model = load_model('models/____________')

# 나비 클래스 이름 불러오기 (알파벳 순서)
# image_dataset_from_directory 가 폴더 이름을 알파벳 순으로 읽어요
나비목록 = sorted([
    폴더.name for 폴더 in (pathlib.Path("butterfly") / "train").iterdir()
    if 폴더.is_dir()
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']

    # TODO 2: 이미지 크기 채우기 (훈련 때 224x224 사용)
    image = Image.open(io.BytesIO(file.read())).convert('RGB').resize((224, 224))
    image = np.array(image) / 255.0
    image = image.reshape(1, 224, 224, 3)

    pred = model.predict(image)[0]   # 100개 확률 배열

    # TODO 3: 가장 높은 확률 인덱스 구하기
    # 힌트: np.argmax(pred)
    최고인덱스 = np.argmax(pred)
    최고확률   = pred[최고인덱스] * 100

    # TODO 4: 신뢰도 기준 설정 (100종류라 기준 낮게)
    신뢰도기준 = 30   # 힌트: 30

    if 최고확률 >= 신뢰도기준:
        result     = 나비목록[최고인덱스]
        confidence = 최고확률
        emoji      = '🦋'
    else:
        result     = '알 수 없는 나비'
        confidence = 0
        emoji      = '❓'

    # TODO 5: jsonify 로 result, confidence, emoji 반환
    return jsonify({
        'result': result,
        'confidence': f'{confidence:.1f}%',
        'emoji': emoji
    })

if __name__ == '__main__':
    app.run(debug=True)