#coding=gbk




def analysis(source_file):
    FileInSentence = []
    PhrasesInSentence = []
    StatisticsOfPhrases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #指定路径
    #TXTFile = open('..\Data\Test'+'7'+'.txt','r')
    TXTFile = open(source_file, 'r')
    #读取文件
    TXT = unicode(TXTFile.read(), 'gbk')
    TXTFile.close()

    #替换
    temp = TXT.replace(':', '|')#貌似这个没用
    temp = TXT.replace('!', '|')
    temp = TXT.replace('?', '|')
    temp = TXT.replace(unicode('：', 'gbk'), '|')
    temp = TXT.replace(unicode('　', 'gbk'), '')
    temp = TXT.replace(unicode('！', 'gbk'), '|')
    temp = TXT.replace(unicode('？', 'gbk'), '|')
    temp = TXT.replace(unicode('。', 'gbk'), '|')
    #temp = TXT.replace(unicode('；', 'gbk'), unicode('，', 'gbk'))#貌似加了这两个会报错，莫名
    #temp = TXT.replace(unicode(';', 'gbk'), unicode('，', 'gbk'))

    #分句子
    FileInSentence = temp.split('|')

    #针对句子处理，找出每个句子各有多少个句读段
    i = 0
    while i < len(FileInSentence):
        temp = FileInSentence[i].split(unicode('，', 'gbk'))
        PhrasesInSentence.append(len(temp))
        i += 1

    #统计各句读段长度一共出现了多少次
    for element in PhrasesInSentence:
        StatisticsOfPhrases[element] += 1
    StatisticsOfPhrases[0] = len(PhrasesInSentence)
    print(StatisticsOfPhrases)

    return StatisticsOfPhrases
