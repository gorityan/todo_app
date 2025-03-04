import threading
import webview
from app import app  # 先ほどの Flask アプリ

def run_flask():
    # Flask アプリを別スレッドで起動（ポート5000）
    app.run(debug=False, use_reloader=False)

if __name__ == '__main__':
    # Flask をバックグラウンドで起動
    threading.Thread(target=run_flask).start()
    # WebView を開く。URL は Flask のローカルサーバを指定
    webview.create_window("ToDoリストアプリ", "http://127.0.0.1:5000")
    webview.start()
