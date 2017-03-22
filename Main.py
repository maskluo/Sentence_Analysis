#coding=gbk
import Analysis
import csv

csvfile = file('..\Result\Result.csv', 'wb')
writer = csv.writer(csvfile)

i = 1
while i <= 4:
    #路径
    source = '..\Data\Test'+str(i)+'.txt'

    #处理
    result = Analysis.analysis(source)

    #输出到CSV
    writer.writerow(result)

    i += 1

csvfile.close()
