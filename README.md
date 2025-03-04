# ToDoリストアプリ

シンプルで使いやすいToDoリスト管理アプリケーションです。タスクの追加、完了マーク、カレンダー表示などの機能を備えています。

## 機能

- タスクの追加（タスク名と期限日の設定）
- タスクの完了/未完了の管理
- カレンダー表示でタスクのスケジュール確認
- タスクの削除

## スクリーンショット

_※スクリーンショットがある場合は、ここに追加してください_

## インストール方法

### 前提条件

以下のソフトウェアがインストールされている必要があります：

- Python 3.7以上
- pip（Pythonパッケージマネージャー）

### インストール手順

1. このリポジトリをクローンまたはダウンロードします
   ```
   git clone https://github.com/yourusername/todo-list-app.git
   cd todo-list-app
   ```

2. 必要なパッケージをインストールします
   ```
   pip install -r requirements.txt
   ```

3. デスクトップアプリとして使用する場合は、追加で以下のパッケージをインストールします
   ```
   pip install pywebview
   ```

## 使用方法

### Webアプリケーションとして実行

```
python app.py
```

ブラウザで http://127.0.0.1:5000 にアクセスしてアプリケーションを使用できます。

### デスクトップアプリケーションとして実行

```
python desktop.py
```

または、Windowsの場合は `run_app.bat` ファイルをダブルクリックして実行できます。
※実行前に `run_app.bat` 内のパスを適切に修正してください。

## アプリの使い方

1. **タスクの追加**
   - 「タスク」フィールドにタスク名を入力
   - 「期限」フィールドで日付を選択
   - 「追加」ボタンをクリック

2. **タスクの管理**
   - タスクを完了したら「完了」ボタンをクリック
   - 完了したタスクを元に戻すには「戻す」ボタンをクリック
   - タスクを削除するには「削除」ボタンをクリック

3. **カレンダー表示**
   - 「カレンダー表示」ボタンをクリックして、タスクをカレンダー形式で確認
   - カレンダーから「戻る」ボタンで一覧表示に戻る

## 技術仕様

- **バックエンド**: Flask (Python)
- **データベース**: SQLite
- **ORM**: SQLAlchemy
- **フロントエンド**: HTML, CSS, JavaScript
- **UI フレームワーク**: Bootstrap 4
- **カレンダー表示**: FullCalendar
- **デスクトップアプリ化**: PyWebView

## プロジェクト構成

- `app.py` - Flask アプリケーションのメインファイル
- `desktop.py` - デスクトップアプリケーション用のラッパー
- `templates/` - HTMLテンプレートファイル
  - `index.html` - メイン画面のテンプレート
  - `calendar.html` - カレンダー表示のテンプレート
- `todo.db` - SQLiteデータベースファイル（自動生成）
- `requirements.txt` - 必要なPythonパッケージのリスト
- `run_app.bat` - Windowsでの実行用バッチファイル

## カスタマイズ

データベースの場所やその他の設定を変更するには、`app.py` の以下の部分を編集してください：

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'todo.db')
```

## ライセンス

_※適切なライセンス情報を追加してください_

## 貢献方法

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 作者

gorityan
