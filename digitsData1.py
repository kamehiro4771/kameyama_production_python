import sklearn.datasets

digits = sklearn.datasets.load_digits()

for i in range(10):
    print("データの個数＝",len(digits.images))
    print("画像のデータ＝",digits.images[i])
    print("何の数字か＝",digits.target[i])
