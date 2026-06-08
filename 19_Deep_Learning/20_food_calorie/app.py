from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from PIL import Image
import io

app = Flask(__name__)

print("모델 불러오는 중...")
음식분류 = pipeline(
    "image-classification",
    model="nateraw/food",
    device=0  # GPU 사용 / CPU는 device=-1
)

칼로리사전 = {
    "pizza": 266,
    "ramen": 436,
    "sushi": 200,
    "ice_cream": 207,
    "steak": 271,
    "fried_rice": 333,
    "bibimbap": 490,
    "dumplings": 310,
    "chicken_wings": 430,
    "hamburger": 540,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read())).convert("RGB")

    results = 음식분류(image)

    top3 = []
    for item in results[:3]:
        label = item["label"]
        score = round(item["score"] * 100, 1)
        칼로리 = 칼로리사전.get(label, "알 수 없음")
        top3.append({
            "label": label,
            "score": score,
            "칼로리": 칼로리
        })

    return jsonify({"results": top3})

if __name__ == '__main__':
    app.run(debug=True)