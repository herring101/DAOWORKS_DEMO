# daoworks-demo

DAOWORKSの動作確認のためのリポジトリです。
DAOWORKSの機能を使い、自動で Pull Request の評価を行います。

このレポジトリでは簡単なTODOアプリの開発をシミュレーションしています。

## 最初の機能

- ユーザーが新しいタスクをリストに追加できる。
- ユーザーがタスクをリストから削除できる。
- ユーザーがタスクの完了状態をダブルクリックで切り替えることができる（未完了から完了へ、またはその逆）。

## 追加の機能

それぞれ Issue と Pull Request を作成する

- タスクの優先順位設定
- 期限の追加
- リマインダーの設定

## 実行方法

このプロジェクトでは、rye というパッケージ管理ツールを使用しています。
インストール方法は [ここ](https://rye-up.com/guide/installation/#installing-rye) を参照してください。

windows での実行方法は以下の通りです。

```pwsh
rye sync
.venv\Scripts\activate
python .\src\daoworks_demo\main.py
```

Unix 系 OS での実行方法は以下の通りです。

```sh
rye sync
. .venv/bin/activate
python ./src/daoworks_demo/main.py
```
