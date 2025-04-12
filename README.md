# Streamlit RAG 実装

このリポジトリは、StreamlitとFlaskを使用したRetrieval-Augmented Generation (RAG) のデモ実装を含んでいます。プロジェクトには、StreamlitベースのフロントエンドとFlaskベースのバックエンドが含まれています。

## プロジェクト構成

- `app.py`: クエリを受け付け、結果を表示するStreamlitアプリケーション。
- `server.py`: 言語モデルAPIをホストするFlaskサーバー。
- `.gitignore`: Gitで無視するファイルやディレクトリを指定。
- `Streamlit.code-workspace`: VS Codeのワークスペース設定ファイル。

## 機能

1. **Streamlit フロントエンド**:
   - ユーザーのクエリを受け付けます。
   - ダミーデータに対してFAISSを使用した類似性検索を実行します。
   - 検索結果とユーザーのクエリをバックエンドに送信し、言語モデル推論を行います。

2. **Flask バックエンド**:
   - 言語モデル推論用のAPIエンドポイントをホストします。
   - プロンプトを処理し、モデル生成の応答を返します。

## セットアップ手順

### 必要条件

- Python 3.8以上
- pip (Pythonパッケージマネージャー)

### インストール

1. リポジトリをクローンします:
   ```bash
   git clone <repository-url>
   cd Streamlit
   ```

2. 仮想環境を作成して有効化します:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
   ```

3. 依存関係をインストールします:
   ```bash
   pip install -r requirements.txt
   ```

### アプリケーションの実行

1. Flaskサーバーを起動します:
   ```bash
   python server.py
   ```

2. Streamlitアプリケーションを起動します:
   ```bash
   streamlit run app.py --server.fileWatcherType none
   ```

3. ブラウザで`http://localhost:8501`にアクセスして、Streamlitアプリを利用します。

## 新機能

### Excelデータの読み込み

- `excel_utils.py`:
  - Excelファイルを読み込み、全てのシートのデータを辞書形式で取得するユーティリティ。
  - 実行時に、読み取ったデータを`output/output.txt`に書き出します。

### 使用方法

1. サンプルExcelファイルを`sample/`ディレクトリに配置します。
2. 以下のコマンドで`excel_utils.py`を実行します:
   ```bash
   python excel_utils.py
   ```
3. 結果は`output/output.txt`に保存されます。

## 注意事項

- FAISSインデックスと言語モデルは現在ダミーデータとプレースホルダーを使用しています。本番環境で使用するには、実際の埋め込みデータとモデル統合に置き換えてください。
- Streamlitアプリを操作する前に、Flaskサーバーが起動していることを確認してください。
- `models--sentence-transformers--all-MiniLM-L6-v2.zip`はC:\Users\<ユーザー名>\.cache\huggingface\hub配下に配置することでローカルでも動くはずです。
- 出力ディレクトリ`output/`が存在しない場合、自動的に作成されます。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。

## 更新履歴

- 2025年4月9日: 初期バージョンのREADMEを作成しました。