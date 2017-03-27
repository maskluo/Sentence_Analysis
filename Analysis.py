#coding=gbk
import math
import csv


def analysis(number):
    #������ʼ��
    CorpusInSentence = []
    PhrasesInSentence = []
    SentenceConclusion = []
    Result = []
    PhraseCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
    ConclusionOfTxt = [[0 for col in range(10)] for row in range(30)]

    #��Ծ��Ӵ����ҳ�ÿ�����Ӹ��ж��ٸ������
    #����ͳ�Ƶ����·��
    csvfile = file('..\Result\SentenceInTXT'+str(number)+'.csv', 'wb')
    writer = csv.writer(csvfile)
    i = 0
    while i < len(CorpusInSentence):
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

    #����ֵ
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
    #ȫƪ����
    for SentenceSituation in SentenceConclusion:
        #���������
        ConclusionOfTxt[SentenceSituation[0]][0] += 1
        #������
        ConclusionOfTxt[SentenceSituation[0]][1] += SentenceSituation[1]
        #������γ������ֵ
        if ConclusionOfTxt[SentenceSituation[0]][2] < SentenceSituation[1]:
            ConclusionOfTxt[SentenceSituation[0]][2] = SentenceSituation[1]
        #������γ�����Сֵ
        if ConclusionOfTxt[SentenceSituation[0]][3] > SentenceSituation[1]:
            ConclusionOfTxt[SentenceSituation[0]][3] = SentenceSituation[1]
        #�����ƽ��������ֵ
        ConclusionOfTxt[SentenceSituation[0]][4] += SentenceSituation[2]
        #ƽ���������ֵ
        if ConclusionOfTxt[SentenceSituation[0]][5] < SentenceSituation[2]:
            ConclusionOfTxt[SentenceSituation[0]][5] = SentenceSituation[2]
        #ƽ��������Сֵ
        if ConclusionOfTxt[SentenceSituation[0]][6] > SentenceSituation[2]:
            ConclusionOfTxt[SentenceSituation[0]][6] = SentenceSituation[2]
        #��׼��ƽ��ֵ��ֵ
        ConclusionOfTxt[SentenceSituation[0]][7] += SentenceSituation[3]
        #��׼�����ֵ
        if ConclusionOfTxt[SentenceSituation[0]][8] < SentenceSituation[3]:
            ConclusionOfTxt[SentenceSituation[0]][8] = SentenceSituation[3]
        #��׼����Сֵ
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

    #���½��۵����·��
    csvfile = file('..\Result\Result' + str(number) + '.csv', 'wb')
    writer = csv.writer(csvfile)
    for element in ConclusionOfTxt:
        writer.writerow(element)
        Result.append(element[0])
    print(Result)
    return Result
