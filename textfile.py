# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *

textfile1 = open("n.txt",'r',encoding='utf-8')
text1 = textfile1.readlines()
textfile2 = open("g.txt",'r',encoding='utf-8')
text2 = textfile2.readlines()

i = 0
file = open("datafile.txt","w")
file.close()
file = open("datafile.txt","a")

tagger = POSTagger(model='resources/postagger.model')

for j,k in zip(text1,text2):

    tag = tagger.tag(word_tokenize(j))
    first_tag = tag[0][1]
    last_tag = tag[-1][1]
    print(last_tag)
    i+=1
    if 'عشق' in word_tokenize(j):
        esgh = 1
    else:
        esgh = 0
    if 'جان' in word_tokenize(j):
        jan = 1
    else:
        jan = 0
    if 'من' in word_tokenize(j):
        man = 1
    else:
        man = 0
    if 'تو' in word_tokenize(j):
        to = 1
    else:
        to = 0

    features = str(i)+' '+ "nimaei" + ' ' + "f1" + ' ' + word_tokenize(j)[0]+ ' ' + "f2" + ' '+ str(esgh)+ ' ' + "f3" + ' '+ str(jan)+ ' ' + "f4" + ' '+ str(man)+ ' ' + "f5" + ' '+ str(to)

    file.write(features)
    file.write('\n')


    tag = tagger.tag(word_tokenize(k))
    first_tag = tag[0][1]
    last_tag = tag[-1][1]
    i+=1
    if 'عشق' in word_tokenize(k):
        esgh = 1
    else:
        esgh = 0
    if 'جان' in word_tokenize(k):
        jan = 1
    else:
        jan = 0
    if 'من' in word_tokenize(k):
        man = 1
    else:
        man = 0
    if 'تو' in word_tokenize(k):
        to = 1
    else:
        to = 0

    features = str(i)+' '+ "ghazal" + ' ' + "f1" + ' ' + word_tokenize(k)[0]+ ' ' + "f2" + ' '+ str(esgh)+ ' ' + "f3" + ' '+ str(jan)+ ' ' + "f4" + ' '+ str(man)+ ' ' + "f5" + ' '+ str(to)

    file.write(features)
    file.write('\n')


file.close
