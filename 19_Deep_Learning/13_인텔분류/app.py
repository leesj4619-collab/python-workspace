from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# TODO 1: 모델 파일 이름 채우기
model = load_model('models/intel_model.keras')

# 알파벳 순서 고정 (image_dataset_from_directory 가 알파벳 순으로 읽음)
장면목록 = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']

장면이모지 = {
    'buildings': '🏢',
    'forest'   : '🌲',
    'glacier'  : '🧊',
    'mountain' : '⛰️',
    'sea'      : '🌊',
    'street'   : '🛣️'
}

장면한국어 = {
    'buildings': '건물',
    'forest'   : '숲',
    'glacier'  : '빙하',
    'mountain' : '산',
    'sea'      : '바다',
    'street'   : '거리'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']

    # TODO 2: 이미지 크기 채우기 (훈련 때 150x150 사용)
    image = Image.open(io.BytesIO(file.read())).convert('RGB').resize((150, 150))
    image = np.array(image) / 255.0
    image = image.reshape(1, 150, 150, 3)

    pred = model.predict(image)[0]   # 6개 확률 배열

    # TODO 3: 가장 높은 확률 인덱스 구하기
    최고인덱스 = np.argmax(pred)           # 힌트: np.argmax(pred)
    최고확률   = pred[최고인덱스] * 100

    # TODO 4: 신뢰도 기준 설정
    신뢰도기준 = 50           # 힌트: 50

    if 최고확률 >= 신뢰도기준:
        장면영어 = 장면목록[최고인덱스]
        result   = 장면한국어[장면영어]
        emoji    = 장면이모지[장면영어]
        confidence = 최고확률
    else:
        result     = '알 수 없는 장면'
        emoji      = '❓'
        confidence = 0

    # TODO 5: jsonify 로 result, confidence, emoji 반환
    return jsonify({
        'resulty': result,
        'confidence': f'{confidence:.1f}%',
        'emoji': emoji
    })

if __name__ == '__main__':
    app.run(debug=True)