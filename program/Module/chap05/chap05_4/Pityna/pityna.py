import responder
import random
import dictionary

class Pityna(object):
    """ピティナの本体クラス
    Attributes:
        name(str):Pitynaオブジェクトの名前を保持
        dictionary(obj:'Dictionary'):Dictinaryオブジェクトを保持
        res_repeat(obj:'RepeatResponder'):RepeatResponderオブジェクトを保持
        res_random(obj:'RandomResponder'):RandomResponderオブジェクトを保持
        respattern(obj:'PatternResponder'):PatternResponderオブジェクトを保持
    """
    def __init__(self, name):
        """Pitynaオブジェクトの名前をnameに格納
        　Responderオブジェクトを生成してresponderに格納
        
        Args:
            name(str):Pitynaオブジェクトの名前
        """
        #Pitynaオブジェクトの名前をインスタンス変数に代入
        self.name = name
        #Dictionaryを生成
        self.dictionary = dictionary.Dictionary()
        #　RepeatResponderを生成
        self.res_repeat = responder.RepeatResponder('Repeat?')
        #　RandomResponderを生成
        self.res_random = responder.RandomResponder(
            'Random',self.dictionary.random)
        #PatternResponderを生成
        self.res_pattern = responder.PatternResponder(
            'Pattern',self.dictionary
        )

    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して応答文字列を取得する
        
        Args:
            input(str)  :ユーザーの発言
        Returns:
            str:応答メッセージ
        """
        #　1~100の数値をランダムに生成
        x = random.randint(1,100)
        #　60以下ならPatternResponderをオブジェクトにする
        if x<=60:
            self.responder = self.res_pattern
        #　61~90以下ならRandomResponder オブジェクトにする
        elif 61<=x<=90:
            self.responder = self.res_random
        #それ以外はRepeatResponderオブジェクトにする
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

class Emotion:
    """ピティナの感情クラス
    
    Attributes:
        pattern(PatternItemのlist):[PatternItem1,patternItem2,PatternItem3,...]
        mode(int):ピティナの機嫌値を保持
    """
    #機嫌値の上限／加減と回復値をクラス変数として定義
    MOOD_MIN = 15
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5

    def __init__(self,pattern):
        """インスタンス変数patternとmoodを初期化する

        Args:
            pattern(dict):Dictionaryのpattern（中身はpatternItemのリスト）
        """
        #Dictionaryオブジェクトのpatternをインスタンス変数patternに格納
        self.pattern = pattern
        #機嫌値moodを0で初期化
        self.mood = 0

    def update(self, input):
        """機嫌値を変動させるメソッド
        ・機嫌値をプラス／マイナス側にMOOD＿RECOVERYの値だけ戻す
        ・ユーザーの発言をパターン辞書にマッチさせ、機嫌値を変動させる

        Args:
            input (str):ユーザーの発言
        """
        #　機嫌値を徐々に戻す処理
        if self.mood < 0:
            self.mood += Emotion.MOOD_RECOVERY
        elif self.mood > 0:
            self.mood -= Emotion.MOOD_RECOVERY
        
        #　パターン辞書の各行の正規表現をユーザーの発言を繰り返しパターンマッチさせる
        #　マッチした場合はadjust_mood()で機嫌値を変動させる
        for ptn_item in self.pattern:
            if ptn_item in self.pattern:
                self.adjust_mood(ptn_item.modify)
                break
        
    def adjust_mood(self,val):
        """機嫌値を増減させるメソッド
        
        Args:
            val(int):機嫌変動値
        """
        #   機嫌値moodの値を機嫌変動値によって増減する
        self.mood += int(val)
        # MOOD_MAXとMOOD_MINと比較して、機嫌値がとり得る範囲に収める
        if self.mood > Emotion.MOOD_MAX:
            self.mood = Emotion.MOOD_MAX
        elif self.mood < Emotion.MOOD_MIN:
            self.mood = Emotion.MOODMIN