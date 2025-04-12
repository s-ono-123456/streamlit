import streamlit as st
import requests
from typing import List
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from faiss_utils import search

# FAISSインデックスを読み込む
index = faiss.read_index("output/faiss_index.bin")

# 埋め込みデータを読み込む
with open("output/data.pkl", "rb") as f:
    data = pickle.load(f)

# GLuCoSE-base-ja-v2モデルの初期化
model = SentenceTransformer('pkshatech/GLuCoSE-base-ja-v2')

# LLM API呼び出し関数
def call_llm_api(prompt: str) -> str:
    url = "http://localhost:8000/api"  # gemma-2-2b-jpn-itモデルのAPIエンドポイント
    payload = {"prompt": prompt}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        return "エラー: モデルへのリクエストに失敗しました。"

# Streamlitアプリケーション
st.title("RAG実装デモ")

query = st.text_input("質問を入力してください:")
if query:
    st.write("検索中...")
    # クエリをベクトル化
    query_vector = model.encode([query]).astype('float32')
    search_results = search(index, query_vector, data, top_k=3)
    st.write("検索結果:", search_results)

    # 検索結果をプロンプトに含めてLLMに送信
    context = "\n".join(search_results)
    prompt = f"以下の文脈を基に質問に答えてください:\n{context}\n質問: {query}"
    response = call_llm_api(prompt)

    st.write("回答:", response)