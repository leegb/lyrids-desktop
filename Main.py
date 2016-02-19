# -*- coding: gb2312 -*-
#!/usr/bin/env python

#coding=utf-8
'''
Created on 2016年1月3日

@author: Administrator
'''
#---------------------------
#文件结构：
# 1.import packages
# 2.变量定义
# 3.类定义
# 4.函数定义
# 5.主程序代码
#---------------------------

import sys
from WindPy import *
from decimal import *
import math
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#==================变量定义===================
#保存点击后传入的参数，比如国企改革、一带一路    
groupName=''
#行情订阅ID
requestID=0    
# Wind获取实时行情
Codes=[]    #返回股票代码
Data = {}   #行情数据
#显示主界面
main=QApplication(sys.argv)
stackedWid=QStackedWidget()
stackedWid.setWindowTitle('Lyrids')
#定义Widget
qWid1=QWidget()
qWid2=QWidget()
qWid3=QWidget()
#御前启动Wind
w.start()
#==================类定义===================

#----------------------登陆类----------------------
class Login(object):
    def setupUi(self, Dialog): 
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 338)
        Dialog.setFixedSize(640,338)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(300, 270, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(470, 270, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(340, 270, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setEchoMode(QLineEdit.Password) #设置QLineEdit输入模式为密码，不直接显示输入内容
        self.lineEdit_2.setGeometry(QRect(500, 270, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(0, 0, 641, 251))
        self.label_3.setText("")
        self.label_3.setPixmap(QPixmap("Guangzhou Tower.png"))
        self.label_3.setObjectName("label_3")
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setGeometry(QRect(410, 290, 71, 41))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(510, 300, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(20, 262, 54, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)
        
        self.passAuthentication=0   #默认用户没有权限通过登陆界面
        Dialog.connect(self.pushButton,SIGNAL("clicked()"),self.userAuthentication)   #验证账号密码，通过则返回1，不通过则返回0
        Dialog.connect(self.lineEdit_2,SIGNAL('returnPressed()'),self.userAuthentication)   #验证账号密码，通过则返回1，不通过则返回0
        Dialog.setWindowTitle("Beta1.0")
        Dialog.setStyleSheet("background:white")
        Dialog.setFixedSize(640,338)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Dialog")
        self.label.setText("账号")
        self.label_2.setText("密码")
        self.checkBox.setText("保存账号")
        self.pushButton.setText("登陆")
        self.label_4.setText("设置")
    
    def userAuthentication(self):
        user=self.lineEdit.text()
        key=self.lineEdit_2.text()
        if user=='admin' and key=='111111':
            self.passAuthentication=1
            print('Login successfully!')
            
            #----------------------------------
            #若Wind启动失败，需要添加Wind客户端关闭重启功能
            #----------------------------------
            if w.isconnected()==True:
                stackedWid.resize(1297,704)
                stackedWid.setFixedSize(1297,704)
                stackedWid.move(10,5)
                stackedWid.setCurrentIndex(1) #Pivot为序号1的界面
            else:
                message=QMessageBox()
                message.setText('警告：WindPy启动超时，请重新启动程序！')
                message.setInformativeText('Wind服务器繁忙，暂时无法连接。请关闭程序后再重新启动！')
                message.setStandardButtons(QMessageBox.Yes)
                message.setDefaultButton(QMessageBox.Yes)
                reply=message.exec()
                if reply==QMessageBox.Yes:
                    w.stop()
                    stackedWid.close()
        else:
            message=QMessageBox()
            message.setText('账号或密码错误！')
            message.setInformativeText('请重新输入用户及密码...')
            message.setWindowTitle('警告')
            message.resize(250,200)
            message.setStandardButtons(QMessageBox.Yes)
            message.setDefaultButton(QMessageBox.Yes)
            reply=message.exec()
            if reply==QMessageBox.Yes:
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                message.hide()
            print('Login failed!')

#------------------------------------------------

class Pivot(object):
    def setupUi(self, Widget1):
        Widget1.setObjectName("Widget1")
        Widget1.resize(669, 496)
        Widget1.setStyleSheet("background-color:\"black\";font-size:18pt;")
        self.groupName = QLabel(Widget1)
        self.groupName.setGeometry(QRect(70, 51, 121, 31))
        self.groupName.setStyleSheet("color:\"white\";font-weight:bold;font-size:20pt;")
        self.groupName.setObjectName("groupName")
        self.line = QFrame(Widget1)
        self.line.setGeometry(QRect(10, 90, 1300, 3))
        self.line.setStyleSheet("color:\"grey\";background-color:\"red\";")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.GQGG_Button = QPushButton(Widget1)
        self.GQGG_Button.setGeometry(QRect(80, 120, 181, 33))
        self.GQGG_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;")
        self.GQGG_Button.setObjectName("pushButton")
        self.YDYL_Button = QPushButton(Widget1)
        self.YDYL_Button.setGeometry(QRect(80, 170, 181, 33))
        self.YDYL_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;")
        self.YDYL_Button.setObjectName("pushButton_2")
        self.ZQFJ_Button = QPushButton(Widget1)
        self.ZQFJ_Button.setGeometry(QRect(80, 220, 181, 33))
        self.ZQFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;")
        self.ZQFJ_Button.setObjectName("pushButton_3")
        self.SZ50_Button = QPushButton(Widget1)
        self.SZ50_Button.setGeometry(QRect(70, 270, 221, 33))
        self.SZ50_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;")
        self.SZ50_Button.setObjectName("pushButton_4")
        self.JGFJ_Button = QPushButton(Widget1)
        self.JGFJ_Button.setGeometry(QRect(80, 320, 181, 33))
        self.JGFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;")
        self.JGFJ_Button.setObjectName("pushButton_5")

        self.retranslateUi(Widget1)
        QMetaObject.connectSlotsByName(Widget1)
        
        #同一板块单击次数两次则进入详细页，单击次数一次则显示下划线 
        self.groupNameClicked=''    #记录点击的板块代码
        self.times=0    #记录单击次数
           
        QObject.connect(self.GQGG_Button,SIGNAL('clicked()'),self.toSubPivot_GQGG)
        QObject.connect(self.YDYL_Button,SIGNAL('clicked()'),self.toSubPivot_YDYL)
        QObject.connect(self.ZQFJ_Button,SIGNAL('clicked()'),self.toSubPivot_ZQFJ)
        QObject.connect(self.SZ50_Button,SIGNAL('clicked()'),self.toSubPivot_SZ50)
        QObject.connect(self.JGFJ_Button,SIGNAL('clicked()'),self.toSubPivot_JGFJ)
     
    def toSubPivot_GQGG(self):
        global groupName,Codes
        if self.groupNameClicked=='GQGG':   #判断上一次点击和本次点击是否同一板块
            self.times=self.times+1
        else:
            if self.groupNameClicked=='YDYL':   #上一次选中的板块颜色恢复为灰色
                self.YDYL_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='ZQFJ':
                self.ZQFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='SZ50':
                self.SZ50_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='JGFJ':
                self.JGFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            self.times=0
        if self.times==0:
            self.GQGG_Button.setStyleSheet("color:\"white\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")  #单击增加下划线
            self.times=self.times+1
            self.groupNameClicked='GQGG'
        else:   #认为用户双击
            groupName='GQGG' #GQGG--国企改革
            self.GQGG_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            Codes=['502006.SH','502007.SH','502008.SH']
            w.wsq("502006.SH,502007.SH,502008.SH", "rt_last,rt_pct_chg,rt_bid1,rt_bsize1,rt_bid2,rt_bsize2,rt_bid3,rt_bsize3,rt_ask1,rt_asize1,rt_ask2,rt_asize2,rt_ask3,rt_asize3", func=getData)
            stackedWid.setCurrentIndex(2)
            self.groupNameClicked=''    #初始化选中的板块
            self.times=0    #初始化times
                                        
    def toSubPivot_YDYL(self):
        global groupName,Codes
        if self.groupNameClicked=='YDYL':   #判断上一次点击和本次点击是否同一板块
            self.times=self.times+1
        else:
            if self.groupNameClicked=='GQGG':
                self.GQGG_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='ZQFJ':
                self.ZQFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='SZ50':
                self.SZ50_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='JGFJ':
                self.JGFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            self.times=0
        if self.times==0:
            self.YDYL_Button.setStyleSheet("color:\"white\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")  #单击增加下划线
            self.times=self.times+1
            self.groupNameClicked='YDYL'
        else:
            groupName='YDYL' #YDYL--一带一路
            self.YDYL_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            Codes=['502013.SH','502014.SH','502015.SH']
            w.wsq("502013.SH,502014.SH,502015.SH", "rt_last,rt_pct_chg,rt_bid1,rt_bsize1,rt_bid2,rt_bsize2,rt_bid3,rt_bsize3,rt_ask1,rt_asize1,rt_ask2,rt_asize2,rt_ask3,rt_asize3", func=getData)
            stackedWid.setCurrentIndex(2) 
            self.groupNameClicked=''    #初始化选中的板块
            self.times=0    #初始化times
            
    def toSubPivot_ZQFJ(self):
        global groupName,Codes
        if self.groupNameClicked=='ZQFJ':   #判断上一次点击和本次点击是否同一板块
            self.times=self.times+1
        else:
            if self.groupNameClicked=='GQGG':
                self.GQGG_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='YDYL':
                self.YDYL_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='SZ50':
                self.SZ50_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='JGFJ':
                self.JGFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            self.times=0
        if self.times==0:
            self.ZQFJ_Button.setStyleSheet("color:\"white\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")  #单击增加下划线
            self.times=self.times+1
            self.groupNameClicked='ZQFJ'
        else:
            groupName='ZQFJ' #ZQFJ--证券分级
            self.ZQFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            Codes=['502010.SH','502011.SH','502012.SH']
            w.wsq("502010.SH,502011.SH,502012.SH", "rt_last,rt_pct_chg,rt_bid1,rt_bsize1,rt_bid2,rt_bsize2,rt_bid3,rt_bsize3,rt_ask1,rt_asize1,rt_ask2,rt_asize2,rt_ask3,rt_asize3", func=getData)
            stackedWid.setCurrentIndex(2)
            self.groupNameClicked=''    #初始化选中的板块
            self.times=0    #初始化times
                 
    def toSubPivot_SZ50(self):
        global groupName,Codes
        if self.groupNameClicked=='SZ50':   #判断上一次点击和本次点击是否同一板块
            self.times=self.times+1
        else:
            if self.groupNameClicked=='GQGG':
                self.GQGG_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='YDYL':
                self.YDYL_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='ZQFJ':
                self.ZQFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='JGFJ':
                self.JGFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            self.times=0
        if self.times==0:
            self.SZ50_Button.setStyleSheet("color:\"white\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")  #单击增加下划线
            self.times=self.times+1
            self.groupNameClicked='SZ50'
        else:
            groupName='SZ50' #SZ50--50上证
            self.SZ50_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            Codes=['502048.SH','502049.SH','502050.SH']
            w.wsq("502048.SH,502049.SH,502050.SH", "rt_last,rt_pct_chg,rt_bid1,rt_bsize1,rt_bid2,rt_bsize2,rt_bid3,rt_bsize3,rt_ask1,rt_asize1,rt_ask2,rt_asize2,rt_ask3,rt_asize3", func=getData)
            stackedWid.setCurrentIndex(2)
            self.groupNameClicked=''    #初始化选中的板块
            self.times=0    #初始化times      
   
    def toSubPivot_JGFJ(self):
        global groupName,Codes
        if self.groupNameClicked=='JGFJ':   #判断上一次点击和本次点击是否同一板块
            self.times=self.times+1
        else:
            if self.groupNameClicked=='GQGG':
                self.GQGG_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='YDYL':
                self.YDYL_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='ZQFJ':
                self.ZQFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            elif self.groupNameClicked=='SZ50':
                self.SZ50_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            self.times=0
        if self.times==0:
            self.JGFJ_Button.setStyleSheet("color:\"white\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")  #单击增加下划线
            self.times=self.times+1
            self.groupNameClicked='JGFJ'
        else:
            groupName='JGFJ' #JGFJ--军工分级
            self.JGFJ_Button.setStyleSheet("color:\"grey\";font-weight:bold;font-size:15pt;border-bottom:1px solid \"white\";")
            Codes=['502003.SH','502004.SH','502005.SH']
            w.wsq("502003.SH,502004.SH,502005.SH", "rt_last,rt_pct_chg,rt_bid1,rt_bsize1,rt_bid2,rt_bsize2,rt_bid3,rt_bsize3,rt_ask1,rt_asize1,rt_ask2,rt_asize2,rt_ask3,rt_asize3", func=getData)
            stackedWid.setCurrentIndex(2)
            self.groupNameClicked=''    #初始化选中的板块
            self.times=0    #初始化times  

    def retranslateUi(self, Widget1):
        Widget1.setWindowTitle("Widget1")
        self.groupName.setText("板块名称")
        self.GQGG_Button.setText( "国企改革主题")
        self.YDYL_Button.setText( "一带一路主题")
        self.ZQFJ_Button.setText( "证券分级主题")
        self.SZ50_Button.setText("上证50分级主题")
        self.JGFJ_Button.setText("军工分级主题")

#--------------------------------------------------------   
      
#----------------------子中枢类----------------------
class SubPivot(object):
    global requestID
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setAccessibleDescription("")
        MainWindow.setStyleSheet("background:rgb(0, 38, 116);\n"
"font-weight:800;\n"
"font-size:14pt;\n"
"color:\"white\"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.theme = QLabel(self.centralwidget)
        self.theme.setGeometry(QRect(80, 10, 801, 41))
        self.theme.setStyleSheet("font-weight:900;\n"
"font-size:30px;\n"
"color:rgb(220, 147, 0);\n"
"border-bottom:1px solid \"white\";\n"
"padding-top:0px;\n"
"")
        self.theme.setObjectName("theme")
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(80, 60, 961, 291))
        self.widget.setStyleSheet("padding-top:0px;")
        self.widget.setObjectName("widget")
        self.widget1 = QWidget(self.widget)
        self.widget1.setGeometry(QRect(0, 0, 921, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tradeDirect1 = QLabel(self.widget1)
        self.tradeDirect1.setStyleSheet("color:\"white\";")
        self.tradeDirect1.setObjectName("tradeDirect1")
        self.horizontalLayout_2.addWidget(self.tradeDirect1)
        self.depart = QLabel(self.widget1)
        self.depart.setStyleSheet("color:\"white\";font-weight:600;\n"
"")
        self.depart.setObjectName("depart")
        self.horizontalLayout_2.addWidget(self.depart)
        self.isQualify2Trade1 = QLabel(self.widget1)
        self.isQualify2Trade1.setStyleSheet("color:\"white\";\n"
"")
        self.isQualify2Trade1.setObjectName("isQualify2Trade1")
        self.horizontalLayout_2.addWidget(self.isQualify2Trade1)
        self.isQualify1 = QLabel(self.widget1)
        self.isQualify1.setStyleSheet("color:\"red\";font-weight:600;")
        self.isQualify1.setObjectName("isQualify1")
        self.horizontalLayout_2.addWidget(self.isQualify1)
        self.expIncomeRate1 = QLabel(self.widget1)
        self.expIncomeRate1.setStyleSheet("color:\"white\";")
        self.expIncomeRate1.setObjectName("expIncomeRate1")
        self.horizontalLayout_2.addWidget(self.expIncomeRate1)
        self.incomeRateValue1 = QLabel(self.widget1)
        self.incomeRateValue1.setStyleSheet("color:\"red\";font-weight:600")
        self.incomeRateValue1.setObjectName("incomeRateValue1")
        self.horizontalLayout_2.addWidget(self.incomeRateValue1)
        self.placeOrder1 = QPushButton(self.widget1)
        self.placeOrder1.setStyleSheet("background-color:\"red\";\n"
"color:\"white\";")
        self.placeOrder1.setObjectName("placeOrder1")
        self.horizontalLayout_2.addWidget(self.placeOrder1)
        self.widget2 = QWidget(self.widget)
        self.widget2.setGeometry(QRect(0, 40, 791, 235))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QHBoxLayout(self.widget2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.depCodeValue1 = QLabel(self.widget2)
        self.depCodeValue1.setStyleSheet("font-weight:bold;color:rgb(220, 147, 0);")
        self.depCodeValue1.setObjectName("depCodeValue1")
        self.gridLayout_14.addWidget(self.depCodeValue1, 1, 1, 1, 1)
        self.depName1 = QLabel(self.widget2)
        self.depName1.setStyleSheet("border-bottom:1px solid \"white\";\n"
"color:\"white\";\n"
"")
        self.depName1.setObjectName("depName1")
        self.gridLayout_14.addWidget(self.depName1, 0, 0, 1, 1)
        self.depCode1 = QLabel(self.widget2)
        self.depCode1.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.depCode1.setObjectName("depCode1")
        self.gridLayout_14.addWidget(self.depCode1, 0, 1, 1, 1)
        self.depNameValue1 = QLabel(self.widget2)
        self.depNameValue1.setStyleSheet("\n"
"font-weight:bold;color:rgb(220, 147, 0);")
        self.depNameValue1.setObjectName("depNameValue1")
        self.gridLayout_14.addWidget(self.depNameValue1, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_14)
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.depRiseValue1 = QLabel(self.widget2)
        self.depRiseValue1.setStyleSheet("color:\"green\";")
        self.depRiseValue1.setObjectName("depRiseValue1")
        self.gridLayout_13.addWidget(self.depRiseValue1, 1, 1, 1, 1)
        self.depRise1 = QLabel(self.widget2)
        self.depRise1.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.depRise1.setObjectName("depRise1")
        self.gridLayout_13.addWidget(self.depRise1, 0, 1, 1, 1)
        self.depNetWorthValue1 = QLabel(self.widget2)
        self.depNetWorthValue1.setStyleSheet("color:\"white\";")
        self.depNetWorthValue1.setObjectName("depNetWorthValue1")
        self.gridLayout_13.addWidget(self.depNetWorthValue1, 1, 0, 1, 1)
        self.depNetWorth1 = QLabel(self.widget2)
        self.depNetWorth1.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.depNetWorth1.setObjectName("depNetWorth1")
        self.gridLayout_13.addWidget(self.depNetWorth1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_13)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.depAsk1_1 = QLabel(self.widget2)
        self.depAsk1_1.setStyleSheet("color:\"white\";")
        self.depAsk1_1.setObjectName("depAsk1_1")
        self.gridLayout_2.addWidget(self.depAsk1_1, 0, 0, 1, 1)
        self.depAskValue1_1 = QLabel(self.widget2)
        self.depAskValue1_1.setStyleSheet("background-color:\"orange\";color:\"green\";")
        self.depAskValue1_1.setObjectName("depAskValue1_1")
        self.gridLayout_2.addWidget(self.depAskValue1_1, 0, 1, 1, 1)
        self.depAskAmount1_1 = QLabel(self.widget2)
        self.depAskAmount1_1.setStyleSheet("background-color:\"orange\";")
        self.depAskAmount1_1.setObjectName("depAskAmount1_1")
        self.gridLayout_2.addWidget(self.depAskAmount1_1, 0, 2, 1, 1)
        self.depAsk1_2 = QLabel(self.widget2)
        self.depAsk1_2.setStyleSheet("color:\"white\";")
        self.depAsk1_2.setObjectName("depAsk1_2")
        self.gridLayout_2.addWidget(self.depAsk1_2, 1, 0, 1, 1)
        self.depAskValue1_2 = QLabel(self.widget2)
        self.depAskValue1_2.setStyleSheet("color:\"white\";")
        self.depAskValue1_2.setScaledContents(False)
        self.depAskValue1_2.setObjectName("depAskValue1_2")
        self.gridLayout_2.addWidget(self.depAskValue1_2, 1, 1, 1, 1)
        self.depAskAmount1_2 = QLabel(self.widget2)
        self.depAskAmount1_2.setStyleSheet("color:\"yellow\";")
        self.depAskAmount1_2.setObjectName("depAskAmount1_2")
        self.gridLayout_2.addWidget(self.depAskAmount1_2, 1, 2, 1, 1)
        self.depAsk1_3 = QLabel(self.widget2)
        self.depAsk1_3.setStyleSheet("color:\"white\";")
        self.depAsk1_3.setObjectName("depAsk1_3")
        self.gridLayout_2.addWidget(self.depAsk1_3, 2, 0, 1, 1)
        self.depAskValue1_3 = QLabel(self.widget2)
        self.depAskValue1_3.setStyleSheet("color:\"green\";")
        self.depAskValue1_3.setObjectName("depAskValue1_3")
        self.gridLayout_2.addWidget(self.depAskValue1_3, 2, 1, 1, 1)
        self.depAskAmount1_3 = QLabel(self.widget2)
        self.depAskAmount1_3.setStyleSheet("color:\"yellow\";")
        self.depAskAmount1_3.setObjectName("depAskAmount1_3")
        self.gridLayout_2.addWidget(self.depAskAmount1_3, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.depNameValue2 = QLabel(self.widget2)
        self.depNameValue2.setStyleSheet("font-weight:bold;color:rgb(220, 147, 0);")
        self.depNameValue2.setObjectName("depNameValue2")
        self.gridLayout_15.addWidget(self.depNameValue2, 1, 0, 1, 1)
        self.depCodeValue2 = QLabel(self.widget2)
        self.depCodeValue2.setStyleSheet("font-weight:bold;\n"
"color:rgb(220, 147, 0);")
        self.depCodeValue2.setObjectName("depCodeValue2")
        self.gridLayout_15.addWidget(self.depCodeValue2, 1, 1, 1, 1)
        self.depName2 = QLabel(self.widget2)
        self.depName2.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.depName2.setObjectName("depName2")
        self.gridLayout_15.addWidget(self.depName2, 0, 0, 1, 1)
        self.depCode2 = QLabel(self.widget2)
        self.depCode2.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.depCode2.setObjectName("depCode2")
        self.gridLayout_15.addWidget(self.depCode2, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_15)
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.depRiseValue2 = QLabel(self.widget2)
        self.depRiseValue2.setStyleSheet("color:\"red\";")
        self.depRiseValue2.setObjectName("depRiseValue2")
        self.gridLayout_16.addWidget(self.depRiseValue2, 1, 1, 1, 1)
        self.depNetWorthValue2 = QLabel(self.widget2)
        self.depNetWorthValue2.setStyleSheet("color:\"white\";")
        self.depNetWorthValue2.setObjectName("depNetWorthValue2")
        self.gridLayout_16.addWidget(self.depNetWorthValue2, 1, 0, 1, 1)
        self.depRise2 = QLabel(self.widget2)
        self.depRise2.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.depRise2.setObjectName("depRise2")
        self.gridLayout_16.addWidget(self.depRise2, 0, 1, 1, 1)
        self.depNetWorth2 = QLabel(self.widget2)
        self.depNetWorth2.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.depNetWorth2.setObjectName("depNetWorth2")
        self.gridLayout_16.addWidget(self.depNetWorth2, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_16)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.depBidValue2_1 = QLabel(self.widget2)
        self.depBidValue2_1.setStyleSheet("background-color:\"orange\";")
        self.depBidValue2_1.setObjectName("depBidValue2_1")
        self.gridLayout_7.addWidget(self.depBidValue2_1, 0, 1, 1, 1)
        self.depBidAmount2_1 = QLabel(self.widget2)
        self.depBidAmount2_1.setStyleSheet("background-color:\"orange\";")
        self.depBidAmount2_1.setObjectName("depBidAmount2_1")
        self.gridLayout_7.addWidget(self.depBidAmount2_1, 0, 2, 1, 2)
        self.depBidValue2_2 = QLabel(self.widget2)
        self.depBidValue2_2.setStyleSheet("color:\"red\";")
        self.depBidValue2_2.setObjectName("depBidValue2_2")
        self.gridLayout_7.addWidget(self.depBidValue2_2, 1, 1, 1, 1)
        self.depBidAmount2_3 = QLabel(self.widget2)
        self.depBidAmount2_3.setStyleSheet("color:\"yellow\";")
        self.depBidAmount2_3.setObjectName("depBidAmount2_3")
        self.gridLayout_7.addWidget(self.depBidAmount2_3, 2, 2, 1, 2)
        self.depBidValue2_3 = QLabel(self.widget2)
        self.depBidValue2_3.setStyleSheet("color:\"red\";")
        self.depBidValue2_3.setObjectName("depBidValue2_3")
        self.gridLayout_7.addWidget(self.depBidValue2_3, 2, 1, 1, 1)
        self.depBid2_3 = QLabel(self.widget2)
        self.depBid2_3.setStyleSheet("color:\"white\";")
        self.depBid2_3.setObjectName("depBid2_3")
        self.gridLayout_7.addWidget(self.depBid2_3, 2, 0, 1, 1)
        self.depBidAmount2_2 = QLabel(self.widget2)
        self.depBidAmount2_2.setStyleSheet("color:\"yellow\";")
        self.depBidAmount2_2.setObjectName("depBidAmount2_2")
        self.gridLayout_7.addWidget(self.depBidAmount2_2, 1, 2, 1, 2)
        self.depBid2_1 = QLabel(self.widget2)
        self.depBid2_1.setStyleSheet("color:\"white\";")
        self.depBid2_1.setObjectName("depBid2_1")
        self.gridLayout_7.addWidget(self.depBid2_1, 0, 0, 1, 1)
        self.depBid2_2 = QLabel(self.widget2)
        self.depBid2_2.setStyleSheet("color:\"white\";")
        self.depBid2_2.setObjectName("depBid2_2")
        self.gridLayout_7.addWidget(self.depBid2_2, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.depName3 = QLabel(self.widget2)
        self.depName3.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.depName3.setObjectName("depName3")
        self.gridLayout.addWidget(self.depName3, 0, 0, 1, 1)
        self.depCode3 = QLabel(self.widget2)
        self.depCode3.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.depCode3.setObjectName("depCode3")
        self.gridLayout.addWidget(self.depCode3, 0, 1, 1, 1)
        self.depNameValue3 = QLabel(self.widget2)
        self.depNameValue3.setStyleSheet("font-weight:bold;color:rgb(220, 147, 0);")
        self.depNameValue3.setObjectName("depNameValue3")
        self.gridLayout.addWidget(self.depNameValue3, 1, 0, 1, 1)
        self.depCodeValue3 = QLabel(self.widget2)
        self.depCodeValue3.setStyleSheet("\n"
"font-weight:bold;\n"
"color:rgb(220, 147, 0);")
        self.depCodeValue3.setObjectName("depCodeValue3")
        self.gridLayout.addWidget(self.depCodeValue3, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.depNetWorth3 = QLabel(self.widget2)
        self.depNetWorth3.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.depNetWorth3.setObjectName("depNetWorth3")
        self.gridLayout_11.addWidget(self.depNetWorth3, 0, 0, 1, 1)
        self.depRise3 = QLabel(self.widget2)
        self.depRise3.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.depRise3.setObjectName("depRise3")
        self.gridLayout_11.addWidget(self.depRise3, 0, 1, 1, 1)
        self.depNetWorthValue3 = QLabel(self.widget2)
        self.depNetWorthValue3.setStyleSheet("color:\"white\";")
        self.depNetWorthValue3.setObjectName("depNetWorthValue3")
        self.gridLayout_11.addWidget(self.depNetWorthValue3, 1, 0, 1, 1)
        self.depRiseValue3 = QLabel(self.widget2)
        self.depRiseValue3.setStyleSheet("color:\"green\";")
        self.depRiseValue3.setObjectName("depRiseValue3")
        self.gridLayout_11.addWidget(self.depRiseValue3, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_11)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.depBid3_1 = QLabel(self.widget2)
        self.depBid3_1.setStyleSheet("color:\"white\";")
        self.depBid3_1.setObjectName("depBid3_1")
        self.gridLayout_12.addWidget(self.depBid3_1, 0, 0, 1, 1)
        self.depBidValue3_1 = QLabel(self.widget2)
        self.depBidValue3_1.setStyleSheet("background-color:\"orange\";")
        self.depBidValue3_1.setObjectName("depBidValue3_1")
        self.gridLayout_12.addWidget(self.depBidValue3_1, 0, 1, 1, 1)
        self.depBidAmount3_1 = QLabel(self.widget2)
        self.depBidAmount3_1.setStyleSheet("background-color:\"orange\";")
        self.depBidAmount3_1.setObjectName("depBidAmount3_1")
        self.gridLayout_12.addWidget(self.depBidAmount3_1, 0, 2, 1, 1)
        self.depBid3_2 = QLabel(self.widget2)
        self.depBid3_2.setStyleSheet("color:\"white\";")
        self.depBid3_2.setObjectName("depBid3_2")
        self.gridLayout_12.addWidget(self.depBid3_2, 1, 0, 1, 1)
        self.depBidValue3_2 = QLabel(self.widget2)
        self.depBidValue3_2.setStyleSheet("color:\"green\";")
        self.depBidValue3_2.setObjectName("depBidValue3_2")
        self.gridLayout_12.addWidget(self.depBidValue3_2, 1, 1, 1, 1)
        self.depBidAmount3_2 = QLabel(self.widget2)
        self.depBidAmount3_2.setStyleSheet("color:\"yellow\";")
        self.depBidAmount3_2.setObjectName("depBidAmount3_2")
        self.gridLayout_12.addWidget(self.depBidAmount3_2, 1, 2, 1, 1)
        self.depBid3_3 = QLabel(self.widget2)
        self.depBid3_3.setStyleSheet("color:\"white\";")
        self.depBid3_3.setObjectName("depBid3_3")
        self.gridLayout_12.addWidget(self.depBid3_3, 2, 0, 1, 1)
        self.depBidValue3_3 = QLabel(self.widget2)
        self.depBidValue3_3.setStyleSheet("color:\"green\";")
        self.depBidValue3_3.setObjectName("depBidValue3_3")
        self.gridLayout_12.addWidget(self.depBidValue3_3, 2, 1, 1, 1)
        self.depBidAmount3_3 = QLabel(self.widget2)
        self.depBidAmount3_3.setStyleSheet("color:\"yellow\";")
        self.depBidAmount3_3.setObjectName("depBidAmount3_3")
        self.gridLayout_12.addWidget(self.depBidAmount3_3, 2, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_12)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setGeometry(QRect(80, 350, 791, 16))
        self.label_30.setStyleSheet("border-bottom:8px double  \"grey\";")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setGeometry(QRect(80, 370, 981, 271))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QRect(0, 10, 921, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tradeDirect2 = QLabel(self.layoutWidget)
        self.tradeDirect2.setStyleSheet("color:\"white\";")
        self.tradeDirect2.setObjectName("tradeDirect2")
        self.horizontalLayout_3.addWidget(self.tradeDirect2)
        self.combind = QLabel(self.layoutWidget)
        self.combind.setStyleSheet("color:\"white\";font-weight:600;\n"
"")
        self.combind.setObjectName("combind")
        self.horizontalLayout_3.addWidget(self.combind)
        self.isQualify2Trade2 = QLabel(self.layoutWidget)
        self.isQualify2Trade2.setStyleSheet("color:\"white\";\n"
"")
        self.isQualify2Trade2.setObjectName("isQualify2Trade2")
        self.horizontalLayout_3.addWidget(self.isQualify2Trade2)
        self.isQualify2 = QLabel(self.layoutWidget)
        self.isQualify2.setStyleSheet("color:\"green\";font-weight:600;")
        self.isQualify2.setObjectName("isQualify2")
        self.horizontalLayout_3.addWidget(self.isQualify2)
        self.expIncomeRate2 = QLabel(self.layoutWidget)
        self.expIncomeRate2.setStyleSheet("color:\"white\";")
        self.expIncomeRate2.setObjectName("expIncomeRate2")
        self.horizontalLayout_3.addWidget(self.expIncomeRate2)
        self.incomeRateValue2 = QLabel(self.layoutWidget)
        self.incomeRateValue2.setStyleSheet("color:\"green\";font-weight:600")
        self.incomeRateValue2.setObjectName("incomeRateValue2")
        self.horizontalLayout_3.addWidget(self.incomeRateValue2)
        self.placeOrder2 = QPushButton(self.layoutWidget)
        self.placeOrder2.setStyleSheet("background-color:\"red\";\n"
"color:\"white\";")
        self.placeOrder2.setObjectName("placeOrder2")
        self.horizontalLayout_3.addWidget(self.placeOrder2)
        self.layoutWidget_2 = QWidget(self.widget_2)
        self.layoutWidget_2.setGeometry(QRect(0, 40, 771, 221))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.comCodeValue1 = QLabel(self.layoutWidget_2)
        self.comCodeValue1.setStyleSheet("font-weight:bold;color:rgb(220, 147, 0);")
        self.comCodeValue1.setObjectName("comCodeValue1")
        self.gridLayout_17.addWidget(self.comCodeValue1, 1, 1, 1, 1)
        self.comName1 = QLabel(self.layoutWidget_2)
        self.comName1.setStyleSheet("border-bottom:1px solid \"white\";\n"
"color:\"white\";")
        self.comName1.setObjectName("comName1")
        self.gridLayout_17.addWidget(self.comName1, 0, 0, 1, 1)
        self.comCode1 = QLabel(self.layoutWidget_2)
        self.comCode1.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.comCode1.setObjectName("comCode1")
        self.gridLayout_17.addWidget(self.comCode1, 0, 1, 1, 1)
        self.comNameValue1 = QLabel(self.layoutWidget_2)
        self.comNameValue1.setStyleSheet("\n"
"font-weight:bold;color:rgb(220, 147, 0);")
        self.comNameValue1.setObjectName("comNameValue1")
        self.gridLayout_17.addWidget(self.comNameValue1, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_17)
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.comRiseValue1 = QLabel(self.layoutWidget_2)
        self.comRiseValue1.setStyleSheet("color:\"green\";")
        self.comRiseValue1.setObjectName("comRiseValue1")
        self.gridLayout_18.addWidget(self.comRiseValue1, 1, 1, 1, 1)
        self.comRise1 = QLabel(self.layoutWidget_2)
        self.comRise1.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.comRise1.setObjectName("comRise1")
        self.gridLayout_18.addWidget(self.comRise1, 0, 1, 1, 1)
        self.comNetWorthValue1 = QLabel(self.layoutWidget_2)
        self.comNetWorthValue1.setStyleSheet("color:\"white\";")
        self.comNetWorthValue1.setObjectName("comNetWorthValue1")
        self.gridLayout_18.addWidget(self.comNetWorthValue1, 1, 0, 1, 1)
        self.comNetWorth1 = QLabel(self.layoutWidget_2)
        self.comNetWorth1.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.comNetWorth1.setObjectName("comNetWorth1")
        self.gridLayout_18.addWidget(self.comNetWorth1, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_18)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comBid1_1 = QLabel(self.layoutWidget_2)
        self.comBid1_1.setStyleSheet("color:\"white\";")
        self.comBid1_1.setObjectName("comBid1_1")
        self.gridLayout_3.addWidget(self.comBid1_1, 0, 0, 1, 1)
        self.comBidValue1_2 = QLabel(self.layoutWidget_2)
        self.comBidValue1_2.setStyleSheet("color:\"green\";")
        self.comBidValue1_2.setObjectName("comBidValue1_2")
        self.gridLayout_3.addWidget(self.comBidValue1_2, 1, 1, 1, 1)
        self.comBidAmount1_1 = QLabel(self.layoutWidget_2)
        self.comBidAmount1_1.setStyleSheet("background-color:\"orange\";")
        self.comBidAmount1_1.setObjectName("comBidAmount1_1")
        self.gridLayout_3.addWidget(self.comBidAmount1_1, 0, 2, 1, 1)
        self.comBid1_2 = QLabel(self.layoutWidget_2)
        self.comBid1_2.setStyleSheet("color:\"white\";")
        self.comBid1_2.setObjectName("comBid1_2")
        self.gridLayout_3.addWidget(self.comBid1_2, 1, 0, 1, 1)
        self.comBidAmount1_2 = QLabel(self.layoutWidget_2)
        self.comBidAmount1_2.setStyleSheet("color:\"yellow\";")
        self.comBidAmount1_2.setObjectName("comBidAmount1_2")
        self.gridLayout_3.addWidget(self.comBidAmount1_2, 1, 2, 1, 1)
        self.comBidAmount1_3 = QLabel(self.layoutWidget_2)
        self.comBidAmount1_3.setStyleSheet("color:\"yellow\";")
        self.comBidAmount1_3.setObjectName("comBidAmount1_3")
        self.gridLayout_3.addWidget(self.comBidAmount1_3, 2, 2, 1, 1)
        self.comBid1_3 = QLabel(self.layoutWidget_2)
        self.comBid1_3.setStyleSheet("color:\"white\";")
        self.comBid1_3.setObjectName("comBid1_3")
        self.gridLayout_3.addWidget(self.comBid1_3, 2, 0, 1, 1)
        self.comBidValue1_1 = QLabel(self.layoutWidget_2)
        self.comBidValue1_1.setStyleSheet("background-color:\"orange\";")
        self.comBidValue1_1.setScaledContents(False)
        self.comBidValue1_1.setObjectName("comBidValue1_1")
        self.gridLayout_3.addWidget(self.comBidValue1_1, 0, 1, 1, 1)
        self.comBidValue1_3 = QLabel(self.layoutWidget_2)
        self.comBidValue1_3.setStyleSheet("color:\"green\";")
        self.comBidValue1_3.setObjectName("comBidValue1_3")
        self.gridLayout_3.addWidget(self.comBidValue1_3, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.comCodeValue2 = QLabel(self.layoutWidget_2)
        self.comCodeValue2.setStyleSheet("font-weight:bold;\n"
"color:rgb(220, 147, 0);")
        self.comCodeValue2.setObjectName("comCodeValue2")
        self.gridLayout_19.addWidget(self.comCodeValue2, 1, 1, 1, 1)
        self.comName2 = QLabel(self.layoutWidget_2)
        self.comName2.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.comName2.setObjectName("comName2")
        self.gridLayout_19.addWidget(self.comName2, 0, 0, 1, 1)
        self.comNameValue2 = QLabel(self.layoutWidget_2)
        self.comNameValue2.setStyleSheet("font-weight:bold;color:rgb(220, 147, 0);")
        self.comNameValue2.setObjectName("comNameValue2")
        self.gridLayout_19.addWidget(self.comNameValue2, 1, 0, 1, 1)
        self.comCode2 = QLabel(self.layoutWidget_2)
        self.comCode2.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.comCode2.setObjectName("comCode2")
        self.gridLayout_19.addWidget(self.comCode2, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_19)
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.comRiseValue2 = QLabel(self.layoutWidget_2)
        self.comRiseValue2.setStyleSheet("color:\"red\";")
        self.comRiseValue2.setObjectName("comRiseValue2")
        self.gridLayout_20.addWidget(self.comRiseValue2, 1, 1, 1, 1)
        self.comNetWorthValue2 = QLabel(self.layoutWidget_2)
        self.comNetWorthValue2.setStyleSheet("color:\"white\";")
        self.comNetWorthValue2.setObjectName("comNetWorthValue2")
        self.gridLayout_20.addWidget(self.comNetWorthValue2, 1, 0, 1, 1)
        self.comRise2 = QLabel(self.layoutWidget_2)
        self.comRise2.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.comRise2.setObjectName("comRise2")
        self.gridLayout_20.addWidget(self.comRise2, 0, 1, 1, 1)
        self.comNetWorth2 = QLabel(self.layoutWidget_2)
        self.comNetWorth2.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.comNetWorth2.setObjectName("comNetWorth2")
        self.gridLayout_20.addWidget(self.comNetWorth2, 0, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_20)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.comAskValue2_1 = QLabel(self.layoutWidget_2)
        self.comAskValue2_1.setStyleSheet("background-color:\"orange\";")
        self.comAskValue2_1.setObjectName("comAskValue2_1")
        self.gridLayout_8.addWidget(self.comAskValue2_1, 0, 1, 1, 1)
        self.comAskAmount2_1 = QLabel(self.layoutWidget_2)
        self.comAskAmount2_1.setStyleSheet("background-color:\"orange\";")
        self.comAskAmount2_1.setObjectName("comAskAmount2_1")
        self.gridLayout_8.addWidget(self.comAskAmount2_1, 0, 2, 1, 2)
        self.comAskValue2_2 = QLabel(self.layoutWidget_2)
        self.comAskValue2_2.setStyleSheet("color:\"red\";")
        self.comAskValue2_2.setObjectName("comAskValue2_2")
        self.gridLayout_8.addWidget(self.comAskValue2_2, 1, 1, 1, 1)
        self.comAskAmount2_3 = QLabel(self.layoutWidget_2)
        self.comAskAmount2_3.setStyleSheet("color:\"yellow\";")
        self.comAskAmount2_3.setObjectName("comAskAmount2_3")
        self.gridLayout_8.addWidget(self.comAskAmount2_3, 2, 2, 1, 2)
        self.comAskValue2_3 = QLabel(self.layoutWidget_2)
        self.comAskValue2_3.setStyleSheet("color:\"red\";")
        self.comAskValue2_3.setObjectName("comAskValue2_3")
        self.gridLayout_8.addWidget(self.comAskValue2_3, 2, 1, 1, 1)
        self.comAsk2_3 = QLabel(self.layoutWidget_2)
        self.comAsk2_3.setStyleSheet("color:\"white\";")
        self.comAsk2_3.setObjectName("comAsk2_3")
        self.gridLayout_8.addWidget(self.comAsk2_3, 2, 0, 1, 1)
        self.comAskAmount2_2 = QLabel(self.layoutWidget_2)
        self.comAskAmount2_2.setStyleSheet("color:\"yellow\";")
        self.comAskAmount2_2.setObjectName("comAskAmount2_2")
        self.gridLayout_8.addWidget(self.comAskAmount2_2, 1, 2, 1, 2)
        self.comAsk2_1 = QLabel(self.layoutWidget_2)
        self.comAsk2_1.setStyleSheet("color:\"white\";")
        self.comAsk2_1.setObjectName("comAsk2_1")
        self.gridLayout_8.addWidget(self.comAsk2_1, 0, 0, 1, 1)
        self.comAsk2_2 = QLabel(self.layoutWidget_2)
        self.comAsk2_2.setStyleSheet("color:\"white\";")
        self.comAsk2_2.setObjectName("comAsk2_2")
        self.gridLayout_8.addWidget(self.comAsk2_2, 1, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comName3 = QLabel(self.layoutWidget_2)
        self.comName3.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.comName3.setObjectName("comName3")
        self.gridLayout_4.addWidget(self.comName3, 0, 0, 1, 1)
        self.comCode3 = QLabel(self.layoutWidget_2)
        self.comCode3.setStyleSheet("border-bottom:1px solid \"white\";color:\"white\";")
        self.comCode3.setObjectName("comCode3")
        self.gridLayout_4.addWidget(self.comCode3, 0, 1, 1, 1)
        self.comNameValue3 = QLabel(self.layoutWidget_2)
        self.comNameValue3.setStyleSheet("font-weight:bold;color:rgb(220, 147, 0);")
        self.comNameValue3.setObjectName("comNameValue3")
        self.gridLayout_4.addWidget(self.comNameValue3, 1, 0, 1, 1)
        self.comCodeValue3 = QLabel(self.layoutWidget_2)
        self.comCodeValue3.setStyleSheet("\n"
"font-weight:bold;\n"
"color:rgb(220, 147, 0);")
        self.comCodeValue3.setObjectName("comCodeValue3")
        self.gridLayout_4.addWidget(self.comCodeValue3, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_4)
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.comNetWorth3 = QLabel(self.layoutWidget_2)
        self.comNetWorth3.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.comNetWorth3.setObjectName("comNetWorth3")
        self.gridLayout_21.addWidget(self.comNetWorth3, 0, 0, 1, 1)
        self.comRise3 = QLabel(self.layoutWidget_2)
        self.comRise3.setStyleSheet("color:\"white\";border-bottom:1px solid \"white\";")
        self.comRise3.setObjectName("comRise3")
        self.gridLayout_21.addWidget(self.comRise3, 0, 1, 1, 1)
        self.comNetWorthValue3 = QLabel(self.layoutWidget_2)
        self.comNetWorthValue3.setStyleSheet("color:\"white\";")
        self.comNetWorthValue3.setObjectName("comNetWorthValue3")
        self.gridLayout_21.addWidget(self.comNetWorthValue3, 1, 0, 1, 1)
        self.comRiseValue3 = QLabel(self.layoutWidget_2)
        self.comRiseValue3.setStyleSheet("color:\"green\";")
        self.comRiseValue3.setObjectName("comRiseValue3")
        self.gridLayout_21.addWidget(self.comRiseValue3, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_21)
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.comAsk3_1 = QLabel(self.layoutWidget_2)
        self.comAsk3_1.setStyleSheet("color:\"white\";")
        self.comAsk3_1.setObjectName("comAsk3_1")
        self.gridLayout_22.addWidget(self.comAsk3_1, 0, 0, 1, 1)
        self.comAskValue3_1 = QLabel(self.layoutWidget_2)
        self.comAskValue3_1.setStyleSheet("background-color:\"orange\";")
        self.comAskValue3_1.setObjectName("comAskValue3_1")
        self.gridLayout_22.addWidget(self.comAskValue3_1, 0, 1, 1, 1)
        self.comAskAmount3_1 = QLabel(self.layoutWidget_2)
        self.comAskAmount3_1.setStyleSheet("background-color:\"orange\";")
        self.comAskAmount3_1.setObjectName("comAskAmount3_1")
        self.gridLayout_22.addWidget(self.comAskAmount3_1, 0, 2, 1, 1)
        self.comAsk3_2 = QLabel(self.layoutWidget_2)
        self.comAsk3_2.setStyleSheet("color:\"white\";")
        self.comAsk3_2.setObjectName("comAsk3_2")
        self.gridLayout_22.addWidget(self.comAsk3_2, 1, 0, 1, 1)
        self.comAskValue3_2 = QLabel(self.layoutWidget_2)
        self.comAskValue3_2.setStyleSheet("color:\"green\";")
        self.comAskValue3_2.setObjectName("comAskValue3_2")
        self.gridLayout_22.addWidget(self.comAskValue3_2, 1, 1, 1, 1)
        self.comAskAmount3_2 = QLabel(self.layoutWidget_2)
        self.comAskAmount3_2.setStyleSheet("color:\"yellow\";")
        self.comAskAmount3_2.setObjectName("comAskAmount3_2")
        self.gridLayout_22.addWidget(self.comAskAmount3_2, 1, 2, 1, 1)
        self.comAsk3_3 = QLabel(self.layoutWidget_2)
        self.comAsk3_3.setStyleSheet("color:\"white\";")
        self.comAsk3_3.setObjectName("comAsk3_3")
        self.gridLayout_22.addWidget(self.comAsk3_3, 2, 0, 1, 1)
        self.comAskValue3_3 = QLabel(self.layoutWidget_2)
        self.comAskValue3_3.setStyleSheet("color:\"green\";")
        self.comAskValue3_3.setObjectName("comAskValue3_3")
        self.gridLayout_22.addWidget(self.comAskValue3_3, 2, 1, 1, 1)
        self.comAskAmount3_3 = QLabel(self.layoutWidget_2)
        self.comAskAmount3_3.setStyleSheet("color:\"yellow\";")
        self.comAskAmount3_3.setObjectName("comAskAmount3_3")
        self.gridLayout_22.addWidget(self.comAskAmount3_3, 2, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_22)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        
        self.depTurnBackButton=QPushButton(self.widget1)#添加返回中枢界面按钮
        self.depTurnBackButton.setStyleSheet('background-color:\"orange\";color:\"white\"')
        self.depTurnBackButton.setObjectName('depTurnBackButton')
        self.depTurnBackButton.setText('返回')
        self.horizontalLayout_2.addWidget(self.depTurnBackButton)
        self.comTurnBackButton=QPushButton(self.widget1)
        self.comTurnBackButton.setStyleSheet('background-color:\"orange\";color:\"white\"')
        self.comTurnBackButton.setObjectName('comTurnBackButton')
        self.comTurnBackButton.setText('返回')
        self.horizontalLayout_3.addWidget(self.comTurnBackButton)
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        QObject.connect(self.depTurnBackButton,SIGNAL('clicked()'), self.turnBack)
        QObject.connect(self.comTurnBackButton,SIGNAL('clicked()'), self.turnBack)
    
    def turnBack(self):
        global Data,Codes
        w.cancelRequest(requestID)   #取消订阅
        Data={} #初始化Data
        Codes=[]    #初始化Codes
        stackedWid.setCurrentIndex(1)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle( "MainWindow")
        #------------------拆分部分-------------------# 
        if groupName=='GQGG':
            self.theme.setText("国企改革主题")
        elif groupName=='YDYL':
            self.theme.setText("一带一路主题")
        elif groupName=='ZQFJ':
            self.theme.setText("证券分级主题")
        elif groupName=='SZ50':
            self.theme.setText( "上证50分级主题")
        elif groupName=='JGFJ':
            self.theme.setText( "军工分级主题")
        self.tradeDirect1.setText( "交易方向>>")
        self.depart.setText( "拆分")
        self.isQualify2Trade1.setText( "是否符合交易要求>>")
        self.isQualify1.setText( "--")
        self.expIncomeRate1.setText( "预期收益率>>")
        self.incomeRateValue1.setText( "--")
        self.placeOrder1.setText( "机器下单")
        self.depCodeValue1.setText( "--")
        self.depName1.setText( "名称")
        self.depCode1.setText( "代码")
        self.depNameValue1.setText( "--")
        self.depRiseValue1.setText( "--")
        self.depRise1.setText( "涨幅")
        self.depNetWorthValue1.setText( "--")
        self.depNetWorth1.setText( "净值")
        self.depAsk1_1.setText( "卖一")
        self.depAskValue1_1.setText( "--")
        self.depAskAmount1_1.setText( "--")
        self.depAsk1_2.setText( "卖二")
        self.depAskValue1_2.setText( "--")
        self.depAskAmount1_2.setText( "--")
        self.depAsk1_3.setText( "卖三")
        self.depAskValue1_3.setText( "--")
        self.depAskAmount1_3.setText( "--")
        self.depNameValue2.setText( "--")
        self.depCodeValue2.setText( "--")
        self.depName2.setText( "名称")
        self.depCode2.setText( "代码")
        self.depRiseValue2.setText( "--")
        self.depNetWorthValue2.setText( "--")
        self.depRise2.setText( "涨幅")
        self.depNetWorth2.setText( "净值")
        self.depBidValue2_1.setText( "--")
        self.depBidAmount2_1.setText( "--")
        self.depBidValue2_2.setText( "--")
        self.depBidAmount2_3.setText( "--")
        self.depBidValue2_3.setText( "--")
        self.depBid2_3.setText( "买三")
        self.depBidAmount2_2.setText( "--")
        self.depBid2_1.setText( "买一")
        self.depBid2_2.setText( "买二")
        self.depName3.setText( "名称")
        self.depCode3.setText( "代码")
        self.depNameValue3.setText( "--")
        self.depCodeValue3.setText( "--")
        self.depNetWorth3.setText( "净值")
        self.depRise3.setText( "涨幅")
        self.depNetWorthValue3.setText( "--")
        self.depRiseValue3.setText( "--")
        self.depBid3_1.setText( "买一")
        self.depBidValue3_1.setText( "--")
        self.depBidAmount3_1.setText( "--")
        self.depBid3_2.setText( "买二")
        self.depBidValue3_2.setText( "--")
        self.depBidAmount3_2.setText( "--")
        self.depBid3_3.setText( "买三")
        self.depBidValue3_3.setText( "--")
        self.depBidAmount3_3.setText( "--")
        #------------------合并部分-------------------#       
        self.tradeDirect2.setText( "交易方向>>")
        self.combind.setText( "合并")
        self.isQualify2Trade2.setText( "是否符合交易要求>>")
        self.isQualify2.setText( "否")
        self.expIncomeRate2.setText( "预期收益率>>")
        self.incomeRateValue2.setText( "--")
        self.placeOrder2.setText( "机器下单")
        self.comCodeValue1.setText( "--")
        self.comName1.setText( "名称")
        self.comCode1.setText( "代码")
        if groupName=='GQGG':
            self.comNameValue1.setText("国企改革主题")
        elif groupName=='YDYL':
            self.comNameValue1.setText("一带一路主题")
        elif groupName=='ZQFJ':
            self.comNameValue1.setText("证券分级主题")
        elif groupName=='SZ50':
            self.comNameValue1.setText( "上证50分级主题")
        elif groupName=='JGFJ':
            self.comNameValue1.setText( "军工分级主题")
        self.comRiseValue1.setText( "--")
        self.comRise1.setText( "涨幅")
        self.comNetWorthValue1.setText( "--")
        self.comNetWorth1.setText( "净值")
        self.comBid1_1.setText( "买一")
        self.comBidValue1_2.setText( "--")
        self.comBidAmount1_1.setText( "--")
        self.comBid1_2.setText( "买二")
        self.comBidAmount1_2.setText( "--")
        self.comBidAmount1_3.setText( "--")
        self.comBid1_3.setText( "买三")
        self.comBidValue1_1.setText( "--")
        self.comBidValue1_3.setText( "--")
        self.comCodeValue2.setText( "--")
        self.comName2.setText( "名称")
        if groupName=='GQGG':
            self.comNameValue2.setText("国企改A")
        elif groupName=='YDYL':
            self.comNameValue2.setText("一带一A")
        elif groupName=='ZQFJ':
            self.comNameValue2.setText("证券A")
        elif groupName=='SZ50':
            self.comNameValue2.setText( "上证50A")
        elif groupName=='JGFJ':
            self.comNameValue2.setText( "军工A")
        self.comCode2.setText( "代码")
        self.comRiseValue2.setText( "--")
        self.comNetWorthValue2.setText( "--")
        self.comRise2.setText( "涨幅")
        self.comNetWorth2.setText( "净值")
        self.comAskValue2_1.setText( "--")
        self.comAskAmount2_1.setText( "--")
        self.comAskValue2_2.setText( "--")
        self.comAskAmount2_3.setText( "--")
        self.comAskValue2_3.setText( "--")
        self.comAsk2_3.setText( "卖三")
        self.comAskAmount2_2.setText( "--")
        self.comAsk2_1.setText( "卖一")
        self.comAsk2_2.setText( "卖二")
        self.comName3.setText( "名称")
        self.comCode3.setText( "代码")
        self.comNameValue3.setText( "--")
        self.comCodeValue3.setText( "--")
        self.comNetWorth3.setText( "净值")
        self.comRise3.setText( "涨幅")
        self.comNetWorthValue3.setText( "--")
        self.comRiseValue3.setText( "--")
        self.comAsk3_1.setText( "卖一")
        self.comAskValue3_1.setText( "--")
        self.comAskAmount3_1.setText( "--")
        self.comAsk3_2.setText( "卖二")
        self.comAskValue3_2.setText( "--")
        self.comAskAmount3_2.setText( "--")
        self.comAsk3_3.setText( "卖三")
        self.comAskValue3_3.setText( "--")
        self.comAskAmount3_3.setText( "--")
#----------------创建类实例，以后flushScreen调用-----------------
# #变量命名规则：类名_别名
Login_login=Login()
Login_login.setupUi(qWid1)
Pivot_pivot=Pivot()
Pivot_pivot.setupUi(qWid2)
SubPivot_subpivot=SubPivot()
SubPivot_subpivot.setupUi(qWid3)
stackedWid.addWidget(qWid1)    #stackedwidget添加子标签页
stackedWid.addWidget(qWid2)
stackedWid.addWidget(qWid3)
stackedWid.setCurrentIndex(0)
stackedWid.setFixedSize(640,338)
#==================函数定义===================
#刷新界面，用于回调函数中更新行情界面
def flushScreen(Data):
    global groupName,w,SubPivot_subpivot
    print('Into FlushScreen...')
    getcontext().prec=4     #设置全局精度为小数点后4位
    depNetWorthValue1 = Decimal(Data['RT_LAST'][0]) /Decimal(1)
    depRiseValue1 = Decimal(Data['RT_PCT_CHG'][0])  /Decimal(1)
    depNetWorthValue2 = Decimal(Data['RT_LAST'][1]) /Decimal(1)
    depRiseValue2 = Decimal(Data['RT_PCT_CHG'][1])  /Decimal(1)
    depNetWorthValue3 = Decimal(Data['RT_LAST'][2]) /Decimal(1)
    depRiseValue3 = Decimal(Data['RT_PCT_CHG'][2])  /Decimal(1)
    depAskValue1_1 = Decimal(Data['RT_ASK1'][0])    /Decimal(1)
    depAskValue1_2 = Decimal(Data['RT_ASK2'][0])    /Decimal(1)
    depAskValue1_3 = Decimal(Data['RT_ASK3'][0])    /Decimal(1)
    depAskAmount1_1 = math.floor(Decimal(Data['RT_ASIZE1'][0]) /Decimal(100))
    depAskAmount1_2 = math.floor(Decimal(Data['RT_ASIZE2'][0]) /Decimal(100))
    depAskAmount1_3 = math.floor(Decimal(Data['RT_ASIZE3'][0]) /Decimal(100))
    depBidValue2_1 = Decimal(Data['RT_BID1'][1])    /Decimal(1)
    depBidValue2_2 = Decimal(Data['RT_BID2'][1])    /Decimal(1)
    depBidValue2_3 = Decimal(Data['RT_BID3'][1])    /Decimal(1)
    depBidAmount2_1 =math.floor(Decimal(Data['RT_BSIZE1'][1])  /Decimal(100))
    depBidAmount2_2 =math.floor(Decimal(Data['RT_BSIZE2'][1])  /Decimal(100))
    depBidAmount2_3 =math.floor(Decimal(Data['RT_BSIZE3'][1])  /Decimal(100))
    depBidValue3_1 = Decimal(Data['RT_BID1'][2])    /Decimal(1)
    depBidValue3_2 = Decimal(Data['RT_BID2'][2])    /Decimal(1)
    depBidValue3_3 = Decimal(Data['RT_BID3'][2])    /Decimal(1)
    depBidAmount3_1 = math.floor(Decimal(Data['RT_BSIZE1'][2]) /Decimal(100))
    depBidAmount3_2 = math.floor(Decimal(Data['RT_BSIZE2'][2]) /Decimal(100))
    depBidAmount3_3 = math.floor(Decimal(Data['RT_BSIZE3'][2]) /Decimal(100))
    comNetWorthValue1 = depNetWorthValue1
    comRiseValue1 = depRiseValue1
    comNetWorthValue2 = depNetWorthValue2
    comRiseValue2 = depRiseValue2
    comNetWorthValue3 = depNetWorthValue3
    comRiseValue3 = depRiseValue3
    comBidValue1_1 = Decimal(Data['RT_BID1'][0])   /Decimal(1)
    comBidValue1_2 = Decimal(Data['RT_BID2'][0])   /Decimal(1)
    comBidValue1_3 = Decimal(Data['RT_BID3'][0])   /Decimal(1)
    comBidAmount1_1 = math.floor(Decimal(Data['RT_BSIZE1'][0])/Decimal(100))
    comBidAmount1_2 = math.floor(Decimal(Data['RT_BSIZE2'][0])/Decimal(100))
    comBidAmount1_3 = math.floor(Decimal(Data['RT_BSIZE3'][0])/Decimal(100))
    comAskValue2_1 = Decimal(Data['RT_ASK1'][1])   /Decimal(1)
    comAskValue2_2 = Decimal(Data['RT_ASK2'][1])   /Decimal(1)
    comAskValue2_3 = Decimal(Data['RT_ASK3'][1])   /Decimal(1)
    comAskAmount2_1 = math.floor(Decimal(Data['RT_ASIZE1'][1])/Decimal(100))
    comAskAmount2_2 = math.floor(Decimal(Data['RT_ASIZE2'][1])/Decimal(100))
    comAskAmount2_3 = math.floor(Decimal(Data['RT_ASIZE3'][1])/Decimal(100))
    comAskValue3_1 = Decimal(Data['RT_ASK1'][2])   /Decimal(1)
    comAskValue3_2 = Decimal(Data['RT_ASK2'][2])   /Decimal(1)
    comAskValue3_3 = Decimal(Data['RT_ASK3'][2])   /Decimal(1)
    comAskAmount3_1 = math.floor(Decimal(Data['RT_ASIZE1'][2])/Decimal(100))
    comAskAmount3_2 = math.floor(Decimal(Data['RT_ASIZE2'][2])/Decimal(100))
    comAskAmount3_3 = math.floor(Decimal(Data['RT_ASIZE3'][2])/Decimal(100))
    # 行情参数计算
    incomeRateValue1 = Decimal(100) * (depBidValue2_1 + depBidValue3_1 - Decimal(2) * depAskValue1_1) / Decimal(2) / depAskValue1_1 - Decimal(0.05)  # 拆分收益率计算
    if incomeRateValue1 >= 0.1 and depAskAmount1_1 > 500 and depBidAmount2_1 > 250 and depBidAmount3_1 > 250:  # 计算是否符合交易要求
        SubPivot_subpivot.isQualify1.setText('是')
        SubPivot_subpivot.isQualify1.setStyleSheet("color:\"red\";font-weight:600;")
    else:
        SubPivot_subpivot.isQualify1.setText('否')
        SubPivot_subpivot.isQualify1.setStyleSheet("color:\"green\";font-weight:600;")
    
    incomeRateValue2 = Decimal(100) * (Decimal(2) * comBidValue1_1 - comAskValue2_1 - comAskValue3_1) / (comAskValue2_1 + comAskValue3_1) - Decimal(0.05)  # 合并收益率计算
    if incomeRateValue2 >= 0.1 and comBidAmount1_1 > 500 and comAskAmount2_1 > 250 and comAskAmount3_1 > 250:
        SubPivot_subpivot.isQualify2.setText('是')
        SubPivot_subpivot.isQualify2.setStyleSheet("color:\"red\";font-weight:600;")
    else:
        SubPivot_subpivot.isQualify1.setText('否')
        SubPivot_subpivot.isQualify2.setStyleSheet("color:\"green\";font-weight:600;")
    # 实时行情界面显示
    if groupName=='GQGG':
        SubPivot_subpivot.theme.setText("国企改革主题")
    elif groupName=='YDYL':
        SubPivot_subpivot.theme.setText("一带一路主题")
    elif groupName=='ZQFJ':
        SubPivot_subpivot.theme.setText("证券分级主题")
    elif groupName=='SZ50':
        SubPivot_subpivot.theme.setText("上证50分级主题")
    elif groupName=='JGFJ':
        SubPivot_subpivot.theme.setText("军工分级主题")
    SubPivot_subpivot.tradeDirect1.setText( "交易方向>>")
    SubPivot_subpivot.depart.setText( "拆分")
    SubPivot_subpivot.isQualify2Trade1.setText( "是否符合交易要求>>")
    SubPivot_subpivot.expIncomeRate1.setText( "预期收益率>>")
    SubPivot_subpivot.incomeRateValue1.setText( str(incomeRateValue1)+'%')
    if incomeRateValue1<0:      #根据盈利与亏损，采用不同颜色显示
        SubPivot_subpivot.incomeRateValue1.setStyleSheet("color:\"green\";font-weight:600")
    else:
        SubPivot_subpivot.incomeRateValue1.setStyleSheet("color:\"red\";font-weight:600")
    SubPivot_subpivot.placeOrder1.setText( "机器下单")
    SubPivot_subpivot.depName1.setText( "名称")
    SubPivot_subpivot.depCode1.setText( "代码")
    if groupName=='GQGG':
        SubPivot_subpivot.depNameValue1.setText("国企改革")
        SubPivot_subpivot.depCodeValue1.setText("502006")
    elif groupName=='YDYL':
        SubPivot_subpivot.depNameValue1.setText("一带一路")
        SubPivot_subpivot.depCodeValue1.setText("502013")
    elif groupName=='ZQFJ':
        SubPivot_subpivot.depNameValue1.setText("证券分级")
        SubPivot_subpivot.depCodeValue1.setText("502010")
    elif groupName=='SZ50':
        SubPivot_subpivot.depNameValue1.setText("50分级")
        SubPivot_subpivot.depCodeValue1.setText("502048")
    elif groupName=='JGFJ':
        SubPivot_subpivot.depNameValue1.setText("军工分级")
        SubPivot_subpivot.depCodeValue1.setText("502003")
    SubPivot_subpivot.depRise1.setText( "涨幅")
    SubPivot_subpivot.depRiseValue1.setText( str(depRiseValue1*100)+'%')
    if depRiseValue1>0:
        SubPivot_subpivot.depRiseValue1.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depRiseValue1.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depNetWorth1.setText( "净值")
    SubPivot_subpivot.depNetWorthValue1.setText( str(depNetWorthValue1))
    SubPivot_subpivot.depAsk1_1.setText( "卖一")
    SubPivot_subpivot.depAskValue1_1.setText( str(depAskValue1_1))
    if depRiseValue1>0:
        SubPivot_subpivot.depAskValue1_1.setStyleSheet('background-color:\"orange\";color:\"red\"')
    else:
        SubPivot_subpivot.depAskValue1_1.setStyleSheet('background-color:\"orange\";color:\"green\"')
    SubPivot_subpivot.depAskAmount1_1.setText( str(depAskAmount1_1))
    SubPivot_subpivot.depAsk1_2.setText( "卖二")
    SubPivot_subpivot.depAskValue1_2.setText( str(depAskValue1_2))
    if depRiseValue1>0:
        SubPivot_subpivot.depAskValue1_2.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depAskValue1_2.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depAskAmount1_2.setText( str(depAskAmount1_2))
    SubPivot_subpivot.depAsk1_3.setText( "卖三")
    SubPivot_subpivot.depAskValue1_3.setText( str(depAskValue1_3))
    if depRiseValue1>0:
        SubPivot_subpivot.depAskValue1_3.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depAskValue1_3.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depAskAmount1_3.setText( str(depAskAmount1_3))
    if groupName=='GQGG':
        SubPivot_subpivot.depNameValue2.setText("国企改A")
        SubPivot_subpivot.depCodeValue2.setText("502007")
    elif groupName=='YDYL':
        SubPivot_subpivot.depNameValue2.setText("一带一A")
        SubPivot_subpivot.depCodeValue2.setText("502014")
    elif groupName=='ZQFJ':
        SubPivot_subpivot.depNameValue2.setText("证券A")
        SubPivot_subpivot.depCodeValue2.setText("502011")
    elif groupName=='SZ50':
        SubPivot_subpivot.depNameValue2.setText("上证50A")
        SubPivot_subpivot.depCodeValue2.setText("502049")
    elif groupName=='JGFJ':
        SubPivot_subpivot.depNameValue2.setText("军工A")
        SubPivot_subpivot.depCodeValue2.setText("502004")
    SubPivot_subpivot.depName2.setText( "名称")
    SubPivot_subpivot.depCode2.setText( "代码")
    SubPivot_subpivot.depRiseValue2.setText( str(depRiseValue2*100)+'%')
    if depRiseValue2>0:
        SubPivot_subpivot.depRiseValue2.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depRiseValue2.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depNetWorthValue2.setText( str(depNetWorthValue2))
    SubPivot_subpivot.depRise2.setText( "涨幅")
    SubPivot_subpivot.depNetWorth2.setText( "净值")
    SubPivot_subpivot.depBid2_1.setText( "买一")
    SubPivot_subpivot.depBidValue2_1.setText( str(depBidValue2_1))
    if depRiseValue2>0:
        SubPivot_subpivot.depBidValue2_1.setStyleSheet('background-color:\"orange\";color:\"red\"')
    else:
        SubPivot_subpivot.depBidValue2_1.setStyleSheet('background-color:\"orange\";color:\"green\"')
    SubPivot_subpivot.depBidAmount2_1.setText( str(depBidAmount2_1))
    SubPivot_subpivot.depBid2_2.setText( "买二")
    SubPivot_subpivot.depBidValue2_2.setText( str(depBidValue2_2))
    if depRiseValue1>0:
        SubPivot_subpivot.depBidValue2_2.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depBidValue2_2.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depBidAmount2_2.setText( str(depBidAmount2_2))
    SubPivot_subpivot.depBid2_3.setText( "买三")
    SubPivot_subpivot.depBidValue2_3.setText( str(depBidValue2_3))
    if depRiseValue1>0:
        SubPivot_subpivot.depBidValue2_3.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depBidValue2_3.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depBidAmount2_3.setText( str(depBidAmount2_3))
    SubPivot_subpivot.depName3.setText( "名称")
    SubPivot_subpivot.depCode3.setText( "代码")
    if groupName=='GQGG':
        SubPivot_subpivot.depNameValue3.setText("国企改B")
        SubPivot_subpivot.depCodeValue3.setText("502008")
    elif groupName=='YDYL':
        SubPivot_subpivot.depNameValue3.setText("一带一B")
        SubPivot_subpivot.depCodeValue3.setText("502015")
    elif groupName=='ZQFJ':
        SubPivot_subpivot.depNameValue3.setText("证券B")
        SubPivot_subpivot.depCodeValue3.setText("502012")
    elif groupName=='SZ50':
        SubPivot_subpivot.depNameValue3.setText("上证50B")
        SubPivot_subpivot.depCodeValue3.setText("502050")
    elif groupName=='JGFJ':
        SubPivot_subpivot.depNameValue3.setText("军工B")
        SubPivot_subpivot.depCodeValue3.setText("502005")
    SubPivot_subpivot.depNetWorth3.setText( "净值")
    SubPivot_subpivot.depRise3.setText( "涨幅")
    SubPivot_subpivot.depRiseValue3.setText( str(depRiseValue3*100)+'%')
    if depRiseValue3>0:
        SubPivot_subpivot.depRiseValue3.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depRiseValue3.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depNetWorthValue3.setText( str(depNetWorthValue3))
    SubPivot_subpivot.depBid3_1.setText( "买一")
    SubPivot_subpivot.depBidValue3_1.setText( str(depBidValue3_1))
    if depRiseValue3>0:
        SubPivot_subpivot.depBidValue3_1.setStyleSheet('background-color:\"orange\";color:\"red\"')
    else:
        SubPivot_subpivot.depBidValue3_1.setStyleSheet('background-color:\"orange\";color:\"green\"')
    SubPivot_subpivot.depBidAmount3_1.setText( str(depBidAmount3_1))
    SubPivot_subpivot.depBid3_2.setText( "买二")
    SubPivot_subpivot.depBidValue3_2.setText( str(depBidValue3_2))
    if depRiseValue3>0:
        SubPivot_subpivot.depBidValue3_2.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depBidValue3_2.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depBidAmount3_2.setText( str(depBidAmount3_2))
    SubPivot_subpivot.depBid3_3.setText( "买三")
    SubPivot_subpivot.depBidValue3_3.setText( str(depBidValue3_3))
    if depRiseValue3>0:
        SubPivot_subpivot.depBidValue3_3.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.depBidValue3_3.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.depBidAmount3_3.setText( str(depBidAmount3_3))
    #------------------合并部分-------------------#       
    SubPivot_subpivot.tradeDirect2.setText( "交易方向>>")
    SubPivot_subpivot.combind.setText( "合并")
    SubPivot_subpivot.isQualify2Trade2.setText( "是否符合交易要求>>")
    SubPivot_subpivot.isQualify2.setText( "否")
    SubPivot_subpivot.expIncomeRate2.setText( "预期收益率>>")
    SubPivot_subpivot.incomeRateValue2.setText( str(incomeRateValue2)+'%')
    if incomeRateValue2<0:
        SubPivot_subpivot.incomeRateValue2.setStyleSheet('color:\"green\";font-weight:600')
    else:
        SubPivot_subpivot.incomeRateValue2.setStyleSheet('color:\"red\";font-weight:600')
    SubPivot_subpivot.placeOrder2.setText( "机器下单")
    SubPivot_subpivot.comName1.setText( "名称")
    SubPivot_subpivot.comCode1.setText( "代码")
    if groupName=='GQGG':
        SubPivot_subpivot.comNameValue1.setText("国企改革")
        SubPivot_subpivot.comCodeValue1.setText("502006")
    elif groupName=='YDYL':
        SubPivot_subpivot.comNameValue1.setText("一带一路")
        SubPivot_subpivot.comCodeValue1.setText("502013")
    elif groupName=='ZQFJ':
        SubPivot_subpivot.comNameValue1.setText("证券分级")
        SubPivot_subpivot.comCodeValue1.setText("502010")
    elif groupName=='SZ50':
        SubPivot_subpivot.comNameValue1.setText("50分级")
        SubPivot_subpivot.comCodeValue1.setText("502048")
    elif groupName=='JGFJ':
        SubPivot_subpivot.comNameValue1.setText("军工分级")
        SubPivot_subpivot.comCodeValue1.setText("502003")
    SubPivot_subpivot.comRise1.setText( "涨幅")
    SubPivot_subpivot.comRiseValue1.setText( str(comRiseValue1*100)+'%')
    if comRiseValue1>0:
        SubPivot_subpivot.comRiseValue1.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comRiseValue1.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comNetWorthValue1.setText( str(comNetWorthValue1))
    SubPivot_subpivot.comNetWorth1.setText( "净值")
    SubPivot_subpivot.comBid1_1.setText( "买一")
    SubPivot_subpivot.comBidValue1_1.setText( str(comBidValue1_1))
    if comRiseValue1>0:
        SubPivot_subpivot.comBidValue1_1.setStyleSheet('background-color:\"orange\";color:\"red\"')
    else:
        SubPivot_subpivot.comBidValue1_1.setStyleSheet('background-color:\"orange\";color:\"green\"')
    SubPivot_subpivot.comBidAmount1_1.setText( str(comBidAmount1_1))
    SubPivot_subpivot.comBid1_2.setText( "买二")
    SubPivot_subpivot.comBidValue1_2.setText( str(comBidValue1_2))
    if comRiseValue1>0:
        SubPivot_subpivot.comBidValue1_2.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comBidValue1_2.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comBidAmount1_2.setText( str(comBidAmount1_2))
    SubPivot_subpivot.comBid1_3.setText( "买三")
    SubPivot_subpivot.comBidValue1_3.setText( str(comBidValue1_3))
    if comRiseValue1>0:
        SubPivot_subpivot.comBidValue1_3.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comBidValue1_3.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comBidAmount1_3.setText( str(comBidAmount1_3))
    SubPivot_subpivot.comName2.setText( "名称")
    if groupName=='GQGG':
        SubPivot_subpivot.comNameValue2.setText("国企改A")
        SubPivot_subpivot.comCodeValue2.setText("502007")
    elif groupName=='YDYL':
        SubPivot_subpivot.comNameValue2.setText("一带一A")
        SubPivot_subpivot.comCodeValue2.setText("502014")
    elif groupName=='ZQFJ':
        SubPivot_subpivot.comNameValue2.setText("证券A")
        SubPivot_subpivot.comCodeValue2.setText("502011")
    elif groupName=='SZ50':
        SubPivot_subpivot.comNameValue2.setText("上证50A")
        SubPivot_subpivot.comCodeValue2.setText("502049")
    elif groupName=='JGFJ':
        SubPivot_subpivot.comNameValue2.setText("军工A")
        SubPivot_subpivot.comCodeValue2.setText("502004")
    SubPivot_subpivot.comCode2.setText( "代码")
    SubPivot_subpivot.comNetWorthValue2.setText( str(comNetWorthValue2))
    SubPivot_subpivot.comRise2.setText( "涨幅")
    SubPivot_subpivot.comRiseValue2.setText( str(comRiseValue2*100)+'%')
    if comRiseValue2>0:
        SubPivot_subpivot.comRiseValue2.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comRiseValue2.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comNetWorth2.setText( "净值")
    SubPivot_subpivot.comAsk2_1.setText( "卖一")
    SubPivot_subpivot.comAskValue2_1.setText( str(comAskValue2_1))
    if comRiseValue2>0:
        SubPivot_subpivot.comAskValue2_1.setStyleSheet('background-color:\"orange\";color:\"red\"')
    else:
        SubPivot_subpivot.comAskValue2_1.setStyleSheet('background-color:\"orange\";color:\"green\"')
    SubPivot_subpivot.comAskAmount2_1.setText( str(comAskAmount2_1))
    SubPivot_subpivot.comAsk2_2.setText( "卖二")
    SubPivot_subpivot.comAskValue2_2.setText( str(comAskValue2_2))
    if comRiseValue2>0:
        SubPivot_subpivot.comAskValue2_2.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comAskValue2_2.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comAskAmount2_2.setText( str(comAskAmount2_2))
    SubPivot_subpivot.comAsk2_3.setText( "卖三")
    SubPivot_subpivot.comAskValue2_3.setText( str(comAskValue2_3))
    if comRiseValue2>0:
        SubPivot_subpivot.comAskValue2_3.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comAskValue2_3.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comAskAmount2_3.setText( str(comAskAmount2_3))
    
    SubPivot_subpivot.comName3.setText( "名称")
    SubPivot_subpivot.comCode3.setText( "代码")
    if groupName=='GQGG':
        SubPivot_subpivot.comNameValue3.setText("国企改B")
        SubPivot_subpivot.comCodeValue3.setText("502008")
    elif groupName=='YDYL':
        SubPivot_subpivot.comNameValue3.setText("一带一B")
        SubPivot_subpivot.comCodeValue3.setText("502015")
    elif groupName=='ZQFJ':
        SubPivot_subpivot.comNameValue3.setText("证券B")
        SubPivot_subpivot.comCodeValue3.setText("502012")
    elif groupName=='SZ50':
        SubPivot_subpivot.comNameValue3.setText("上证50B")
        SubPivot_subpivot.comCodeValue3.setText("502050")
    elif groupName=='JGFJ':
        SubPivot_subpivot.comNameValue3.setText("军工B")
        SubPivot_subpivot.comCodeValue3.setText("502005")
    SubPivot_subpivot.comNetWorth3.setText( "净值")
    SubPivot_subpivot.comRise3.setText( "涨幅")
    SubPivot_subpivot.comRiseValue3.setText( str(comRiseValue3*100)+'%')
    if comRiseValue3>0:
        SubPivot_subpivot.comRiseValue3.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comRiseValue3.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comNetWorthValue3.setText(str(comNetWorthValue3))
    SubPivot_subpivot.comAsk3_1.setText( "卖一")
    SubPivot_subpivot.comAskValue3_1.setText( str(comAskValue3_1))
    if comRiseValue3>0:
        SubPivot_subpivot.comAskValue3_1.setStyleSheet('background-color:\"orange\";color:\"red\"')
    else:
        SubPivot_subpivot.comAskValue3_1.setStyleSheet('background-color:\"orange\";color:\"green\"')
    SubPivot_subpivot.comAskAmount3_1.setText( str(comAskAmount3_1))
    SubPivot_subpivot.comAsk3_2.setText( "卖二")
    SubPivot_subpivot.comAskValue3_2.setText( str(comAskValue3_2))
    if comRiseValue3>0:
        SubPivot_subpivot.comAskValue3_2.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comAskValue3_2.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comAskAmount3_2.setText( str(comAskAmount3_2))
    SubPivot_subpivot.comAsk3_3.setText( "卖三")
    SubPivot_subpivot.comAskValue3_3.setText( str(comAskValue3_3))
    if comRiseValue3>0:
        SubPivot_subpivot.comAskValue3_3.setStyleSheet('color:\"red\"')
    else:
        SubPivot_subpivot.comAskValue3_3.setStyleSheet('color:\"green\"')
    SubPivot_subpivot.comAskAmount3_3.setText( str(comAskAmount3_3))
    
    print('Finish FlushScreen...')

#------------------
#Wind行情订阅回调函数
def getData(data):
    global requestID,Data,Codes
    if data.ErrorCode != 0:
        return data.ErrorCode
    
    #获取订阅ID
    requestID=data.RequestID
    if len(data.Codes)==1:  #行情实时订阅时只返回单个证券的变化部分
        index=Codes.index(data.Codes[0])    #data.Codes is a list
        for i in range(len(data.Fields)):
            Data[data.Fields[i]][index] = data.Data[i][0]   #data.Data is a list
    else:   #实时行情第一次调用时会返回多个证券的数据
        for i in range(len(data.Fields)):
            Data[data.Fields[i]] = data.Data[i]
    flushScreen(Data)
#------------------

#------------------住程序启动-----------------
stackedWid.show()
sys.exit(main.exec_())
#------------------------------------------

