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
        self.responder = Responder('Repeat')
    
    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して応答文字列を取得する

        Args:


        Args:
            input(str):ユーザーの発言

        Returns:
            str:応答文字列
        """
        #response()メソッドを実行し、戻り値（応答文字列をそのまま返す
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
    def ___init___(self,name):
        