# Analyze SisFall

SisFall datasetを用いて、転倒検知・ヒヤリハット検知の評価を行う

# dependencies

- python >= 3.6
- numpy  >= 1.15.4
- pandas >= 0.23.4
- matplotlib >= 3.0.2
- pytest >= 4.0.1
- plotly >= 3.4.2

# TODO

- [x] データセット読み込み
    
    - [x] ファイル一覧取得
    - [x] ファイル名からラベル取得
    - [x] ラベルと動作名の辞書ファイル作成
    - [x] ラベルから動作取得
    - [x] ファイルから加速度データ取得
    - [x] 時刻追加
    - [x] 加速度データに対するラベリング処理
- [x] データセットの可視化
- [ ] 転倒検知をPythonで実装
- [ ] ヒヤリハット検知をPythonで実装
- [ ] アルゴリズムの評価
