import os
import random
import re

class Dictionary(object):
    """辞書用の2ファイルを開き、応答データをリストと辞書オブジェクトにそれぞれ格納する
    
    Attributes:
        random(list):ランダム辞書の全てのフレーズを要素として格納
        [フレーズ１,フレーズ２,フレーズ３,...]

        pattern(PatternItemのlist)：
            [PatternItem1,PatternItem2,PatternItem,3,...]
    """
    def __init__(self):
        """インスタンス変数randomとpatternの初期化
        
        """
        #ランダム辞書のメッセージのリストを作成
        self.random = self.make_random_list()
        #ピティナのパターン辞書を作成
        self.pattern = self.make_pattern_dictionary()

    def make_random_list(self):
        """ランダム辞書ファイルのデータを読み込んでリストrandomに格納する

            Returns:
                list:ランダム辞書の応答フレーズを格納したリスト
        """
        #   random.txtのフルパスを取得
        path = os.path.join(os.path.dirname(__file__), 'dics','random.txt')
        #   ランダム辞書ファイルオープン
        rfile = open(path, 'r', encoding = 'utf_8')
        #   各行を要素としてリストに格納
        r_lines = rfile.readlines()
        #   ファイルオブジェクトをクローズ
        rfile.close()
        #   末尾の開業と空白文字を取り除いてリストrandom_listに格納
        random_list = []
        for line in r_lines:
            str = line.rstrip('\n')
            if(str != ''):
                random_list.append(str)

        return random_list
    def make_pattern_dictionary(self):
        """パターン辞書ファイルのデータを読み込んでリストpatternitem_listに格納する
        
        Returns:
            PatternItemのlist:PatternItemはパターン辞書1行のデータを持つ
        """
        #   pattern.txtのフルパスを取得
        path = os.path.join(os.path.dirname(__file__),'dics','pattern.txt')
        #   パターン辞書オープン
        pfile = open(path, 'r',encoding = 'utf_8')
        #   各行を要素としてリストに格納
        p_lines = pfile.readlines()
        #   ファイルオブジェクトをクローズ
        pfile.close()
        #   末尾の開業と空白文字を取り除いてpattern_listに格納
        pattern_list = []
        for line in p_lines:
            str = line.rstrip('\n')
            if(str != ''):
                pattern_list.append(str)
        
        # パターン辞書の各行をタブで切り分けて以下の変数に格納
        #
        # ptnパターン辞書1行の正規表現パターン
        # prsパターン辞書1行の応答フレーズグループ
        #
        #ptn,prsを引数にしてPatternItemオブジェクトを1っこ生成し、patternitem_listに追加
        #パターン辞書の行の数だけ繰り返す
        patternitem_list= []
        for line in pattern_list:
            ptn,prs = line.split('\t')
            patternitem_list.append(PatternItem(ptn,prs))
        return patternitem_list

class PatternItem:
    """パターン辞書1行の情報を保持するクラス
    
    Attributes:すべて「パターン辞書1行」のデータ
        modify(int):機嫌値
        pattern(str):正規表現パターン
        phrases(dictのlist):
            リスト要素の辞書は”応答フレーズ１個”の情報を持つ
            辞書の数は1行の応答フレーズグループの数と同じ
            ｛’need’：必要機嫌値,’phrases’：’応答フレーズ1個’｝
    """
    SEPARATOR = '^((-?\d+)##)?(.*)$'

    def __init__(self,pattern,phrases):
        """パターン辞書1行の情報を保持するクラス

        Args:
            pattern(str):パターン辞書１行の正規表現パターン（機嫌変動値##パターン）
            phrases(dicのlist):パターン辞書1行の応答フレーズグループ
        """
        #インスタンス変数modify,patternの初期化
        self.init_modifypattern(pattern)

    