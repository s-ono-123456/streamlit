import faiss
import numpy as np
from typing import List

def build_faiss_index(data: List[str], dimension: int = 384):
    """
    FAISSインデックスを構築します。

    Args:
        data (List[str]): 検索対象のデータ。
        dimension (int): ベクトルの次元数。

    Returns:
        index: 構築されたFAISSインデックス。
        vectors: データに対応するベクトル。
    """
    index = faiss.IndexFlatL2(dimension)
    # all-MiniLM-L6-v2モデルでエンコードされたベクトルを使用します。
    vectors = np.array(data, dtype='float32')
    index.add(vectors)
    return index, vectors

def search(index, query_vector: np.ndarray, data: List[str], top_k: int = 3):
    """
    FAISSインデックスを使用して検索を実行します。

    Args:
        index: FAISSインデックス。
        query_vector (np.ndarray): クエリのベクトル。
        data (List[str]): 検索対象のデータ。
        top_k (int): 上位k件の結果を取得。

    Returns:
        List[str]: 検索結果。
    """
    distances, indices = index.search(query_vector, top_k)
    results = [data[i] for i in indices[0]]
    return results