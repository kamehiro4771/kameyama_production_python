import os

#   random.txtのフルパスを取得
path = os.path.join(os.path.dirname(__file__),'dics','random.txt')
#   dicsフォルダーのrandom.txtを読み取りモードで開く
file = open(path,'r',encoding = 'utf_8')
#   ファイル終端までのすべてのデータを取得する
data = file.read()
#   ファイルオブジェクトをクローズ
file.close()
#   取得したデータを出力
print(data)