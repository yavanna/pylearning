# coding: UTF-8
# 行末までコメント

# データ型
# 数値、真偽値、None、関数・オブジェクト
# 要素が並んだもの
# - 文字列・・・文字が並んだもの
# - リスト・・・データが並んだもの
# - タプル・・・データが並んだもの（変更が出来ない）
# - セット・・・データが並んだもの（重複を許さない）
# - 辞書・・・キーと値がペア

import numpy as np  # デモ用データ生成用。本題とはあまり関係ない。  
import matplotlib.pyplot as plt  # 今日の話題の中心となる2Dプロッティングライブラリ   
import matplotlib.cm as cm  # グラフに使う色を細かく指定するためのクラス
from IPython.display import Image  # 図をノートブックにインポートするためのクラス

plt.rcParams['font.size'] = 14 #フォントサイズを設定

x = np.array(range(1, 25))
y1 = np.random.normal(20, 5, 24)
y2 = np.random.normal(30, 5, 24)
y3 = np.random.normal(40, 5, 24)
y4 = np.random.normal(50, 5, 24)
y5 = np.random.normal(60, 5, 24)