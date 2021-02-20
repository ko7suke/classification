# Classification
 __画像を分類 (指定) するアプリケーションです.__

## _使い方_  
1. ターミナル内で任意のファルダに移動し, `git clone https://github.com/ko7suke/classification.git` を実行してください.
1. ターミナルでクローンしたフォルダに移動し, `docker build .` を実行してください.
1. ビルド完了後, `docker run -it -v <クローンしたフォルダまでの絶対パス>/classification/classification/:/work -p 8000:8000 <IMAGE ID>` を実行してください. `IMAGE ID` がわからない場合は `docker images` コマンドを実行し、IMAGE　IDを確認してください.
1. `127.0.0.1:8000/classify` へアクセスし, 画像分類アプリをお試しください。
 
## _その他_
* オリジナルの分類器を作ることも可能です. 詳細は後ほど記載します.
