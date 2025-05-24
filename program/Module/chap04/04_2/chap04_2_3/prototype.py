import pityna#pitynaモジュールのインポート

"""実行ブロック
"""
def prompt(obj):
    """ピティナのプロンプトを作る関数
    
    
    Args:
        obj(object):呼び出し元のPitynaオブジェクト
　Returns:
        str:ピティナのプロンプト用の文字列
        """
    #「'Pitynaオブジェクト名:応答オブジェクト名>'」の文字列を返す
    return obj.get_name() + ':' + obj.get_responder_name() + '> '

#ここからプログラム開始
# プログラムの情報を出力
print('Pityna System prototype : Pityna')
#Pitynaオブジェクトを生成
pityna = pityna.Pityna('pityna')
#対話処理開始
while True:
    inputs = input(' > ')
    if not inputs:
        print('バイバイ')
        break
    #応答文字列を取得
    response = pityna.dialogue(inputs)
    #プロンプト文字列と応答文字列を連結して出力
    print(prompt(pityna),response)