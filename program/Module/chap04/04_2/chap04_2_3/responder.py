import random

class Responder(object):
    """応答クラスのスーパークラス
    """
    def __init__(self,name):
        """ Responderオブジェクトの名前をnameに格納

        Args:
            name (str): Responderオブジェクトの名前
        """
        self.name = name

    def response(self, input):
        """オーバライドを前提としたresponse()メソッド
        
        Args:
                input(str) :    ユーザーの発言
        Returns:
                str:応答メッセージ（ただしからの文字列）        
        """
        return ''
class RepeatResponder(Responder):
    """オウム返しのためのサブクラス
    """
    def response(self, input):
        """をオーバーライド、オウム返しの返答をする
        
        
        Args:
                input(str):ユーザーの発言
        Returns:
                str:応答メッセージ        
        """
        #オウム返しの返答をする
        return '{}って何？'.format(input)
class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス
    """
    def __init__(self,name):
        """ランダムに抽出するメッセージのリストを作成する
        Args:
                        name(str)       : Responderオブジェクトの名前
        """
        #スーパークラスの初期化メソッドを呼んでResponder名をnameに格納
        super().__init__(name)
        #ランダム応答用のメッセージリストを用意
        self.responses = ['いい天気だね','なんとなくそう思う','10円ひろった']

    def response(self,input):
        """response()をオーバライド、ランダムな応答を返す
        
        Args:
                input(str)      :ユーザーが入力した文字列
        Returns:
                str:    リストからランダムに抽出した文字列
        """
        #リストresponsesからランダムに抽出して戻り値として返す
        return (random.choice(self.responses))