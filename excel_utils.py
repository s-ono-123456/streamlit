import pandas as pd
import os

def load_data_from_excel(file_path: str) -> dict:
    """
    Excelファイルから全てのシートのデータを読み取る関数。

    Args:
        file_path (str): Excelファイルのパス。

    Returns:
        dict: シート名をキー、データを値とする辞書。
    """
    try:
        data = pd.read_excel(file_path, sheet_name=None)  # 全てのシートを読み取る
        return {sheet: df.values.tolist() for sheet, df in data.items()}
    except Exception as e:
        print(f"エラー: Excelファイルの読み取りに失敗しました: {e}")
        return {}

if __name__ == "__main__":
    # サンプルExcelファイルのパス
    sample_file_path = "sample/外部設計書_画面設計（あいうえお）.xlsx"

    # データを読み込む
    data = load_data_from_excel(sample_file_path)

    # 読み込んだデータを出力
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, "output.txt")

    if data:
        with open(output_file_path, "w", encoding="utf-8") as f:
            for sheet_name, rows in data.items():
                f.write(f"シート名: {sheet_name}\n")
                for row in rows:
                    f.write(f"{row}\n")
        print(f"データが {output_file_path} に書き出されました。")
    else:
        print("データが読み込めませんでした。")