from __future__ import print_function
import nltk
#import numpy
import re
import random
from nltk import CFG, grammar
from nltk.parse.generate import generate
from nltk.probability import DictionaryProbDist
import sys
lst=[["boys","girls","clasroom","Deveshi","390","perimeter","rectangle","difference"],
     ["men","women","seminarhall","Ram","350","area","square","product"],
["red balls","white balls","box","Myteacher","450","perimeter","parallelogram","sum"]]

lst2=[["50notes","20notes","length","breadth","first number","second number","boys","girls"],["50notes","20notes","length","breadth","first number","second number","men","women"],
["50notes","20notes","length","breadth","first number","second number","red balls","white balls"]]



gramstring="""S -> S1[VAL=?n]
S1[VAL='money'] -> NN[VAL='money'] HS[VAL='money'] A[VAL='money'] TT[VAL='money'] PP CD IN DEN[VAL='money'] PP C1[VAL='money'] C2[VAL='money'] C3[VAL='money']
S1[VAL='shape'] -> DET PR[VAL='shape'] PP A SHP[VAL='shape'] VBZ CD
S1[VAL='int'] -> DET DIFF[VAL='int'] PP NUMS VBZ CD
S1[VAL='age'] -> DET AGS[VAL='age'] PP N1[VAL='age'] AND N2[VAL='age'] R IN DET RAT CDR
S1[VAL='class'] -> DET NUM PP BYS[VAL='class'] AND GRS[VAL='class'] IN CSS[VAL='class'] R IN RAT CDR
NN[VAL='money'] -> 'Deveshi'
HS[VAL='money'] -> 'has'
A -> 'a'

TT[VAL='money'] ->'total'
PP -> 'of'

CD -> '590'

IN -> 'in'

DEN[VAL='money'] -> 'denominations'
C1[VAL='money'] -> '50'
C2[VAL='money'] -> '20'
C3[VAL='money'] -> '10'
DET -> 'the'

PR[VAL='shape'] -> 'perimeter'
SHP[VAL='shape'] -> 'rectangle'
VBZ -> 'is'

DIFF[VAL='int'] -> 'difference'
NUM -> 'number'
NUMS -> '2 numbers'
AGS[VAL='age'] -> 'ages'
N1[VAL='age'] -> 'Rahul'
N2[VAL='age'] -> 'Haroon'
R -> 'are'

RAT -> 'ratio'

CDR -> '5:7'
BYS[VAL='class'] -> 'boys'
AND -> 'and'
GRS[VAL='class'] ->'girls'
CSS[VAL='class'] -> 'clasroom'
"""

g2="""
S -> S1[VAL=?n]
S1[VAL='money'] -> DET RAT PP OBJ1[VAL='money'] AND OBJ2[VAL='money'] VBZ CDR
S1[VAL='shape'] -> DET RAT PP OBJ1[VAL='shape'] AND OBJ2[VAL='shape'] VBZ CDR
S1[VAL='int'] -> DET RAT PP OBJ1[VAL='int'] AND OBJ2[VAL='int'] VBZ CDR
S1[VAL='age'] -> NUM[VAL='age'] YR[VAL='age'] LAT[VAL='age'] SUM[VAL='age'] PP TH[VAL='age'] AGS[VAL='age'] VB[VAL='age'] BE[VAL='age'] CD[VAL='age']
S1[VAL='class'] -> NU PP BYS[VAL='class'] VBZ CDN[VAL='class'] MOR[VAL='class'] THAN[VAL='class'] NU PP GRS[VAL='class']
DET -> 'The'
RAT -> 'ratio'
PP -> 'of'
OBJ1[VAL='money'] -> '50notes'
OBJ1[VAL='shape'] -> 'length'
OBJ1[VAL='int'] -> 'first number'
OBJ2[VAL ='money'] -> '20notes'
OBJ2[VAL='shape'] -> 'breadth'
OBJ2[VAL='int'] -> 'second number'
AND -> 'and'
VBZ -> 'is'
CDR -> '3:5'
NUM[VAL='age'] -> 'Four'
YR[VAL='age'] -> 'years'
LAT[VAL='age'] -> 'later'
SUM[VAL='age'] -> 'sum'
TH[VAL='age'] -> 'their'
AGS[VAL='age'] -> 'ages'
VB[VAL='age'] -> 'will'
BE[VAL='age'] -> 'be'
CD[VAL='age'] -> '56'
NU -> 'Number'
BYS[VAL='class'] -> 'boys'
CDN[VAL='class'] -> '8'
MOR[VAL='class'] -> 'more'
THAN[VAL='class'] -> 'than'
GRS[VAL='class'] -> 'girls'
"""
g3 = """
S -> S1[G=?n] 
S1[G='money'] -> 'How many notes of each denomination person has?'
S1[G='shape'] -> 'What are its length and breadth?'
S1[G='int'] -> 'What are the two numbers?'
S1[G='age'] -> 'What are their present ages?'
S1[G='class'] -> 'What is the total strength?'

"""
first=[]
sec=[]
third=[]

grammar1 = nltk.grammar.FeatureGrammar.fromstring("""% start S"""+"\n"+gramstring)
parser1 = nltk.FeatureChartParser(grammar1)
for sentence1 in generate(grammar1):
    if(parser1.parse_one(sentence1)): 
        string1=' '.join(sentence1)
        first.append(string1)
    #print(l)


grammar2 = nltk.grammar.FeatureGrammar.fromstring("""% start S"""+"\n"+g2)
parser2 = nltk.FeatureChartParser(grammar2)
for sentence2 in generate(grammar2):
    if(parser2.parse_one(sentence2)): 
        string2=' '.join(sentence2)
        if string2 not in sec:
            sec.append(string2)
        else:
            pass

grammar3 = nltk.grammar.FeatureGrammar.fromstring("""% start S"""+"\n"+g3)
parser3 = nltk.FeatureChartParser(grammar3)
for sentence3 in generate(grammar3):
    if(parser3.parse_one(sentence3)): 
        string3=' '.join(sentence3)
        if string3 not in third:
            third.append(string3)
        else:
            pass
for m,n,p in zip(first,sec,third):
    print(m)
    print(n)
    print(p)
    print("\n")
j=0
k=0
while(j+1<3):
    l=[]
    b=[]
    n=[]
    for item1,item2 in zip(lst[j],lst[j+1]):
        gramstring=gramstring.replace(item1,item2)
    grammar1 = nltk.grammar.FeatureGrammar.fromstring("""% start S"""+"\n"+gramstring)
    parser1 = nltk.FeatureChartParser(grammar1)
    for sentence1 in generate(grammar1):
        if(parser1.parse_one(sentence1)): 
            string1=' '.join(sentence1)
            l.append(string1)
    #print(l)
    for item1,item2 in zip(lst2[j],lst2[j+1]):
        g2=g2.replace(item1,item2)
    grammar2 = nltk.grammar.FeatureGrammar.fromstring("""% start S"""+"\n"+g2)
    parser2 = nltk.FeatureChartParser(grammar2)
    for sentence2 in generate(grammar2):
        if(parser2.parse_one(sentence2)): 
            string2=' '.join(sentence2)
            if string2 not in b:
                b.append(string2)
            else:
                pass
    
    grammar3 = nltk.grammar.FeatureGrammar.fromstring("""% start S"""+"\n"+g3)
    parser3 = nltk.FeatureChartParser(grammar3)
    for sentence3 in generate(grammar3):
        if(parser3.parse_one(sentence3)): 
            string3=' '.join(sentence3)
            n.append(string3)
##            if string3 not in n:
##                n.append(string3)
##            else:
##                pass
##    #print(b)
    for i,p,o in zip(l,b,n):
        print(i)
        print(p)
        print(o)
        print("\n")
            
            

    j+=1

        
    
