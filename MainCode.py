import nltk
import numpy
import re
from nltk import CFG
from nltk.parse.generate import generate

# Create grammars for the variations

g1="""
S -> NP VP
NP -> DT NNP P AR JJ N 
VP -> V CN
NNP -> 'perimeter' | 'area'
V -> 'is'
CN -> '134'|'234'
DT -> 'The'|'the'
N -> 'swimmingpool'|'field'|'garden'
P -> 'of'
AR -> 'a'|'the'|'an'
JJ -> 'rectangular'
"""
g2="""
 S -> NP VP
 NP -> PP NN
 PP -> 'Its'
 NN -> 'length' | 'breadth' 
 VP -> V CN M JJM T PP NN
 M -> 'm' | 'cm' | 'km' 
 JJM -> 'more than' | 'less than'
 T -> 'twice' | 'thrice'
 CN -> '2'|'3'
 V -> 'is'
"""
g3="""
S -> NP VP
NP -> DT NNP P AR JJ 
VP -> V CN
NNP -> 'sum' | 'difference'
V -> 'is'
CN -> '95' | '56' | '98' | '100'
DT -> 'The'|'the'
P -> 'of'
AR -> 'two'
JJ -> 'numbers'
"""
g4="""
 S -> NP VP
 NP -> PP NN
 PP -> 'If'
 NN -> 'one' 
 VP -> V CN JJM 
 JJM -> 'more than the other' | 'less than the other'
 CN -> '2' | '3' | '15' | '5'
 V -> 'is'
"""
g5="""
 S -> VP CN NP
 VP -> PP PR VB CD NN
 PP -> 'If' | 'Consider if'
 PR -> 'you' | 'I' | 'we'
 VB -> 'add' | 'multiply' | 'subtract'
 CD -> '1/2' | '2/3' | '3/4'
 NN -> 'from a number'
 CN -> 'and'
 NP -> VB DT WR PB CD PS CD
 DT -> 'the'
 WR -> 'result' | 'answer' | 'number'
 PB -> 'by'
 PS -> 'the number is'
"""

g6="""
S -> NP VP
NP -> DT NNP P AR JJ N 
VP -> V CN
NNP -> 'base'
V -> 'is'
CN -> '3/4' | '2/5' | '1/4'
DT -> 'The'|'the'
N -> 'triangle'
P -> 'of'
AR -> 'a'|'the'
JJ -> 'isosceles' | 'scalene' | 'equilateral'
"""
g7="""
S -> NP VP
NP -> DT NNP P AR N 
VP -> V CN
NNP -> 'perimeter' | 'area'
V -> 'is'
CN -> '5/7'|'1/3'
DT -> 'The'|'the'
N -> 'triangle'
P -> 'of'
AR -> 'a'|'the'

"""
g8="""
S -> NP VP
NP -> DT NNP P AR JJ 
VP -> V CN
NNP -> 'ratio'
V -> 'is'
CN -> '4:5' | '2:6' | '5:6' | '7:9'
DT -> 'The'|'the'
P -> 'of'
AR -> 'two'
JJ -> 'numbers'
"""
g9="""
 S -> NP VP
 NP -> PP NN
 PP -> 'If'
 NN -> 'they' 
 VP -> JJM CN
 JJM -> 'differ by' 
 CN -> '2' | '3' | '15' | '5' | '18'
 
"""
g10="""
S -> NP VP
NP -> DT NN PP CD N INT
VP -> V CN
V -> 'is'
CN -> '51' | '34' | '56' | '45'
DT -> 'the'
NN -> 'product' | 'sum' | 'difference'
PP -> 'of'
CD -> 'three' | 'four' | 'five'
N -> 'consecutive'
INT -> 'integers' | 'multiples of 8'
"""
g11="""
S -> NP VP
NP -> DT NN PP CD N INT D
D -> 'when they are taken in' | I A M
A -> 'and'
M -> 'multiplied by' | C R
C -> '2,3,4' | '3,4,5' | '5,6,7'
R -> 'respectively'
I -> 'increasing order' | 'decreasing order' 
VP -> V CN
V -> 'is'
CN -> '51' | '34' | '56' | '45'
DT -> 'the'
NN -> 'product' | 'sum' | 'difference'
PP -> 'of'
CD -> 'three' | 'four' | 'five'
N -> 'consecutive'
INT -> 'numbers'
"""

g12="""
S -> NP VP
NP -> R L
R ->'The number of boys and girls in a class are'|'The length of sides'
L ->M N
M -> 'in a'
N -> 'class'|'rectangle'
VP -> B A.
B -> 'in the ratio'
A -> P : Q
P -> '3'|'4'|'5'|'6'|'7'|'8'|'1'|'2'|'12'|'15'|'9'
Q -> '2'|'5'|'7'|'9'|'11'|'13'|'17'
"""
g13="""
S -> NP VP
NP -> 'The number of boys is'|'The length of one side is'
VP -> A B
B -> C D
D -> 'than the number of girls' | 'than the other side.'
A -> '1'|'2'|'3'|'4'|'5'|'6'
C -> 'more'|'less'
"""
g14="""
S -> NP VP
NP -> A B 
VP -> C D
A -> 'Sum'|'Difference'
B -> 'of the digits of a two-digit number is'
C -> '9'|'10'|'15'|'18'|'5'|'6'|'7'|'3'|'4'|'8'|'11'|'12'|'13'|'14'|'17'|'16'
D -> '.'
"""
g15="""
S -> NP VP
NP -> 'When we interchange the digits,it is found that resulting new number is'
VP -> A B C D
A -> 'greater'|'smaller'|'larger'
B -> 'than the original number by'
C -> '27'|'30'|'15'|'20'|'26'|'36'|'45'|'20'|'30'|'22'
D -> '.'
"""


g16="""
S -> NP VP
NP -> A B 
VP -> C F D E
A -> 'Nisha'  
B -> 'present age is'
C -> 'three'|'four'|'five'|'six'|'seven'|'eight'|'nine'|'two'
F -> 'times'
D -> 'Nisha mother'
E -> 'present age.'
"""
g17="""
S -> NP VP
NP -> A B 
VP -> C D E F A G
A -> 'Nisha'
B -> 'age'
C -> 'three'|'four'|'five'|'six'|'seven'|'eight'|'nine'|'two'
D -> 'years from now will be'
E -> 'one third'|'one fourth'|'on fifth'
F -> 'of'
G -> 'present age.'
"""

g18="""
 S -> NP VP
 NP -> N JJ AG
 VP -> V CD AD N JJ AG
 V -> 'is'
 CD -> '6' | '5' | '4' | '7'
 AD -> 'times'
 N -> 'Shobo' | 'Shobo mother'
 JJ -> 'present'
 AG -> 'age'
"""

g19="""
 S -> NP VP
 NP -> N AG TM
 VP -> V HCD PP N JJ AG
 JJ -> 'present'
 N -> 'Shobo' | 'Shobo mother'
 AG -> 'age'
 TM -> 'five years from now' | 'ten years from now' | 'six years from now'
 V -> 'will be'
 HCD -> 'one third' | 'half' | 'quarter' | 'one sixth'
 
"""

g20="""
 S -> NP VP
 NP -> NM 
 VP -> V CD YR JJ TH NM
 V -> 'is'
 CD -> '25' | '26' | '30' | '29'
 YR -> 'years'
 JJ -> 'older' | 'younger'
 TH -> 'than'
 NM -> 'Baichung grandfather' | 'Baichung father' | 'Baichung'
 
"""
g21="""
 S -> NP VP
 NP -> NM 
 VP -> V CD YR JJ TH NM
 V -> 'is'
 CD -> '26' | '23' | '34' |'35'
 YR -> 'years'
 JJ -> 'younger' | 'older'
 TH -> 'than'
 NM -> 'Baichung' | 'Baichung grandfather' | 'Baichung father'
 
"""


# cutDownsent() splits the question into sentences and later tokenizes each sentences to words
# so that POS tagging can be done on them.
# Return a list of words along with their POS(Parts of speech)

ls=[]
def cutDownsent(s):
    words=[]
    pos=[]
    words.append(nltk.word_tokenize(s))
    for word in words:
        pos.append(nltk.pos_tag(word))
    return pos



# Filtering the sentences to remove the sentences which aren't semanticaly right.

d={}
def filter(sent):
    d={}
    # Tokenize each sentence to get POS
    s=cutDownsent(sent)

    # for each tuple in a list,it will have (Object,POS)
    for item in s[0]:
        lst1=[item[0]]
        lst2=[item[1]]
        #To filter,put the Object into a dictionary as key and its POS as value
        for i,j in zip(lst1,lst2):
            if i not in d.keys():
                d[i]=[j]
            else:
                d[i].append(j)
    # If the object is repeated more than once,and it is a Noun,then remove such sentences.Eg:(length is more than length...)
    for itemV in d.values():
       if 'NN' in itemV and len(itemV)>=2:
            flag=False
            break
       else:
            flag=True
    if(flag == False):
        return None
    else:
        return sent


# Dealing with age problems,careful analysis must be done to filter the illogical statements.
# Store the objects which relate to age in a list.
def ageFilter(sent):
    lst=["mother","father","grandfather","grandmother"]
    # There are a few problems with keywords.So,accordingly handle these cases
    if "times" in sent:
        # Split the whole sentence and store the words in a list to check later for the repetitions.
        listChange=sent.split(" ")
        # split the sentence at that keyword,look for the words on its left(lhs),look for the words on its right(rhs) and handle the cases.
        rhs=sent.split("times",1)[1]
        lhs=sent.split("times",1)[0]
        # mother should not be repeated,similarly father and etc.Eg: Shobo's mother age is 6 times Shobo's mother age.
        if("mother" in lhs and "mother" not in rhs)or("father" in lhs and "father" not in rhs)or("grandfather" in lhs and "grandfather" not in rhs )or("grandmother" in lhs and "grandmother" not in rhs):
            return sent
        elif("mother" not in sent and "father" not in sent and "grandmother" not in sent and "grandfather" not in sent):
            #Handle the cases with repeated objects.Eg: Shobo's age is 6 times Shobo's age.
            for i in listChange:
                if listChange.count(i)>1:
                    return None
        
            
           
                    

    elif "one third" in sent:
        listChange=sent.split(" ")
        rhs=sent.split("one third",1)[1]
        lhs=sent.split("one third",1)[0]
        # Similarly,handle the cases where object's age can be always less than his/her mother's age,father's age,etc.
        if("mother" not in lhs and "mother" in rhs) or ("father" not in lhs and "father" in rhs)or ("grandfather" not in lhs and "grandfather" in rhs)or ("grandmother"  not in lhs and "grandmother" in rhs):
            return sent
        elif("mother" not in sent and "father" not in sent and "grandmother" not in sent and "grandfather" not in sent):
            for i in listChange:
                if listChange.count(i)>1:
                    return None
        
    elif  "half" in sent:
        listChange=sent.split(" ")
        rhs=sent.split("half",1)[1]
        lhs=sent.split("half",1)[0]
        if("mother" not in lhs and "mother" in rhs) or ("father" not in lhs and "father" in rhs)or ("grandfather" not in lhs and "grandfather" in rhs)or ("grandmother"  not in lhs and "grandmother" in rhs):
            return sent
        elif("mother" not in sent and "father" not in sent and "grandmother" not in sent and "grandfather" not in sent):
            for i in listChange:
                if listChange.count(i)>1:
                    return None
        
    
    elif "quarter" in sent:
        listChange=sent.split(" ")
        rhs=sent.split("quarter",1)[1]
        lhs=sent.split("quarter",1)[0]
        if("mother" not in lhs and "mother" in rhs) or ("father" not in lhs and "father" in rhs)or ("grandfather" not in lhs and "grandfather" in rhs)or ("grandmother"  not in lhs and "grandmother" in rhs):
            return sent
        elif("mother" not in sent and "father" not in sent and "grandmother" not in sent and "grandfather" not in sent):
            for i in listChange:
                if listChange.count(i)>1:
                    return None
        
    elif "one sixth" in sent:
        listChange=sent.split(" ")
        rhs=sent.split("one sixth",1)[1]
        lhs=sent.split("one sixth",1)[0]
        if("mother" not in lhs and "mother" in rhs) or ("father" not in lhs and "father" in rhs)or ("grandfather" not in lhs and "grandfather" in rhs)or ("grandmother"  not in lhs and "grandmother" in rhs):
            return sent
        elif("mother" not in sent and "father" not in sent and "grandmother" not in sent and "grandfather" not in sent):
            for i in listChange:
                if listChange.count(i)>1:
                    return None
        
    elif "younger" in sent:
        listChange=sent.split(" ")
        rhs=sent.split("younger",1)[1]
        lhs=sent.split("younger",1)[0]
        # the order of objects in this problem should be restricted to only few like, Eg: Baichung's grandfather is older than Baichung.
        # Baichung's father is younger than Baichung's grandfather...etc.
        if("grandfather" in lhs and "grandfather" in rhs):
            return None
        elif("mother" in lhs and "grandmother" in rhs)or( "father" in lhs and "grandfather" in rhs):
            return sent
##                for i in listChange:
##                    if i in lst and listChange.count(i)>1:
##                        return None
##                    else:

       
        
        elif("mother" not in sent and "father" not in sent and "grandmother" not in sent and "grandfather" not in sent):
            for i in listChange:
                if listChange.count(i)>1:
                    return None
        else:
            return None
        
            
    # Similar to the younger conditions,but reverse.   
    elif "older" in sent:
        listChange=sent.split(" ")
        rhs=sent.split("older",1)[1]
        lhs=sent.split("older",1)[0]
        if("grandfather" in lhs and "grandfather" in rhs):
            return None
        
        elif("mother" in lhs and "mother" not in rhs) or ("father" in lhs and "father" not in rhs) or ("grandfather" in lhs and "grandfather" not in rhs) or ("grandmother" in lhs and "grandmother" not in rhs) or("grandfather" in lhs and "father" in rhs):
##                for i in listChange:
##                    if i in lst and listChange.count(i)>1:
##                        return None
##                    else:
            return sent
        

        elif("mother" not in sent and "father" not in sent and "grandmother" not in sent and "grandfather" not in sent):
            for i in listChange:
                if listChange.count(i)>1:
                    return None
        else:
            return None
        
        
            
        
        
   
        
        
        
# Filter each sentence and return them all.
def eliminate(sentence):
    sents=nltk.sent_tokenize(sentence)
    for sent in sents:
        str=filter(sent)
        return str

#Here input is the chosen option on UI.
#Given IDs to each question as per NCERT Book,input will be given that chosen value.
input=26
# Generate variations of a particular question based on the input and its corresponding grammar.
if input==2:
    g=CFG.fromstring(g1)
    g2=CFG.fromstring(g2)
    rd_parser=nltk.RecursiveDescentParser(g)
    for sent,sent2 in zip(generate(g2,n=100),generate(g,n=100)):
        newsent1=' '.join(sent)
        newsent2=' '.join(sent2)
        ans1=eliminate(newsent1)
        ans2=eliminate(newsent2)
        if(ans1 == None or ans2 == None):
            pass
        else:
            print(ans1)
            print(ans2)
            print("Determine the length and breadth")
            print("\n")
elif input==4:
    g=CFG.fromstring(g3)
    g2=CFG.fromstring(g4)
    rd_parser=nltk.RecursiveDescentParser(g)
    for sent,sent2 in zip(generate(g2,n=100),generate(g,n=100)):
        newsent1=' '.join(sent)
        newsent2=' '.join(sent2)
        ans1=eliminate(newsent1)
        ans2=eliminate(newsent2)
        if(ans1 == None or ans2 == None):
            pass
        else:
            print(ans1)
            print(ans2)
            print("Find the numbers.")
            print("\n")
elif input==1:
    g2=CFG.fromstring(g5)
    for sent in generate(g2,n=200):
        newsent1=' '.join(sent)
        print(newsent1)
        print("What is the number?")
        print("\n")
elif input==3:
    g=CFG.fromstring(g6)
    g2=CFG.fromstring(g7)
    for sent,sent2 in zip(generate(g2,n=100),generate(g,n=100)):
        newsent1=' '.join(sent)
        newsent2=' '.join(sent2)
        ans1=eliminate(newsent1)
        ans2=eliminate(newsent2)
        if(ans1 == None or ans2 == None):
            pass
        else:
            print(ans1)
            print(ans2)
            print("What are the other length of its other sides?")
            print("\n")
elif input==5:
    g=CFG.fromstring(g9)
    g2=CFG.fromstring(g8)
    for sent,sent2 in zip(generate(g2,n=100),generate(g,n=100)):
        newsent1=' '.join(sent)
        newsent2=' '.join(sent2)
        print(newsent1)
        print(newsent2)
        print("Find the numbers.")
        print("\n")
elif input==6:
    g=CFG.fromstring(g10)
    for sent in generate(g,n=100):
        newsent1=' '.join(sent)
        print(newsent1)
        print("What are these numbers?")
        print("\n")
elif input==8:
    g=CFG.fromstring(g11)
    for sent in generate(g,n=100):
        newsent1=' '.join(sent)
        ans1=eliminate(newsent1)
        if(ans1 == None):
            pass
        else:
            print(ans1)
            print("What are these numbers?")
            print("\n")
elif input==9:
    g=CFG.fromstring(g12)
    g2=CFG.fromstring(g13)
    for sent,sent2 in zip(generate(g2,n=100),generate(g,n=100)):
        newsent1=' '.join(sent)
        newsent2=' '.join(sent2)
        ans1=eliminate(newsent1)
        ans2=eliminate(newsent2)
        if(ans1 == None or ans2 == None):
            pass
        else:
            print(ans1)
            print(ans2)
            print("Determine the length and breadth")
            print("\n")

elif input==23:
    g=CFG.fromstring(g15)
    g2=CFG.fromstring(g14)
    for sent,sent2 in zip(generate(g2,n=100),generate(g,n=100)):
        newsent1=' '.join(sent)
        newsent2=' '.join(sent2)

        print(newsent1)
        print(newsent2)
        print("What is the two digit number?")
        print("\n")
elif input==25:
    g=CFG.fromstring(g16)
    g2=CFG.fromstring(g17)
    for sent,sent2 in zip(generate(g2,n=100),generate(g,n=100)):
        newsent1=' '.join(sent)
        newsent2=' '.join(sent2)

        print(newsent1)
        print(newsent2)
        print("What are their present ages?")
        print("\n")

elif input==26:
    mainList=[]
    sideList=[]
    g=CFG.fromstring(g20)
    g2=CFG.fromstring(g21)
##    for sent in generate(g,n=200):
##        newsent1=' '.join(sent)
##        #newsent2=' '.join(sent2)
##        ans1=ageFilter(newsent1)
##        #ans2=ageFilter(newsent2)
##        if(ans1 == None):
##            pass
##        else:
##            mainList.append(ans1)
##    print(mainList)
##            #print(ans2)
    for sent1,sent2 in zip(generate(g,n=200),generate(g2,n=200)):
        newsent1=' '.join(sent1)
        newsent2=' '.join(sent2)
        ans1=ageFilter(newsent1)
        ans2=ageFilter(newsent2)
        if(ans2 == None or ans1==None):
            pass
        else:
            print(ans1)
            print(ans2)
            print("What are their present ages?")
            print("\n")
   
    


            
            


    
    

            
            


  
        
        
            
