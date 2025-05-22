class Pityna:
    """ピティナの本体クラス
    """
    def __init__(self, name):
        """インスタンス変数name、responderの初期化
        Args:
            name(str):Pitynaオブジェクトの名前
        """
        #Pitynaオブジェクトの名前をインスタンス変数に代入
        self.name = name
        #Responderオブジェクトを生成してインスタンス変数に代入
        self.responder =Responder('Repeat')
    
    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して応答文字列を取得する
        Args:
                i nput(str):ユーザーの発言

        Returns:
                 str:応答文字列
        """
        #response()メソッドを実行し、戻り値（応答文字列）をそのまま返す
        return self.responder.response(input)
    
    def get_responder_name(self):
        """応答に使用されたオブジェクト名を返す
        
        Returns:
            str:応答オブジェクトの名前
        """
        #response()メソッドを実行し、戻り値（応答文字列）をそのまま返す
        return self.responder.name
    
    def get_name(self):
        """Pitynaオブジェクトの名前を返す

        Returns:
            str: Pitynaクラスの名前
        """
        #Pitynaクラスの名前を取得し戻り値にする
        return self.name
    
class Responder:
    """応答クラス
    """
    def __init__(self,name):
        """Responderオブジェクトの名前をnameに格納
        
        Args:
            name(str) :Responderオブジェクトの名前
        """
        self.name = name
    def response(self, input):
        """応答文字列を作って返す

        Args:
            input(str):ユーザーが入力した文字列
        Returns:
            str:   応答メッセージ
        """
        #オウム返しの返答をする
        return "{}ってなに？".format(input)
###########################################################################
#実行ブロック
###########################################################################
def prompt(obj):
    """ピティナのプロンプトを作る関数
    
    Args:
            obj(object):呼び出し元のPitynaオブジェクト
    Returns:
            str:ピティナのプロンプト用の文字列
    """
    #「'Pitynaオブジェクト名:応答オブジェクト名>'」の文字列を返す
    return obj.get_name() + ':'  + obj.get_responder_name() + '> '
#ここからプログラム開始
#プログラムの情報を表示
pityna = Pityna('Pityna')
print('Pityna System prototype : Pityna')

#対話処理開始
while True:
    inputs = input(' > ')
    if not inputs:
        print('バイバイ')
        break
    else:
        #応答文字列を取得
        response = pityna.dialogue(inputs)
        #プロンプトと応答文字列をつなげて表示
        print(prompt(pityna), response)