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

# -*- coding:utf-8 -*-

import os
from bottle import route, run


@route('/hello/')
def hello():
    return "Hello World"


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
