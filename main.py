from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QStyledItemDelegate, QLineEdit
import sqlite3 as sql
import re
import matplotlib.pyplot as plt
import numpy as np

###################################################
#using external style sheet as inner breaks layout#
###################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 630)
        MainWindow.setMinimumSize(QtCore.QSize(800, 630))
        MainWindow.setMaximumSize(QtCore.QSize(800, 630))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 661))
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
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        ###################################
        self.givename = self.get_username()
        ###################################
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAutoFillBackground(True)
        self.tab.setObjectName("tab")
        self.savings_line = QtWidgets.QLineEdit(self.tab)
        self.savings_line.setStyleSheet(open('stylesheet.css').read())
        self.savings_line.setGeometry(QtCore.QRect(70, 120, 300, 35))
        self.savings_line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.savings_line.setObjectName("savings_line")
        self.income_line = QtWidgets.QLineEdit(self.tab)
        self.income_line.setGeometry(QtCore.QRect(70, 260, 300, 35))
        #########################################################
        self.income_line.setStyleSheet(open('stylesheet.css').read())
        #########################################################
        self.income_line.setObjectName("income_line")
        self.expenses_line = QtWidgets.QLineEdit(self.tab)
        self.expenses_line.setGeometry(QtCore.QRect(70, 330, 300, 35))
        ############################################################
        self.expenses_line.setStyleSheet(open('stylesheet.css').read())
        ############################################################
        self.expenses_line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.expenses_line.setObjectName("expenses_line")
        self.savings_label = QtWidgets.QLabel(self.tab)
        self.savings_label.setGeometry(QtCore.QRect(70, 100, 301, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.savings_label.setFont(font)
        self.savings_label.setObjectName("savings_label")
        self.pinbox_label = QtWidgets.QLabel(self.tab)
        self.pinbox_label.setGeometry(QtCore.QRect(70, 170, 291, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pinbox_label.setFont(font)
        self.pinbox_label.setObjectName("pinbox_label")
        self.income_label = QtWidgets.QLabel(self.tab)
        self.income_label.setGeometry(QtCore.QRect(70, 240, 291, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.income_label.setFont(font)
        self.income_label.setObjectName("income_label")
        self.expenses_label = QtWidgets.QLabel(self.tab)
        self.expenses_label.setGeometry(QtCore.QRect(70, 310, 331, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.expenses_label.setFont(font)
        self.expenses_label.setObjectName("expenses_label")
        ################################################################
        self.create_base_btn = QtWidgets.QPushButton(self.tab, clicked= lambda: self.press_create_base())
        ###############################################################
        self.create_base_btn.setGeometry(QtCore.QRect(110, 430, 221, 41))
        self.create_base_btn.setToolTip("")
        self.create_base_btn.setWhatsThis("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/inc/images/picture24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_base_btn.setIcon(icon)
        self.create_base_btn.setIconSize(QtCore.QSize(30, 30))
        #############################################################
        self.create_base_btn.setStyleSheet(open('stylesheet.css').read())
        #############################################################
        self.create_base_btn.setObjectName("create_base_btn")
        self.tab1_label = QtWidgets.QLabel(self.tab)
        self.tab1_label.setGeometry(QtCore.QRect(220, 30, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tab1_label.setFont(font)
        self.tab1_label.setObjectName("tab1_label")
        self.tab1_pic = QtWidgets.QLabel(self.tab)
        self.tab1_pic.setGeometry(QtCore.QRect(270, 0, 501, 581))
        self.tab1_pic.setText("")
        self.tab1_pic.setPixmap(QtGui.QPixmap(":/inc/output-onlinejpgtools (3).png"))
        self.tab1_pic.setObjectName("tab1_pic")
        self.months_box = QtWidgets.QSpinBox(self.tab)
        self.months_box.setGeometry(QtCore.QRect(70, 190, 300, 35))
        self.months_box.setStyleSheet(open('stylesheet.css').read())
        self.months_box.setMinimum(6)
        self.months_box.setMaximum(120)
        self.months_box.setSingleStep(6)
        self.months_box.setObjectName("months_box")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setAutoFillBackground(True)
        self.tab_2.setObjectName("tab_2")
        self.data_base_box = QtWidgets.QTableWidget(self.tab_2)
        self.data_base_box.setGeometry(QtCore.QRect(20, 70, 751, 441))
        font = QtGui.QFont()
        font.setBold(False)
        font.setPointSize(10)
        self.data_base_box.setFont(font)
        self.data_base_box.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.data_base_box.setAlternatingRowColors(True)
        self.data_base_box.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.data_base_box.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.data_base_box.setObjectName("data_base_box")
        self.data_base_box.setColumnCount(6)
        self.data_base_box.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_base_box.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_base_box.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_base_box.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_base_box.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_base_box.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_base_box.setHorizontalHeaderItem(5, item)
        ################################################################
        self.refresh_btn = QtWidgets.QPushButton(self.tab_2,clicked= lambda: self.refresh_data())
        ################################################################
        self.refresh_btn.setGeometry(QtCore.QRect(510, 10, 221, 41))
        #############################################################
        self.refresh_btn.setStyleSheet(open('stylesheet.css').read())
        #############################################################
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/inc/images/picture33.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon1)
        self.refresh_btn.setIconSize(QtCore.QSize(30, 30))
        self.refresh_btn.setObjectName("refresh_btn")
        ###################################################################
        self.update_data_btn = QtWidgets.QPushButton(self.tab_2, clicked= lambda: self.update_it())
        ###################################################################
        self.update_data_btn.setGeometry(QtCore.QRect(280, 530, 221, 41))
        #############################################################
        self.update_data_btn.setStyleSheet(open('stylesheet.css').read())
        #############################################################
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/inc/images/picture36.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_data_btn.setIcon(icon2)
        self.update_data_btn.setIconSize(QtCore.QSize(30, 30))
        self.update_data_btn.setObjectName("update_data_btn")
        self.tab2_label = QtWidgets.QLabel(self.tab_2)
        self.tab2_label.setGeometry(QtCore.QRect(50, 10, 451, 31))
        self.tab2_label.setObjectName("tab2_label")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        #################################################################
        self.plot_line_btn = QtWidgets.QPushButton(self.tab_3, clicked= lambda: self.show_me_line())
        #################################################################
        self.plot_line_btn.setGeometry(QtCore.QRect(50, 250, 221, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/inc/1909170-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plot_line_btn.setIcon(icon3)
        self.plot_line_btn.setIconSize(QtCore.QSize(30, 30))
        self.plot_line_btn.setObjectName("plot_line_btn")
        #############################################################
        self.plot_line_btn.setStyleSheet(open('stylesheet.css').read())
        ###################################################################
        self.plot_bar_btn = QtWidgets.QPushButton(self.tab_3, clicked= lambda: self.show_me_bar())
        ###################################################################
        self.plot_bar_btn.setGeometry(QtCore.QRect(520, 250, 221, 41))
        self.plot_bar_btn.setIcon(icon3)
        self.plot_bar_btn.setIconSize(QtCore.QSize(30, 30))
        self.plot_bar_btn.setObjectName("plot_bar_btn")
        #############################################################
        self.plot_bar_btn.setStyleSheet(open('stylesheet.css').read())
        #################################################################
        self.plot_pie_btn = QtWidgets.QPushButton(self.tab_3, clicked= lambda: self.show_me_pie())
        #################################################################
        self.plot_pie_btn.setGeometry(QtCore.QRect(280, 530, 221, 41))
        self.plot_pie_btn.setIcon(icon3)
        self.plot_pie_btn.setIconSize(QtCore.QSize(30, 30))
        self.plot_pie_btn.setObjectName("plot_pie_btn")
        #############################################################
        self.plot_pie_btn.setStyleSheet(open('stylesheet.css').read())
        #############################################################
        self.plot_line_label = QtWidgets.QLabel(self.tab_3)
        self.plot_line_label.setGeometry(QtCore.QRect(30, 10, 281, 71))
        self.plot_line_label.setWordWrap(True)
        self.plot_line_label.setObjectName("plot_line_label")
        self.line_pic = QtWidgets.QLabel(self.tab_3)
        self.line_pic.setGeometry(QtCore.QRect(50, 50, 261, 211))
        self.line_pic.setText("")
        self.line_pic.setPixmap(QtGui.QPixmap(":/inc/8e77dd6a09ce0f0a31bd7d077321dd7b-growing-colorful-lines-chart.png"))
        self.line_pic.setObjectName("line_pic")
        self.plot_bar_label = QtWidgets.QLabel(self.tab_3)
        self.plot_bar_label.setGeometry(QtCore.QRect(440, 10, 331, 71))
        self.plot_bar_label.setWordWrap(True)
        self.plot_bar_label.setObjectName("plot_bar_label")
        self.bar_pic = QtWidgets.QLabel(self.tab_3)
        self.bar_pic.setGeometry(QtCore.QRect(520, 70, 311, 171))
        self.bar_pic.setText("")
        self.bar_pic.setPixmap(QtGui.QPixmap(":/inc/bNDOM.png"))
        self.bar_pic.setObjectName("bar_pic")
        self.plot_pie_label = QtWidgets.QLabel(self.tab_3)
        self.plot_pie_label.setGeometry(QtCore.QRect(220, 300, 351, 61))
        self.plot_pie_label.setWordWrap(True)
        self.plot_pie_label.setObjectName("plot_pie_label")
        self.pie_pic = QtWidgets.QLabel(self.tab_3)
        self.pie_pic.setGeometry(QtCore.QRect(290, 340, 301, 201))
        self.pie_pic.setText("")
        self.pie_pic.setPixmap(QtGui.QPixmap(":/inc/output-onlinejpgtools (4).png"))
        self.pie_pic.setObjectName("pie_pic")
        self.pie_pic.raise_()
        self.plot_line_btn.raise_()
        self.plot_bar_btn.raise_()
        self.plot_pie_btn.raise_()
        self.plot_line_label.raise_()
        self.line_pic.raise_()
        self.plot_bar_label.raise_()
        self.bar_pic.raise_()
        self.plot_pie_label.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial tracker"))
        self.savings_label.setText(_translate("MainWindow", "How much savings you currently have?"))
        self.pinbox_label.setText(_translate("MainWindow", "For how many months you will be saving?"))
        self.income_label.setText(_translate("MainWindow", "Monthly income before taxes"))
        self.expenses_label.setText(_translate("MainWindow", "Ussual monthly expenses(taxes, rent, etc...)"))
        self.create_base_btn.setText(_translate("MainWindow", "Create database"))
        self.tab1_label.setText(_translate("MainWindow", f"Welcome {self.givename}. Please enter:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic setup"))
        item = self.data_base_box.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Montly income"))
        item = self.data_base_box.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Expenses"))
        item = self.data_base_box.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Extra income"))
        item = self.data_base_box.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Extra expenses"))
        item = self.data_base_box.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Savings"))
        item = self.data_base_box.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Comments"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.update_data_btn.setText(_translate("MainWindow", "Update data"))
        self.tab2_label.setText(_translate("MainWindow", "Here you can edit data!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Table"))
        self.plot_line_btn.setText(_translate("MainWindow", "Show me Line!"))
        self.plot_bar_btn.setText(_translate("MainWindow", "Show me Bar!"))
        self.plot_pie_btn.setText(_translate("MainWindow", "Show me Pie!"))
        self.plot_line_label.setText(_translate("MainWindow",
         "Line graphs are used to track changes over short and long periods of time. When smaller changes exist, line graphs are better to use than bar graphs."))
        self.plot_bar_label.setText(_translate("MainWindow",
         "Bar graphs are used to track changes over time. However, when trying to measure change over time, bar graphs are best when the changes are larger."))
        self.plot_pie_label.setText(_translate("MainWindow",
         "Pie charts show the parts-to-whole relationship.Pie charts can be helpful for showing the relationship of parts to the whole when there are a small number of levels. "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Charts"))

    def press_create_base(self):
        # check if int or float, no string allowed
        if re.match(r'^-?\d+(?:\.\d+)$', self.savings_line.text()) is not None or self.savings_line.text().isnumeric() and\
            re.match(r'^-?\d+(?:\.\d+)$', self.income_line.text()) is not None or self.savings_line.text().isnumeric() and\
                re.match(r'^-?\d+(?:\.\d+)$', self.expenses_line.text()) is not None or self.expenses_line.text().isnumeric():
            con = sql.connect("data.db")
            cur = con.cursor()
            con.execute(f"DELETE FROM {self.givename}")
            saving = float(self.savings_line.text())
            extraincome = 0
            extraexpenses = 0
            comments = '...'
            for i in range(0, int(self.months_box.text())):
                con.execute(f"""INSERT INTO {self.givename}(monthly, expenses, extraincome, extraexpenses, savings, comments)
                    VALUES(?,?,?,?,?,?)""",(self.income_line.text(), self.expenses_line.text(), extraincome, extraexpenses, saving, comments))
                # calculate saving by adding income-expenses and updating value
                saving += float(self.income_line.text()) - float(self.expenses_line.text())    
            con.commit()
            con.close()
            msgBox0 = QMessageBox()
            msgBox0.setIcon(QMessageBox.Information)
            msgBox0.setText(f"Database created")
            msgBox0.setWindowTitle("Success!")
            msgBox0.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox0.exec()
        else:
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Critical)
            msgBox1.setText(f"Only integers allowed!")
            msgBox1.setWindowTitle("Wrong input!")
            msgBox1.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox1.exec()

    def refresh_data(self):
        con = sql.connect("data.db")
        cur = con.cursor()
        sqlquery = f"SELECT * FROM {self.givename}"
        self.data_base_box.setRowCount(int(len(list(cur.execute(f"""SELECT monthly FROM {self.givename}""")))))
        tablerow = 0
        for col in cur.execute(sqlquery):
            # pull data from database and submit into table where user can see it
            self.data_base_box.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(col[0])))
            self.data_base_box.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(col[1])))
            self.data_base_box.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(col[2])))
            self.data_base_box.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(col[3])))
            self.data_base_box.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(col[4])))
            self.data_base_box.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(col[5])))
            tablerow+=1

    def update_it(self):
        # countrows checking how big table should be created
        countrows = self.data_base_box.rowCount()
        # state checks if submitted data correct
        state = True
        for i in range(0,countrows):
            col0 = self.data_base_box.item(i,0)
            col1 = self.data_base_box.item(i,1)
            col2 = self.data_base_box.item(i,2)
            col3 = self.data_base_box.item(i,3)
            col4 = self.data_base_box.item(i,4)
            # check if int or float, no string allowed
            if re.match(r'^-?\d+(?:\.\d+)$', col0.text()) is None and col0.text().isnumeric()==False or\
             re.match(r'^-?\d+(?:\.\d+)$', col1.text()) is None and col1.text().isnumeric()==False or\
              re.match(r'^-?\d+(?:\.\d+)$', col2.text()) is None and col2.text().isnumeric()==False or\
               re.match(r'^-?\d+(?:\.\d+)$', col3.text()) is None and col3.text().isnumeric()==False:
                msgBox1 = QMessageBox()
                msgBox1.setIcon(QMessageBox.Critical)
                msgBox1.setText(f"Only comments can be string, other cells need to be integer!")
                msgBox1.setWindowTitle("Wrong input!")
                msgBox1.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox1.exec()
                state = False

        if state == True:
            con = sql.connect("data.db")
            cur = con.cursor()
            con.execute(f"DELETE FROM {self.givename}")
            saving = self.data_base_box.item(0,4).text()
            saving = float(saving)
            # append data to table
            for i in range(0,countrows):
                col0 = self.data_base_box.item(i,0)
                col1 = self.data_base_box.item(i,1)
                col2 = self.data_base_box.item(i,2)
                col3 = self.data_base_box.item(i,3)
                col5 = self.data_base_box.item(i,5)
                con.execute(f"""INSERT INTO {self.givename}(monthly, expenses, extraincome, extraexpenses, savings, comments)
                    VALUES(?,?,?,?,?,?)""",(float(col0.text()), float(col1.text()), float(col2.text()), float(col3.text()), float(saving),col5.text()))
                saving += float(col0.text()) - float(col1.text()) + float(col2.text()) - float(col3.text())
            con.commit()
            con.close()

    def show_me_line(self):
        #############################################
        #only works as external script
        #############################################
        exec(open("line_graph.py").read(), globals())
        #############################################

    def show_me_bar(self):
        con = sql.connect("data.db")
        cur = con.cursor()
        sqlquery = f"SELECT * FROM {self.givename}"
        income = []
        expenses = []
        savings = []
        months = [i for i in range(int(len(list(cur.execute(f"SELECT monthly FROM {self.givename}")))))]
        for i in cur.execute(f"SELECT * FROM {self.givename}"):
              income.append(i[0]+i[2])
              expenses.append(i[1]+i[3])
              savings.append(i[4])
        con.commit()
        con.close()

        barWidth = 0.28
        fig = plt.subplots(figsize =(8, 6))
         
        br1 = np.arange(len(months))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
         
        plt.bar(br1, income, color ='green', width = barWidth,
                edgecolor ='blue', label ='Income')
        plt.bar(br2, expenses, color ='red', width = barWidth,
                edgecolor ='black', label ='Expenses')
        plt.bar(br3, savings, color ='blue', width = barWidth,
                edgecolor ='green', label ='Savings')
        plt.title('Income/expenses over time', fontweight ='bold', fontsize = 15)
        plt.xlabel('Months', fontweight ='bold', fontsize = 15)
        plt.ylabel('Amount of money', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(0, len(months))],
                months)
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.3)
        plt.legend()
        plt.show()

    def show_me_pie(self):
        con = sql.connect("data.db")
        cur = con.cursor()
        sqlquery = f"SELECT * FROM {self.givename}"
        income = []
        expenses = []
        savings = []
        starting_savings = list(cur.execute(f"SELECT savings FROM {self.givename}"))[0]
        months = [i for i in range(int(len(list(cur.execute(f"SELECT monthly FROM {self.givename}")))))]
        for i in cur.execute(f"SELECT * FROM {self.givename}"):
              income.append(i[0]+i[2])
              expenses.append(i[1]+i[3])
              savings.append(i[4])
        con.commit()
        con.close()
        if savings[-1] - starting_savings[0] < 0:
            saved_extra = 0
        else:
            saved_extra = savings[-1] - starting_savings[0]
        x = [sum(income),sum(expenses), saved_extra, starting_savings[0]]
        labels = ['Sum of all income', 'Sum of all expenses', 'Saved over time', 'Starting savings']
        colors = ['tab:green', 'tab:red', 'tab:cyan', 'tab:blue']
        explode = [0, 0.05, 0.15, 0.3]

        fig, ax = plt.subplots(figsize =(8, 6))

        ax.pie(x, labels = labels,
                  colors = colors,
                  autopct='%.0f%%',
                  explode = explode,
                  shadow = True,
                  startangle = 180)

        ax.set_title('Income/expenses over time', fontweight ='bold', fontsize = 15)
        plt.show()

    def get_username(self):
        # get current user name from database
        con = sql.connect("data.db")
        cur = con.cursor()
        statement = "SELECT * FROM currentuser"
        cur.execute(statement)
        userlist = cur.fetchall()
        return userlist[0][0]

            
import paveiksliukai_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
