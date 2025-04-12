import re
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from faiss_utils import build_faiss_index
from typing import List, Dict, Any

# ファイルパスの設定
input_file = "output/sample1.md"
output_file = "output/data.pkl"

# モデルのロード
model = SentenceTransformer('pkshatech/GLuCoSE-base-ja-v2')

# シート名ごとにデータを分割する関数
def split_by_sheet_name(content: str) -> List[str]:
    pattern = r"## シート名: (.+?)\n"
    matches = re.finditer(pattern, content)
    
    sheets = []
    last_index = None
    for match in matches:
        if last_index is not None:
            sheets[-1] += "\n" + content[last_index:match.start()].strip()
        sheets.append(f"## シート名: {match.group(1)}")
        last_index = match.end()
    if last_index is not None:
        sheets[-1] += "\n" + content[last_index:].strip()
    return sheets

# ファイルの読み込み
with open(input_file, "r", encoding="utf-8") as f:
    file_content = f.read()

# シート名ごとに分割
sheets = split_by_sheet_name(file_content)

# 埋め込みの生成
data_vectors = model.encode(sheets, convert_to_tensor=True)

# pickle ファイルに保存
with open(output_file, "wb") as f:
    pickle.dump(sheets, f)

print(f"Embeddings have been saved to {output_file}")

# FAISSインデックスの構築
# all_vectors = np.array(list(data_vectors.values()), dtype='float32')
index, vectors = build_faiss_index(data_vectors.tolist(), dimension=data_vectors.shape[1])

# FAISSインデックスを保存
faiss.write_index(index, "output/faiss_index.bin")
print("FAISS index has been saved to output/faiss_index.bin")