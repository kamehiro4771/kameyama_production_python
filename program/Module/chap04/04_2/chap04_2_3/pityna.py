import responder
class Pityna(object):
    """ピティナの本体クラス
    """
    def __init__(self,name):
        """インスタンス変数name、responderの初期化
        
        Args:
                name(str)   :Pitynaオブジェクトの名前
        """
        #Pitynaオブジェクトの名前をインスタンス変数に代入
        self.name = name
        #Responderオブジェクトを作成してインスタンス変数に代入
        self.responder = responder.RepeatResponder('Repeat')

    def dialogue(self, input):
        """応答オブジェクトのresponse()呼び出して応答文字列を取得する
        
        Args:
                input(str)  :ユーザーの発言
        Returns:
                str:応答メッセージ
        """
        return self.responder.response(input)
    def get_responder_name(self):
        """応答に使用されたオブジェクト名を返す
        
        Args:
                self(object):応答オブジェクトの名前
        """
        #responderに格納jされているオブジェクト名を返す
        return self.responder.name
    def get_name(self):
        """Pitynaオブジェクトの名前を返す
        
        Args:
                self(object):呼び出し元の  Pitynaオブジェクト
        Returns:
                str:    Pitynaクラスの名前
        """
        #Pitynaクラスの名前を返す
        return self.name