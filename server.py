from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# gemma-2-2b-jpn-itモデルのロード（ダミー実装）
def load_model():
    # ダミーのモデルとトークナイザーを返す
    class DummyModel:
        def __init__(self):
            pass

    class DummyTokenizer:
        def __init__(self):
            pass

    return DummyModel(), DummyTokenizer()

model, tokenizer = load_model()

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