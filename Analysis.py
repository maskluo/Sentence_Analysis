#coding=gbk




def analysis(source_file):
    FileInSentence = []
    PhrasesInSentence = []
    StatisticsOfPhrases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #ָ��·��
    #TXTFile = open('..\Data\Test'+'7'+'.txt','r')
    TXTFile = open(source_file, 'r')
    #��ȡ�ļ�
    TXT = unicode(TXTFile.read(), 'gbk')
    TXTFile.close()

    #�滻
    temp = TXT.replace(':', '|')#ò�����û��
    temp = TXT.replace('!', '|')
    temp = TXT.replace('?', '|')
    temp = TXT.replace(unicode('��', 'gbk'), '|')
    temp = TXT.replace(unicode('��', 'gbk'), '')
    temp = TXT.replace(unicode('��', 'gbk'), '|')
    temp = TXT.replace(unicode('��', 'gbk'), '|')
    temp = TXT.replace(unicode('��', 'gbk'), '|')
    #temp = TXT.replace(unicode('��', 'gbk'), unicode('��', 'gbk'))#ò�Ƽ����������ᱨ��Ī��
    #temp = TXT.replace(unicode(';', 'gbk'), unicode('��', 'gbk'))

    #�־���
    FileInSentence = temp.split('|')

    #��Ծ��Ӵ����ҳ�ÿ�����Ӹ��ж��ٸ������
    i = 0
    while i < len(FileInSentence):
        temp = FileInSentence[i].split(unicode('��', 'gbk'))
        PhrasesInSentence.append(len(temp))
        i += 1

    #ͳ�Ƹ�����γ���һ�������˶��ٴ�
    for element in PhrasesInSentence:
        StatisticsOfPhrases[element] += 1
    StatisticsOfPhrases[0] = len(PhrasesInSentence)
    print(StatisticsOfPhrases)

    return StatisticsOfPhrases
