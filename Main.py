#coding=gbk

import Analysis
import csv

FileNumber = 1
csvfile = file('..\Result\Result.csv', 'wb')
writer = csv.writer(csvfile)

i = 1
while i <= FileNumber:
    #����
    result = Analysis.analysis(FileNumber)

    #�����CSV
    writer.writerow(result)

    i += 1

csvfile.close()
