from flask import Flask, jsonify, make_response
from flask.helpers import safe_join
# from flask_cors import CORS #別オリジンからのアクセスの時だけいる（開発のみ）
# MySQLdbのインポート
import MySQLdb
# 環境変数用
import os
# json読み込み用
import json

api = Flask(__name__)
# CORS(api)

@api.route('/users', methods=['GET'])
def get_user():
    json_load = json.load(open('db_env.json', 'r'))
    if os.environ.get('SABI_ENV')=='production':
        db_host = json_load['production']['db_host']
        db_user = json_load['production']['db_user']
        db_password = json_load['production']['db_password']
        db_db = json_load['production']['db_db']
    else:
        db_host = json_load['development']['db_host']
        db_user = json_load['development']['db_user']
        db_password = json_load['development']['db_password']
        db_db = json_load['development']['db_db']    
    # データベースへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        db=db_db)
    print(os.environ.get('SABI_ENV'))
    print(db_host)
    cursor = connection.cursor()
    # ここに実行したいコードを入力します
    cursor.execute("create table users (id int, name varchar(64))")
    cursor.execute("insert into users values (3,'aaa'),(4,'あa')")
    cursor.execute("SELECT * FROM users")
    # fetchall()で全件取り出し
    rows = cursor.fetchall()
    print(rows)
    # 保存を実行
    connection.commit()
    # 接続を閉じる
    connection.close()
    result = {
        "user": rows
    }
    return make_response(jsonify(result))

print('hello')

api.run(host='0.0.0.0', port=3000)