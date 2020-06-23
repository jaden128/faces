import test
Ui_MainWindow = test.Ui_Faces
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class CoperQt(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_MainWindow.__init__(self,*args,**kwargs)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象

        self.setWindowTitle("Face_recognition")


    def keyPressEvent(self, q):
        if q.key() == Qt.Key_q:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoperQt()  # 创建QT对象
    window.show()  # QT对象显示
    sys.exit(app.exec_())