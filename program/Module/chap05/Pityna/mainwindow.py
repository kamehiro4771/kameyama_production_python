from PyQt5 import QtWidgets
import qt_PitynaUI
#import Pityna

class MainWindow(QtWidgets.QMainWindow):
    """QtWidgets.QMainWindowを継承したサブクラス
    UI画面の構築を行う
    Attributes:
        pityna(obj):Pitynaオブジェクトを保持
        action(bool):ラジオボタンの状態を保持
        ui(obj):UI_MainWindowオブジェクトを保持
    """
    def __init__(self):
        """初期化処理
        """
        #スーパークラスの__init__()を実行
        super().__init__()
        # Pitynaオブジェクトを生成
 #       self.pityna = pityna.Pityna("pityna")
        #ラジオボタンの状態を初期化
        self.action = True
        # Ui_MainWindowオブジェクトを生成
        self.ui = qt_PitynaUI.Ui_MainWindow()
        # setupUi()で画面の構築、MainWindow自身を引数にすることが必要
        self.ui.setupUi(self)

    def putlog(self, str):
        """QListWidgetクラスのaddItem()でログをリストに追加する
        
        Args:
            str(str):ユーザーの入力または応答メッセージをログ用に成形した文字列
        """
        self.ui.ListWidgeLog.addItem(str)

    def prompt(self):
        """ピティナのプロンプトを作る

        Returns:
            str:プロンプトを作る文字列
        """
        #Pitynaクラスのget_name()でオブジェクト名を取得
        p = self.pityna.get_name()
        #「Responderを表示」がオンならオブジェクト名を追加する
        if self.action == True:
            p += ':' + self.pityna.get_responder_name()
        #プロンプト記号を付けて返す
        return p + '>'

    def button_talk_slot(self):
        """[話す]ボタンのイベントハンドラー
        
        ・Pitynaクラスのdialogue()を実行して応答メッセージを取得
        ・入力文字列および応答メッセージをログに出力
        """
        #ラインエディットがユーザーの発言を取得
        value = self.ui.LineEdit.text()
        if not value:
            #未入力の場合は「何？」と表示
            self.ui.LabelResponce.setText('')
        else:
            #発言があれば対話オブジェクトを実行
            #ユーザーの発言を引数にしてdialogue()を実行し、応答メッセージを取得
            response = self.pityna.dialogue(value)
            #ピティナの応答メッセージをラベルに出力
            self.ui.LabelResponce.setText(response)
            #プロンプト記号にユーザーの発言を連結してログ用のリストに出力
            self.putlog('>'+value)
            #ピティナのプロンプト記号に応答メッセージを連結してログ用のリストに出力
            self.putlog(self.prompt() + response)
            #QLineEditクラスのclear()メソッドでラインエディットのテキストをクリア
            self.uiLineEdit.clear()

    def closeEvent(self, event):
        """ウィジェットを閉じるclose()メソッド実行時にQCloseEventによって呼ばれる
        
        Overrides:
            ・メッセージボックスを表示する
            ・「Yes」がクリックされたらイベントを続行してウィジェットを閉じる
            ・「No」がクリックされたらイベントを取り消してウィジェットを閉じないようにする
        Args:
            event(obj):閉じるイベント発生時に渡されるQCloseEventオブジェクト

        """
        reply = QtWidgets.QMessageBox.question(
            self,
            '確認',#タイトル
            "プログラムを終了しますか？",#メッセージ
            #Yes|Noボタンを表示
            buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

    #[Yes]クリックでウィジェットを閉じ、[No]クリックで閉じる処理を無効にする
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()#イベント続行
        else:
            event.ignore()#イベント取り消し
    def show_responder_name(self):
        """RadioButton_1がオンの時に呼ばれるイベントハンドラー
        
        """
        #ラジオボタンの状態を保持するactionの値をTrueにする
        self.action = True

    def hidden_responder_name(self):
        """RadioButton_2がオンの時に呼ばれるイベントハンドラー
        
        """
        #ラジオボタンの状態を保持するactionの値をFalseにする
        self.action = False