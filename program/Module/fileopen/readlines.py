import os

#   random.txtのフルパスを取得
path = os.path.join(os.path.dirname(__file__),'dics','random.txt')
file = open(path,'r',encoding = 'utf_8')
#   1行ずつリストの要素として読み込む
lines = file.readlines()
file.close()
print(lines)