import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('시작 시간', self)
        self.lbl.move(120, 50)

        self.lbl = QLabel('중간 시간', self)
        self.lbl.move(120, 80)

        self.lbl = QLabel('끝 시간', self)
        self.lbl.move(120, 110)

        cb = QComboBox(self)
        for i in range(24):
            cb.addItem('%s시' % i, self)
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())