from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget() #创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout() #创建主部件网格布局
        self.main_widget.setLayout(self.main_layout) # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget() #创建左侧部件
        self.left_widget.setObjectName('left_widget') #起名
        self.left_layout = QtWidgets.QGridLayout() #创建左侧网格布局
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格布局

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widet')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget,0,0,12,2)
        self.main_layout.addWidget(self.right_widget,0,2,12,10)
        self.setCentralWidget(self.main_widget)

        self.left_close = QtWidgets.QPushButton("")
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")

        self.left_label_1 = QtWidgets.QPushButton("每日推荐")
        self.left_label_1.setObjectName()
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
