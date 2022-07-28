##################################################
# No one reads it anyway
##################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import subprocess
import sys
import sqlite3 as sql


style_sheet = """
    QLineEdit:focus {
        background-color: rgba(214, 224, 234, 1);
        border: 1px solid black;
    }
"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 101, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 101, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 101, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 101, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it())
        self.loginbutton.setEnabled(True)
        self.loginbutton.setGeometry(QtCore.QRect(90, 250, 220, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.loginbutton.setFont(font)
        self.loginbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginbutton.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/user-login-icon-14.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginbutton.setIcon(icon)
        self.loginbutton.setStyleSheet(open('stylesheet_log_reg.css').read())
        self.loginbutton.setIconSize(QtCore.QSize(30, 30))
        self.loginbutton.setCheckable(False)
        self.loginbutton.setAutoDefault(False)
        self.loginbutton.setDefault(False)
        self.loginbutton.setFlat(False)
        self.loginbutton.setObjectName("loginbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 120, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.registerbutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.register_it())
        self.registerbutton.setGeometry(QtCore.QRect(160, 300, 91, 23))
        self.registerbutton.setStyleSheet(open('stylesheet_log_reg.css').read())
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pics/add-user-icon-png-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.registerbutton.setIcon(icon1)
        self.registerbutton.setIconSize(QtCore.QSize(18, 18))
        self.registerbutton.setObjectName("registerbutton")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(50, 140, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(50, 200, 300, 35))
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-100, 60, 501, 291))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pics/8e77dd6a09ce0f0a31bd7d077321dd7b-growing-colorful-lines-chart.png"))
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.loginbutton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.registerbutton.raise_()
        self.username.raise_()
        self.password.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.loginbutton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.label_3.setText(_translate("MainWindow", "Welcome to savings tracker"))
        self.registerbutton.setText(_translate("MainWindow", "Register"))

    def press_it(self):
        con = sql.connect("data.db")
        cur = con.cursor()
        statement = "SELECT username, password FROM users"
        cur.execute(statement)
        userlist = cur.fetchall()
        state = False
        for i in userlist:
                if i[0]==self.username.text() and i[1]==self.password.text():
                    state = True
                    con.close()
        if state == True:
            with sql.connect('data.db') as db:
                cursor=db.cursor()
                cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.username.text()}(
                monthly integer NOT NULL,
                expenses integer NOT NULL,
                extraincome integer NOT NULL,
                extraexpenses integer NOT NULL,
                savings integer NOT NULL,
                comments text NOT NULL);""")
            db.commit()
            db.close()

            with sql.connect('data.db') as db1:
                cursor1=db1.cursor()
                cursor1.execute("DELETE FROM currentuser")
                cursor1.execute(f"""INSERT INTO currentuser(user_name)
                    VALUES("{self.username.text()}")""")
            db1.commit()
            db1.close()

            subprocess.Popen(['python', 'main.py'])
            sys.exit()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText(f"Please check if Username and Password are correct!")
            msgBox.setWindowTitle("Wrong Username or Password")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                pass
                
            elif returnValue == QMessageBox.Cancel:
                sys.exit()

    def register_it(self):
        subprocess.Popen(['python', 'register.py'])
        sys.exit()


import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
