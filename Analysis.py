#coding=gbk
import math
import csv

def analysis(number):
    #变量初始化
    CorpusInSentence = []
    PhrasesInSentence = []
    SentenceConclusion = []
    PhraseCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #单句统计的输出路径
    csvfile = file('..\Result\SentenceInTXT'+str(number)+'.csv', 'wb')
    writer = csv.writer(csvfile)

    #指定文件
    source = '..\Data\Test'+str(number)+'.txt'
    TXTFile = open(source, 'r')
    #读取文件
    TXT = unicode(TXTFile.read(), 'gbk')
    TXTFile.close()

    #替换
    Corpus = TXT.replace(':', '|')#貌似这个没用
    Corpus = Corpus.replace('!', '|')
    Corpus = Corpus.replace('?', '|')
    Corpus = Corpus.replace(unicode('：', 'gbk'), '|')
    Corpus = Corpus.replace(unicode('　', 'gbk'), '')
    Corpus = Corpus.replace(unicode('“', 'gbk'), '')
    Corpus = Corpus.replace(unicode('”', 'gbk'), '')
    Corpus = Corpus.replace(unicode('！', 'gbk'), '|')
    Corpus = Corpus.replace(unicode('？', 'gbk'), '|')
    Corpus = Corpus.replace(unicode('。', 'gbk'), '|')
    Corpus = Corpus.replace(unicode('……', 'gbk'), '|')
    #Corpus = TXT.replace(unicode('；', 'gbk'), unicode('，', 'gbk'))#貌似加了这两个会报错，莫名
    #Corpus = TXT.replace(unicode(';', 'gbk'), unicode('，', 'gbk'))

    #分句子
    CorpusInSentence = Corpus.split('|')

    #定义二维数组存储
    #存储各句子，各列分别为该句子句读段数量，该句总长度，句读段平均长度，句读段标准差
    SentenceSituation = [0 for col in range(4)]
    #存储文章中读段数量，该类型句读段的句子总长度的平均值，最大值，最小值，句读段平均长度的平均值，最大值，最小值，句读段标准差的平均值，最大值
    ConclusionOfTxt = [[0 for col in range(4)] for row in range(30)]

    print(Corpus)
    #针对句子处理，找出每个句子各有多少个句读段
    i = 0
#    while i < len(CorpusInSentence):
    while i < 5:
        SentenceSituation = [0, 0, 0, 0]
        CorpusInPhrase = CorpusInSentence[i].split(unicode('，', 'gbk'))
        #PhrasesInSentence.append(len(CorpusInPhrase))
        #句读段数量
        Length = len(CorpusInPhrase)
        #句读段总长度，平均值，标准差
        Sum = 0
        if Length > 1:
            for element in CorpusInPhrase:
                Sum += len(element)
            Mean = Sum / Length
            Variance = 0
            for element in CorpusInPhrase:
                Variance += math.pow((len(element)-Mean), 2)
            SDeviation = math.sqrt(Variance / Length)
        else:
            Sum = len(CorpusInPhrase[0])
            Mean = Sum
            SDeviation = 0
        #输出
        SentenceSituation = [Length, Sum, Mean, SDeviation]
        SentenceConclusion.append(SentenceSituation)
        writer.writerow(SentenceSituation)
        i += 1
    csvfile.close()

    # 存储各句子，各列分别为该句子句读段数量，该句总长度，句读段平均长度，句读段标准差
    SentenceSituation = [0 for col in range(4)]
    # 存储文章中句读段数量，以及该类型句读段的句子总长度的平均值，最大值，最小值，句读段平均长度的平均值，最大值，最小值，句读段标准差的平均值，最大值，最小值
    ConclusionOfTxt = [[0 for col in range(10)] for row in range(30)]
    #统计各句读段长度一共出现了多少次
    SumSum = 0
    SumMax = 0
    SumMin = 10
    MeanSum = 0
    MeanMax = 0
    MeanMin = 10
    SDSum = 0
    SDMax = 0
    SDMin = 10
    for SentenceSituation in SentenceConclusion:
        ConclusionOfTxt[SentenceSituation[0]][0] += 1
        '''
        SumSum += SentenceSituation[1]
        if SumMax < SentenceSituation[1]:
            SumMax = SentenceSituation[1]
        if SumMin > SentenceSituation[1]:
            SumMin = SentenceSituation[1]
        MeanSum += SentenceSituation[2]
        if MeanMax < SentenceSituation[2]:
            MeanMax = SentenceSituation[2]
        if MeanMin > SentenceSituation[2]:
            MeanMin = SentenceSituation[2]
        SDSum += SentenceSituation[3]
        if SDMax < SentenceSituation[3]:
            SDMax = SentenceSituation[3]
        if SDMin > SentenceSituation[3]:
            SDMin = SentenceSituation[3]
'''
    print (SentenceConclusion)
    print (ConclusionOfTxt)





    for element in PhrasesInSentence:
        PhraseCount[element] += 1
    PhraseCount[0] = len(PhrasesInSentence)
    print(PhraseCount)

    return PhraseCount
