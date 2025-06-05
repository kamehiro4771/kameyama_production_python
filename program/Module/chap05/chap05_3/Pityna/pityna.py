import responder
import random

class Pityna(object):
    """ピティナの本体クラス
    """
    def __init__(self, name):
        """インスタンス変数name、responderの初期化
        
        Args:
            name(str):Pitynaオブジェクトの名前
        """
        #Pitynaオブジェクトの名前をインスタンス変数に代入
        self.name = name
        #　RandomResponderを生成
        self.res_random = responder.RandomResponder('Random')
        #　RepeatResponderを生成
        self.res_repeat = responder.RepeatResponder('Repeat')
        #　responderの初期値をRepeatResponderにする
        self.responder = self.res_repeat
        #Responderオブジェクトを生成してインスタンス変数に代入
        self.responder = responder.RandomResponder('Random')

    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して応答文字列を取得する
        
        Args:
            input(str)  :ユーザーの発言
        Returns:
            str:応答メッセージ
        """
        #　0か1をランダムに生成
        x = random.randint(0,1)
        #　RandomResponderをオブジェクトにする
        if x==0:
            self.responder = self.res_random
        #　以外ならRepeatResponder オブジェクトにする
        else:
            self.responder = self.res_repeat
        #　選択されたResponderオブジェクトからの応答を返す
        return self.responder.response(input)
    
    def get_responder_name(self):
        """応答に使用されたオブジェクト名を返す

        Args:
            self(object):呼び出し元のPitynaオブジェクト
        Return:
            str:応答オブジェクトの名前
        """
        #responderに格納されているオブジェクト名を返す
        return self.responder.name
    
    def get_name(self):
        """Pitynaオブジェクトの名前を返す
        
        Args;
            self(object):呼び出し元のPitynaオブジェクト
        Returns:
            str:Pitynaクラスの名前
        """
        #Pitynaクラスの名前を返す
        return self.name