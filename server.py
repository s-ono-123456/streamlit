from flask import Flask, request, jsonify

app = Flask(__name__)

# gemma-2-2b-jpn-itモデルのロード（ダミーの例）
def load_model():
    # 実際にはモデルをロードするコードを記述
    return "gemma-2-2b-jpn-itモデル"

model = load_model()

# 推論関数（ダミーの例）
def generate_response(prompt):
    # 実際にはモデルを使用して推論を行うコードを記述
    return f"モデルの応答: {prompt}"

# APIエンドポイント
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error": "Invalid request, 'prompt' is required."}), 400

    prompt = data['prompt']
    response = generate_response(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)