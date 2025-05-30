from PyQt5 import uic
import os

# qt_PitynaUI.uiのフルパスを取得
path_ui = os.path.join(os.path.dirname(__file__),'qt_PitynaUI.ui')
#Qt Designerの出力ファイルを読み取りモードでオープン
fin = open('chap05/Pityna/qt_PitynaUI.ui','r',encoding='utf-8')
# qt_Pitynaui.pyのフルパス取得
path_py = os.path.join(os.path.dirname(__file__),'qt_pitynaui.py')
# Python形式ファイルを書き込みモードでオープン
fout = open('chap05/Pityna/qt_PitynaUI.py','w',encoding='utf-8')
# コンバートを開始
uic.compileUi(fin, fout)
#2つのファイルをクローズ
fin.close()
fout.close()