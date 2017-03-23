#coding=gbk

import Analysis
import csv

FileNumber = 1
csvfile = file('..\Result\Result.csv', 'wb')
writer = csv.writer(csvfile)

i = 1
while i <= FileNumber:
    #处理
    result = Analysis.analysis(FileNumber)

    #输出到CSV
    writer.writerow(result)

    i += 1

csvfile.close()
