#coding=gbk

import Analysis
import csv

csvfile = file('..\Result\Result.csv', 'wb')
writer = csv.writer(csvfile)

i = 1
while i <= 9:
    #·��
    source = '..\Data\Test'+str(i)+'.txt'

    #����
    result = Analysis.analysis(source)

    #�����CSV
    writer.writerow(result)

    i += 1

csvfile.close()
