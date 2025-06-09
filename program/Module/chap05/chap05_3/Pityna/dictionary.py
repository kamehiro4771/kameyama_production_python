import os

class Dictionary(object):
    """辞書用の2ファイルを開き、応答データをリストと辞書オブジェクトにそれぞれ格納する
    
    Attributes:
        random(list):ランダム辞書のフレーズを格納したリストを保持
        pattern(dict):パターン辞書のパターンと応答フレーズを格納する辞書オブジェクト
    """
    def __init__(self):
        """Dictionaryオブジェクトの初期化処理
        
        """
        #　ピティナのランダム辞書を作成
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
        """パターン辞書ファイルのデータを辞書オブジェクトpatternに格納
        
        Returns:
            dict:パターン辞書のパターンと応答フレーズを格納したdictオブジェクト  

        ・辞書オブジェクトpatternの構造
        {
            ・'pattern':[パターンのリスト]
            ・'phrases':[パターンに対応する応答フレーズのリスト]
        }
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
        
        # 1行をタブで切り分けて辞書オブジェクトpattern_dictに格納
        # 'pattern'キー：正規表現のパターン
        # 'pattern'キー：応答フレーズ（メッセージ）
        pattern_dict = {}
        for line in pattern_list:
            ptn,prs = line.split('\t')
            pattern_dict.setdefault('pattern',[]).append(ptn)
            pattern_dict.setdefault('phrases',[]).append(prs)
        return pattern_dict