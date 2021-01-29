import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QComboBox, QFileDialog


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('시작: ', self)
        self.lbl1.move(120, 50)

        self.lbl2 = QLabel('   끝: ', self)
        self.lbl2.move(120, 80)

        self.lbl3 = QLabel('', self)  # 시작 시간 표시
        self.lbl3.move(150, 50)

        self.lbl4 = QLabel('', self)  # 끝 시간 표시
        self.lbl4.move(150, 80)

        self.lbl5 = QLabel('주소', self)  # 그림 주소 표시
        self.lbl5.move(150, 110)

        btn1 = QPushButton('Wallpaper', self)  # 그림 주소 설정
        btn1.setCheckable(True)
        btn1.move(50, 105)
        btn1.pressed.connect(self.SelectWallpaper)

        # btn2 = QPushButton("미리보기", self)
        # btn2.setCheckable(True)
        # btn2.move(120, 105)
        # btn2.pressed.connect(self.PreView)


        cb1 = QComboBox(self)
        for i in range(24):
            cb1.addItem('%s시' % i, self)
        cb1.move(50, 45)

        cb2 = QComboBox(self)
        for i in range(24):
            cb2.addItem('%s시' % i, self)
        cb2.move(50, 75)

        cb1.activated[str].connect(self.onActivated1)
        cb2.activated[str].connect(self.onActivated2)

        self.setWindowTitle('Wallpaper Changer')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated1(self, text):
        self.lbl3.setText(text)
        self.lbl3.adjustSize()

    def onActivated2(self, text):
        self.lbl4.setText(text)
        self.lbl4.adjustSize()

    def SelectWallpaper(self):
        fileName = QFileDialog.getOpenFileName(self, self.tr("Open Data files"), "./", self.tr("Images (*.png *.jpg *.jpeg);; All Files(*.*)"))
        self.lbl5.setText(fileName)
        self.lbl5.adjustSize()

    # def PreView(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())