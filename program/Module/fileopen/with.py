import os

#   random.txtのフルパスを取得
path = os.path.join(os.path.dirname(__file__),'dics','random.txt')
#   ファイルオブジェクトをfileに保持し、内方表記を使って要素末尾の\nを削除
with open(path,'r',encoding = 'utf_8') as file:
    list = [elm.rstrip() for elm in file.readlines()]
    print(list)