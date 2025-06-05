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