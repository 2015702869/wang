import xlrd
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='chuli',
    charset='utf8'
)
cursor =conn.cursor()  #获取一个光标
sql ='insert into wxpjg_naturalgas (city,shiyohng,licenseplate,productname,sname,medium,maxPressure,yongji,rjbh,zhizao,manufacturedate,servicelife,company,inspection,shiyong,operationtime,jcheckdate,jigou,xcheckdate,dataentry) ' \
     'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
book = xlrd.open_workbook("E:/python/ceshi.xlsx")
sheet = book.sheet_by_name('Sheet1')
count = 1
counts = 1
while(counts < sheet.nrows):
    list = []
    while (count < sheet.ncols):
        incomes = sheet.col_values(colx=count, start_rowx=counts, end_rowx=counts+1)
        for value in incomes:
            if(count == 11):
                value = xlrd.xldate_as_datetime(value, 0).strftime('%Y-%m-%d')
            if(count == 16):
                value = xlrd.xldate_as_datetime(value, 0).strftime('%Y-%m-%d')
            if(count == 17):
                value = xlrd.xldate_as_datetime(value, 0).strftime('%Y-%m-%d')
            if(count == 19):
                value = xlrd.xldate_as_datetime(value, 0).strftime('%Y-%m-%d')
            list.append(value)
        count = count + 1
    counts = counts + 1
    count = 1
    cursor.execute(sql, list)
    conn.commit()