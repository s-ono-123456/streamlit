import streamlit as st
import requests
from typing import List
import numpy as np
from faiss_utils import build_faiss_index, search
from sklearn.feature_extraction.text import TfidfVectorizer

# 検索用データの準備（例: ダミーデータ）
data = [
    "これはサンプルデータです。",
    "RAGの実装例について説明します。",
    "gemma-2-2b-jpn-itモデルを使用します。",
    "Streamlitを使ったアプリケーション開発。"
]

# TF-IDFベクトライザの初期化
tfidf_vectorizer = TfidfVectorizer()

# データを使ってTF-IDFベクトライザを学習
data_vectors = tfidf_vectorizer.fit_transform(data).toarray()

# FAISSインデックスの構築
index, _ = build_faiss_index(data_vectors.tolist(), dimension=data_vectors.shape[1])

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
    # クエリをTF-IDFでベクトル化
    query_vector = tfidf_vectorizer.transform([query]).toarray().astype('float32')
    search_results = search(index, query_vector, data)
    st.write("検索結果:", search_results)

    # 検索結果をプロンプトに含めてLLMに送信
    context = "\n".join(search_results)
    prompt = f"以下の文脈を基に質問に答えてください:\n{context}\n質問: {query}"
    response = call_llm_api(prompt)

    st.write("回答:", response)