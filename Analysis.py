#coding=gbk
import math
import csv


def analysis(number):
    #变量初始化
    CorpusInSentence = []
    PhrasesInSentence = []
    SentenceConclusion = []
    Result = []
    PhraseCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
    ConclusionOfTxt = [[0 for col in range(10)] for row in range(30)]

    #针对句子处理，找出每个句子各有多少个句读段
    #单句统计的输出路径
    csvfile = file('..\Result\SentenceInTXT'+str(number)+'.csv', 'wb')
    writer = csv.writer(csvfile)
    i = 0
    while i < len(CorpusInSentence):
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

    #赋初值
    for element in ConclusionOfTxt:
        element[1] = 0
        element[2] = 0
        element[3] = 10
        element[4] = 0
        element[5] = 0
        element[6] = 10
        element[7] = 0
        element[8] = 0
        element[9] = 10
    #全篇分析
    for SentenceSituation in SentenceConclusion:
        #句读段总量
        ConclusionOfTxt[SentenceSituation[0]][0] += 1
        #总字数
        ConclusionOfTxt[SentenceSituation[0]][1] += SentenceSituation[1]
        #单句读段长度最大值
        if ConclusionOfTxt[SentenceSituation[0]][2] < SentenceSituation[1]:
            ConclusionOfTxt[SentenceSituation[0]][2] = SentenceSituation[1]
        #单句读段长度最小值
        if ConclusionOfTxt[SentenceSituation[0]][3] > SentenceSituation[1]:
            ConclusionOfTxt[SentenceSituation[0]][3] = SentenceSituation[1]
        #句读段平均长度总值
        ConclusionOfTxt[SentenceSituation[0]][4] += SentenceSituation[2]
        #平均长度最大值
        if ConclusionOfTxt[SentenceSituation[0]][5] < SentenceSituation[2]:
            ConclusionOfTxt[SentenceSituation[0]][5] = SentenceSituation[2]
        #平均长度最小值
        if ConclusionOfTxt[SentenceSituation[0]][6] > SentenceSituation[2]:
            ConclusionOfTxt[SentenceSituation[0]][6] = SentenceSituation[2]
        #标准差平均值总值
        ConclusionOfTxt[SentenceSituation[0]][7] += SentenceSituation[3]
        #标准差最大值
        if ConclusionOfTxt[SentenceSituation[0]][8] < SentenceSituation[3]:
            ConclusionOfTxt[SentenceSituation[0]][8] = SentenceSituation[3]
        #标准差最小值
        if ConclusionOfTxt[SentenceSituation[0]][9] > SentenceSituation[3]:
            ConclusionOfTxt[SentenceSituation[0]][9] = SentenceSituation[3]

    Sum = 0
    for element in ConclusionOfTxt:
        if element[0] == 0:
            element[3] = 0
            element[6] = 0
            element[9] = 0
        else:
            Sum += element[0]
            element[1] = element[1] * 1.0 / element[0]
            element[4] = element[4] * 1.0 / element[0]
            element[7] = element[7] * 1.0 / element[0]
    ConclusionOfTxt[0][0] = Sum

    #文章结论的输出路径
    csvfile = file('..\Result\Result' + str(number) + '.csv', 'wb')
    writer = csv.writer(csvfile)
    for element in ConclusionOfTxt:
        writer.writerow(element)
        Result.append(element[0])
    print(Result)
    return Result
