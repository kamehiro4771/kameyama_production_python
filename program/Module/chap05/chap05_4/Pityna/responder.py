import random
import re

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
    def __init__(self,name):
        """スーパークラスの__init()__の呼び出しのみを行う
        
        Arags:
                name(str):応答クラスの名前
        """
        super().__init__(name)

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
    def __init__(self,name,dic_random):
        """スーパークラスの__init__()にnameを渡し、
           ランダム応答用のリストをインスタンス変数に格納する
        Args:
                        name(str) :応答クラスの名前
                        dic_random(list):Dictionaryオブジェクトが保持するランダム応答用のリスト 
        """
        super().__init__(name)
        self.random = dic_random

    def response(self,input):
        """response()をオーバーライド、ランダムな応答を返す
        
        Args:
                input(str)      :ユーザーが入力した文字列
        Returns:
                str:    リストからランダムに抽出した文字列
        """
        #リストresponsesからランダムに抽出して戻り値として返す
        return (random.choice(self.random))
    
class PatternResponder(Responder):
        """パターンに反応するためのサブクラス
        """
        def __init__(self,name,dictionary):
                """スーパークラスの__init__()にnameを渡し、
                Dictionaryオブジェクトをインスタンス変数に格納する

                Args:
                        name(str)       :Responderオブジェクトの名前
                        dictionary(dic):Dictionaryオブジェクト

                """
                super().__init__(name)
                self.dictionary = dictionary

        def response(self,input):
                """パターンにマッチした場合に応答フレーズを抽出して返す
                Args:
                        input(str):ユーザーの発言

                Returns:str:
                        パターンにマッチした場合はパターンと対になっている応答メッセージを返す
                        パターンにマッチしない場合はランダム辞書の応答メッセージを返す
                """
                # Pattern['pattern']とpattern['phrases']に対して反復処理
                for ptn, prs in zip(
                        #ptnに正規表現のパターンに代入する
                        self.dictionary.pattern['pattern'],
                        #prsパターンに対応する応答メッセージを代入する
                        self.dictionary.pattern['phrases']
                ):
                        m = re.search(ptn,input)
                        if m:
                        #ユーザーの発言の一部がパターンにマッチしている場合は、
                        #prsの応答フレーズを'|'で区切り分けてランダムに一文を取り出す
                                resp = random.choice(prs.split('|'))
                        #抽出した応答フレーズを返す
                        #応答フレーズの中に%match%が埋め込まれていた場合は、
                        #インプットされた文字列内のパターンマッチした文字列に置き換える
                                return re.sub('%match%',m.group(), resp)
                #パターンマッチしない場合はランダム辞書から返す
                return random.choice(self.dictionary.random)
                
