import Analysis

i = 1
while i <= 4:
    #路径
    source = '..\Data\Test'+str(i)+'.txt'

    #处理
    result = Analysis.analysis(source)

    #文件输出
    Destination = '..\Result\Result'+str(i)+'.txt'
    File = open(Destination, 'r')
    for num in result:
        File.write(str(result) + '\n')
    File.close()

    i += 1

