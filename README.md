取り組みの全体フロー
1.	FastAPIでREST API実装
2.	SQLAlchemyでモデル定義&CRUD実装
3.	Railwayにデプロイ
4.	ProcfileでUvicorn起動設定
5.	requirements.txtに依存パッケージ
6.	RailwayのPostgreSQLにDB作成
7.	テスト実行して仕様確認


使用した言語＆フレームワーク
言語              Python 3.10.5
Webフレームワーク   FastAPI
ASGIサーバー       Uvicorn
ORM               SQLAlchemy
DBドライバ         psycopg2-binary (PostgreSQL)

クラウド&インフラ
ホスティング  Railway
データベース  Railwayが提供するPostgreSQL
Procfile    UvicornをASGIサーバとして起動

Pythonパッケージ（requirements.txtにも記載あり）
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-dotenv

DBスキーマ
sql/create.sqlをPostgreSQL用に調整
テーブル作成はBase.metadata.create_all()で初期化

補足
Railwayの環境変数にDATABASE_URLを登録
以下のURLに作成したソースコードを保管しています。
https://github.com/Manyason/puroject/tree/main
