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
   streamlit run app.py
   ```

3. ブラウザで`http://localhost:8501`にアクセスして、Streamlitアプリを利用します。

## 注意事項

- FAISSインデックスと言語モデルは現在ダミーデータとプレースホルダーを使用しています。本番環境で使用するには、実際の埋め込みデータとモデル統合に置き換えてください。
- Streamlitアプリを操作する前に、Flaskサーバーが起動していることを確認してください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。