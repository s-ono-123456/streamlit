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

def extract_text_from_excel(file_path):
    """
    指定されたExcelファイルを読み込み、各シートのテキストを抽出します。
    ただし、シート名に「改訂履歴」または「記載要領」が含まれる場合はスキップします。

    Args:
        file_path (str): Excelファイルのパス

    Returns:
        dict: シート名をキー、シート内のテキストを値とする辞書
    """
    extracted_data = {}

    # Excelファイルを読み込む
    excel_data = pd.ExcelFile(file_path)

    for sheet_name in excel_data.sheet_names:
        # シート名に「改訂履歴」または「記載要領」が含まれている場合はスキップ
        if "改訂履歴" in sheet_name or "記載要領" in sheet_name:
            continue

        # シートのデータをDataFrameとして読み込む
        sheet_data = excel_data.parse(sheet_name)

        # DataFrameを文字列に変換して保存
        extracted_data[sheet_name] = sheet_data.to_string(index=False)

    return extracted_data