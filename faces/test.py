# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_Faces(object):
    def setupUi(self, Faces):
        Faces.setObjectName("Faces")
        Faces.resize(414, 350)
        Faces.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        Faces.setFont(font)
        Faces.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Faces.setMouseTracking(True)
        Faces.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(Faces)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 460, 350))
        self.label.setSizeIncrement(QtCore.QSize(340, 340))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)
        self.label.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("图标/face2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 60, 110, 110))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setTabletTracking(True)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 220, 110, 110))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setTabletTracking(True)
        self.pushButton_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        Faces.setCentralWidget(self.centralwidget)
        self.pushButton_2.clicked.connect(self.faces)

        self.retranslateUi(Faces)
        self.pushButton_2.clicked.connect(Faces.show)
        self.pushButton_4.clicked.connect(Faces.close)
        QtCore.QMetaObject.connectSlotsByName(Faces)

    def retranslateUi(self, Faces):
        _translate = QtCore.QCoreApplication.translate
        Faces.setWindowTitle(_translate("Faces", "MainWindow"))
        self.pushButton_2.setText(_translate("Faces", "P: Start"))
        self.pushButton_4.setText(_translate("Faces", "Q: Exit"))

    def faces(self):
        import cv2
        import pickle
        import dlib

        detector = dlib.get_frontal_face_detector()

        face_cascade = cv2.CascadeClassifier('E:\\faces\\data\\haarcascade_frontalface_alt2.xml')
        eye_cascade = cv2.CascadeClassifier('E:\\faces\\data\\haarcascade_eye.xml')
        smile_cascade = cv2.CascadeClassifier('E:\\faces\\data\\haarcascade_smile.xml')

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("./recognizers/trainner.yml")


        labels = {"person_name": 1}
        with open("pickles/labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}

        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                # print(x,y,w,h)
                roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
                roi_color = frame[y:y + h, x:x + w]

                # keras
                id_, conf = recognizer.predict(roi_gray)
                if conf >= 4 and conf <= 85:
                    # print(5: #id_)
                    # print(labels[id_])
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

                img_item = "7.png"
                cv2.imwrite(img_item, roi_color)

                color = (255, 0, 0)  # BGR 0-255
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)


            # 展示结果
            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        # 释放frame
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Faces()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
