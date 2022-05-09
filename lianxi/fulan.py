from PySide2.QtWidgets import QApplication, QMessageBox,QFileDialog
from PySide2.QtUiTools import QUiLoader
import xlrd
import pymysql

class Stats:
    file = ""
    users = ""
    password = ""
    duans = ""
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('qiping.ui')
        self.ui.pushButton_2.clicked.connect(self.handleCalc)
        self.ui.pushButton_3.clicked.connect(self.daru)
        self.ui.pushButton.clicked.connect(self.lianjie)
    def lianjie(self):
        Stats.users = self.ui.lineEdit.text()
        Stats.password = self.ui.lineEdit_2.text()
        Stats.duans = self.ui.spinBox.text()
        print(Stats.users, Stats.password, Stats.duans, sep="||")
    def daru(self):
        if(Stats.file == ""):
            QMessageBox.critical(
                self.ui,
                '错误',
                '请选择文件！')
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='chuli',
            charset='utf8'
        )
        cursor = conn.cursor()  # 获取一个光标
        sql = 'insert into wxpjg_naturalgas (city,shiyohng,licenseplate,productname,sname,medium,maxPressure,yongji,rjbh,zhizao,manufacturedate,servicelife,company,inspection,shiyong,operationtime,jcheckdate,jigou,xcheckdate,dataentry) ' \
              'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        book = xlrd.open_workbook(Stats.file)
        sheet = book.sheet_by_name('Sheet1')
        count = 1
        counts = 1
        while (counts < sheet.nrows):
            list = []
            while (count < sheet.ncols):
                incomes = sheet.col_values(colx=count, start_rowx=counts, end_rowx=counts + 1)
                for value in incomes:
                    if (count == 11):
                        value = xlrd.xldate_as_datetime(value, 0).strftime('%Y-%m-%d')
                    if (count == 16):
                        value = xlrd.xldate_as_datetime(value, 0).strftime('%Y-%m-%d')
                    if (count == 17):
                        value = xlrd.xldate_as_datetime(value, 0).strftime('%Y-%m-%d')
                    if (count == 19):
                        value = xlrd.xldate_as_datetime(value, 0).strftime('%Y-%m-%d')
                    list.append(value)
                count = count + 1
            counts = counts + 1
            count = 1
            try:
                bol = cursor.execute(sql, list)
                conn.commit()
            except:
                QMessageBox.critical(
                    self.ui,
                    '错误',
                    '导入错误！')
                break
        if(bol):
            QMessageBox.information(
                self.ui,
                '操作成功',
                '导入成功')
    def handleCalc(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择你要上传的文件",  # 标题
            r"e:python",  # 起始目录
            "图片类型(*.jpg *png);;Elexe(*.xlsx);;worder(*.word)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.label_5.setProperty('text', filePath)
        Stats.file = filePath
app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()