#coding:gbk
"""
Ŀ��:
����:������
"""

import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}            # �����ֵ�
relationships = {}    # ��ϵ�ֵ�
lineNames = []        # ÿ���������ϵ

jieba.load_userdict("dict.txt")        # �����ֵ�
with codecs.open("���������Ľֵ�.txt", "r", "gbk") as f:
    for line in f.readlines():
        poss = pseg.cut(line)        # �ִʲ����ظôʴ���
        lineNames.append([])        # Ϊ�¶����һ��������������б�
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue            # ���ִʳ���С��2��ôʴ��Բ�Ϊnrʱ��Ϊ�ôʲ�Ϊ����
            lineNames[-1].append(w.word)        # Ϊ��ǰ�εĻ�������һ������
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1                    # ��������ִ����� 1

for name, times in names.items():
    print(name, times)

for line in lineNames:                    # ����ÿһ��
    for name1 in line:                    
        for name2 in line:                # ÿ���е�����������
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:        # ��������δͬʱ�������½���
                relationships[name1][name2]= 1
            else:
                relationships[name1][name2]=relationships[name1][name2]+1

with codecs.open("node.txt","w","gbk") as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("edge.txt", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v +" "+str(w)+"\r\n")
