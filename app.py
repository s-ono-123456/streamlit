import streamlit as st
import requests
from typing import List
import faiss
import numpy as np

# 検索用データの準備（例: ダミーデータ）
data = [
    "これはサンプルデータです。",
    "RAGの実装例について説明します。",
    "gemma-2-2b-jpn-itモデルを使用します。",
    "Streamlitを使ったアプリケーション開発。"
]

# FAISSインデックスの構築
def build_faiss_index(data: List[str]):
    dimension = 512  # ベクトルの次元数（仮定）
    index = faiss.IndexFlatL2(dimension)
    # ダミーのベクトルを生成（実際には埋め込みモデルを使用）
    vectors = np.random.rand(len(data), dimension).astype('float32')
    index.add(vectors)
    return index, vectors

index, vectors = build_faiss_index(data)

# 検索関数
def search(query: str, top_k: int = 3):
    # クエリをベクトル化（ダミーのベクトルを使用）
    query_vector = np.random.rand(1, vectors.shape[1]).astype('float32')
    distances, indices = index.search(query_vector, top_k)
    results = [data[i] for i in indices[0]]
    return results

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
    search_results = search(query)
    st.write("検索結果:", search_results)

    # 検索結果をプロンプトに含めてLLMに送信
    context = "\n".join(search_results)
    prompt = f"以下の文脈を基に質問に答えてください:\n{context}\n質問: {query}"
    response = call_llm_api(prompt)

    st.write("回答:", response)