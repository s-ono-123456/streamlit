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

3. **データ処理**:
   - `excel_utils.py`を使用して、Excelファイルを読み込み、全てのシートのデータをMarkdown形式で処理します。
   - 処理結果を`output/content.md`に書き出します。
   - `process_sample1.py`を使用して、Markdownファイル（`output/sample1.md`）を読み込み、シート名ごとにデータを分割し、`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`モデルを用いて埋め込みを生成します。
   - 生成した埋め込みは`output/sample1_embeddings.pkl`に保存されます。

## 使用方法

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

4. データ処理を行うには以下を実行します:
   - Excelデータを処理するには、サンプルExcelファイルを`sample/`ディレクトリに配置し、以下のコマンドを実行します:
     ```bash
     python excel_utils.py
     ```
     結果は`output/content.md`に保存されます。
   - Markdownデータを処理するには、以下のコマンドを実行します:
     ```bash
     python process_sample1.py
     ```
     結果は`output/sample1_embeddings.pkl`に保存されます。

## 注意事項

- FAISSインデックスと言語モデルは現在ダミーデータとプレースホルダーを使用しています。本番環境で使用するには、実際の埋め込みデータとモデル統合に置き換えてください。
- Streamlitアプリを操作する前に、Flaskサーバーが起動していることを確認してください。
- `models--sentence-transformers--all-MiniLM-L6-v2.zip`はC:\Users\<ユーザー名>\.cache\huggingface\hub配下に配置することでローカルでも動くはずです。
- 出力ディレクトリ`output/`が存在しない場合、自動的に作成されます。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。

## 更新履歴

- 2025年4月12日: `process_sample1.py` を追加し、Markdownデータの埋め込み生成機能を実装しました。
- 2025年4月12日: `requirements.txt` に `sentence-transformers` と `sentencepiece` を追加しました。
- 2025年4月12日: `excel_utils.py`を更新し、Excelデータの読み込み結果を`content.md`に出力するよう変更しました。
- 2025年4月9日: 初期バージョンのREADMEを作成しました。