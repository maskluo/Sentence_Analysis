#coding=gbk
import math
import csv

def analysis(number):
    #������ʼ��
    CorpusInSentence = []
    PhrasesInSentence = []
    SentenceConclusion = []
    PhraseCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #����ͳ�Ƶ����·��
    csvfile = file('..\Result\SentenceInTXT'+str(number)+'.csv', 'wb')
    writer = csv.writer(csvfile)

    #ָ���ļ�
    source = '..\Data\Test'+str(number)+'.txt'
    TXTFile = open(source, 'r')
    #��ȡ�ļ�
    TXT = unicode(TXTFile.read(), 'gbk')
    TXTFile.close()

    #�滻
    Corpus = TXT.replace(':', '|')#ò�����û��
    Corpus = Corpus.replace('!', '|')
    Corpus = Corpus.replace('?', '|')
    Corpus = Corpus.replace(unicode('��', 'gbk'), '|')
    Corpus = Corpus.replace(unicode('��', 'gbk'), '')
    Corpus = Corpus.replace(unicode('��', 'gbk'), '')
    Corpus = Corpus.replace(unicode('��', 'gbk'), '')
    Corpus = Corpus.replace(unicode('��', 'gbk'), '|')
    Corpus = Corpus.replace(unicode('��', 'gbk'), '|')
    Corpus = Corpus.replace(unicode('��', 'gbk'), '|')
    Corpus = Corpus.replace(unicode('����', 'gbk'), '|')
    #Corpus = TXT.replace(unicode('��', 'gbk'), unicode('��', 'gbk'))#ò�Ƽ����������ᱨ��Ī��
    #Corpus = TXT.replace(unicode(';', 'gbk'), unicode('��', 'gbk'))

    #�־���
    CorpusInSentence = Corpus.split('|')

    #�����ά����洢
    #�洢�����ӣ����зֱ�Ϊ�þ��Ӿ�����������þ��ܳ��ȣ������ƽ�����ȣ�����α�׼��
    SentenceSituation = [0 for col in range(4)]
    #�洢�����ж��������������;���εľ����ܳ��ȵ�ƽ��ֵ�����ֵ����Сֵ�������ƽ�����ȵ�ƽ��ֵ�����ֵ����Сֵ������α�׼���ƽ��ֵ�����ֵ
    ConclusionOfTxt = [[0 for col in range(4)] for row in range(30)]

    print(Corpus)
    #��Ծ��Ӵ����ҳ�ÿ�����Ӹ��ж��ٸ������
    i = 0
#    while i < len(CorpusInSentence):
    while i < 5:
        SentenceSituation = [0, 0, 0, 0]
        CorpusInPhrase = CorpusInSentence[i].split(unicode('��', 'gbk'))
        #PhrasesInSentence.append(len(CorpusInPhrase))
        #���������
        Length = len(CorpusInPhrase)
        #������ܳ��ȣ�ƽ��ֵ����׼��
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
        #���
        SentenceSituation = [Length, Sum, Mean, SDeviation]
        SentenceConclusion.append(SentenceSituation)
        writer.writerow(SentenceSituation)
        i += 1
    csvfile.close()

    # �洢�����ӣ����зֱ�Ϊ�þ��Ӿ�����������þ��ܳ��ȣ������ƽ�����ȣ�����α�׼��
    SentenceSituation = [0 for col in range(4)]
    # �洢�����о�����������Լ������;���εľ����ܳ��ȵ�ƽ��ֵ�����ֵ����Сֵ�������ƽ�����ȵ�ƽ��ֵ�����ֵ����Сֵ������α�׼���ƽ��ֵ�����ֵ����Сֵ
    ConclusionOfTxt = [[0 for col in range(10)] for row in range(30)]
    #ͳ�Ƹ�����γ���һ�������˶��ٴ�
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
