import pandas as pd

def load_data_from_csv(file_path: str) -> list:
    """
    CSVファイルからデータを読み取る関数。

    Args:
        file_path (str): CSVファイルのパス。

    Returns:
        list: 読み取ったデータのリスト。
    """
    try:
        df = pd.read_csv(file_path)
        # 必要に応じて特定の列を選択
        return df.iloc[:, 0].tolist()
    except Exception as e:
        print(f"エラー: CSVファイルの読み取りに失敗しました: {e}")
        return []
