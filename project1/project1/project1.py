import urllib.request
from bs4 import BeautifulSoup 
from nltk import sent_tokenize
#nltk.download("book")
import re
import sqlite3
import requests 
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
conn = sqlite3.connect('project1.db')
c = conn.cursor() 
 

def createdb():
    c.execute(''' Drop Table If Exists project1''') 
    c.execute(''' Create Table project1 (
                            title Text,
                            book Text,
                            language Text,
                            author Text,
                            dates Text,
                            chapter Text,
                            verse Text,
                            passage Text,
                            link Text)''') 
   
    
###############retrieval function   
    
    
def read_text(url):
    d =urllib.request.urlopen(url)
    text=d.read().decode('iso-8859-1').encode('utf-8')
    soup=BeautifulSoup(text,"lxml")
    clean1=soup.get_text()
    return clean1
 
def fetchdata():

    ##########################get avianus
    
    
    avianus= (read_text('http://thelatinlibrary.com/avianus.html'))
     
    #clean out a bunch of junk
    clean=re.sub('\xa0|\xbb','',avianus)#strip some unconvertable char
    clean=re.sub('\t','',clean)
    clean=re.sub(r'([A-Z])\.',r'\1',clean) #get roman numeral and headers together
    clean=re.sub(r'([A-Z]l)\.','II',clean) #fix one weird header
    clean=re.sub(r'([A-Z][A-Z])\s+([A-Z][a-z])',r'\1. \2',clean)#split off the title
    clean=re.sub(r'\n+(VII)',r'. \1',clean) #fix VII missing a . in text
    #clean=re.sub(r'\.\[\w+','[',clean)
    clean=re.sub(r'\]\n','].',clean)
    clean=re.sub(r'\d\w',' ',clean)
    clean=re.sub(r'\d\n',' ',clean)
    clean=re.sub(r'[?|$|!|;|:|,]','',clean)
    clean=re.sub('\n',' ',clean)
    clean=re.sub('IX DE DUOBUS SOCIIS ET URSA.','IX [DE DUOBUS SOCIIS ET URSA].',clean) # a section that is missing []
    x=sent_tokenize(clean)
    avianus=[]
    avianus=list(map(lambda a: a.strip(r'\n'), x))
    avianus=avianus[1:] #to remove the first element that is the header information
    avianus.pop() #to remove the last element that is a footer
     
    #print(avianus)
    
    title='AVIANI FABULAE'
    language='LATIN'
    link='http://thelatinlibrary.com/avianus.html'
    
    verse=1
    chapter=0
    
    for passage in avianus:
        if re.match(r'.*[A-Z]\s+\[.*\]\.$',passage) is not None:
            chapter=chapter+1
            verse=1
        else:
            c.execute("Insert Into project1 (title,book,language,author,dates,chapter,verse,passage,link) values (?,?,?,?,?,?,?,?,?)",
                  (title,None,language,None,None,chapter,verse,passage,link))
            verse=verse+1
                                    
    conn.commit()
    
    
    ##########################get greg
    
    greg= (read_text('http://thelatinlibrary.com/greg.html'))
    
    #clean out a bunch of junk
    clean=re.sub('\xa0','',greg)
    clean=re.sub('\t','',clean)
    clean=re.sub(r'\.\s\[\w+','[',clean)
    clean=re.sub(r'\]\n','].',clean)
    clean=re.sub(r'\d\w',' ',clean)
    clean=re.sub(r'\d\n',' ',clean)
    clean=re.sub(r'[?|$|!|;|:|,]','',clean)
    clean=re.sub('\n',' ',clean)
    x=sent_tokenize(clean)
    greg=[]
    greg=list(map(lambda a: a.strip(r'\n'), x))
    greg=greg[1:] #to remove the first element that is the header information
    greg.pop() #to remove the last element that is a footer
    
    #print(greg)
    
    title='EPISTOLAE AD CONSTANTINAM AVGVSTAM'
    language='LATIN'
    author='SANCTI GREGORII MAGNI'
    dates='IV.30'
    link='http://thelatinlibrary.com/greg.html'
    
    verse=1
    
    
    for passage in greg:
        c.execute("Insert Into project1 (title,book,language,author,dates,chapter,verse,passage,link) values (?,?,?,?,?,?,?,?,?)",
                  (title,None,language,author,dates,None,verse,passage,link))
        verse=verse+1
                                    
    conn.commit()
    
    ##########################get minucius
    
    minucius= (read_text('http://thelatinlibrary.com/minucius.html'))
    
    #clean out a bunch of junk
    clean=re.sub('\xa0','',minucius)
    clean=re.sub('\t','',clean)
    clean=re.sub('(OCTAVIUS)\s+',r'\1. ',clean)
    clean=re.sub(r'(I)(.)\n+(Cogitanti\b)',r'I . \3 ',clean) 
    clean=re.sub(r'\]\n','].',clean)
    clean=re.sub(r'\d\w',' ',clean)
    clean=re.sub(r'\d\n',' ',clean)
    clean=re.sub(r'blanditur\!','blanditur.',clean)
    clean=re.sub(r'\'Nos Proinde','Nos Proinde',clean)
    clean=re.sub(r'[?|!|$|;|:|,|"|\']','',clean) #I had to strip some strange formating around '
    clean=re.sub('\n',' ',clean)
    x=sent_tokenize(clean)
    minucius=[]
    minucius=list(map(lambda a: a.strip(r'\n'), x))
    minucius=minucius[1:] #to remove the first element that is the header information
    minucius.pop() #to remove the last element that is a footer
    
    #print(minucius)
    
    title='OCTAVIUS'
    language='LATIN'
    author='M. MINUCII FRLICIS'
    link='http://thelatinlibrary.com/minucius.html'
    
    verse=1
    chapter=0
    
    for passage in minucius:
        if re.match(r'^[A-Z][a-z]',passage) is None:
            chapter=chapter+1
            verse=1
        else:
            c.execute("Insert Into project1 (title,book,language,author,dates,chapter,verse,passage,link) values (?,?,?,?,?,?,?,?,?)",
                  (title,None,language,author,None,chapter,verse,passage,link))
            verse=verse+1
                                    
    conn.commit()
    
    ####################get williamapulia
    
    williamapulia= (read_text('http://thelatinlibrary.com/williamapulia.html'))
    
    #clean out a bunch of junk
    clean=re.sub('\xa0|\xbb|\x97','',williamapulia)
    clean=re.sub('\t','',clean)
    clean=re.sub(r'\.\s\[\w+','[',clean)
    clean=re.sub(r'\]\n','].',clean)
    clean=re.sub(r'\d\w',' ',clean)
    clean=re.sub(r'\d\n',' ',clean)
    clean=re.sub(r'[?|$|!|;|:|,|"]','',clean)
    clean=re.sub('\n',' ',clean)
    clean=re.sub(r'(\w*[A-Z][A-Z]\b)\s+([A-Z][a-z]\w*\b)',r'\1. \2',clean)
    clean=re.sub(r'(Gesta ducum)',r' \1',clean)
    clean=re.sub(r'(LIBER)',r'. \1',clean)
    clean=re.sub(r'(INCIPIUNT GESTA   .)','',clean)
    clean=re.sub(r'^s\)','INCIPIT',clean)
    x=sent_tokenize(clean)
    williamapulia=[]
    williamapulia=list(map(lambda a: a.strip(r'\n'), x))
    williamapulia=williamapulia[2:] #to remove the first element that is the header information
    williamapulia.pop() #to remove the last element that is a footer
    
    #print(williamapulia)
    
    title='GESTA ROBERTI WISCARDI'
    dates='1090'
    language='LATIN'
    author='GUILLELMUS APULIENSIS'
    link='http://thelatinlibrary.com/poggio.html'
    
    verse=1
    book=0
    
    for passage in williamapulia:
        if re.match(r'^INCIPIT|^LIBER',passage) is not None:
            book=book+1
            verse=1
        else:
            c.execute("Insert Into project1 (title,book,language,author,dates,chapter,verse,passage,link) values (?,?,?,?,?,?,?,?,?)",
                  (title,book,language,author,dates,None,verse,passage,link))
            verse=verse+1
                                    
    conn.commit()
    
    ##########################get poggio
    
    poggio= (read_text('http://thelatinlibrary.com/poggio.html'))
    
    #clean out a bunch of junk 
    clean=re.sub(r'(\d+\b)\.',r'\1',poggio) #strip the period after the number on section headings
    clean=re.sub(r'([A-Z][a-z]*)\n+',r'\1.',clean) #add a period to tokenize after section heading
    clean=re.sub(r'52','. 52',clean) #there is an extra ' on the end of 51 I wanted to keep this until we translate incase it is needed
    clean=re.sub('\t+','',clean)
    clean=re.sub(r'[$|!|;|:|,|"]','',clean) # get rid of special charactars 
    clean=re.sub('\n',' ',clean) #stip extra spacing
    x=sent_tokenize(clean)
    poggio=[]
    poggio=list(map(lambda a: a.strip(r'\n'), x))
    poggio=poggio[1:] #to remove the first element that is the header information
    poggio.pop() #to remove the last element that is a footer
    
    #print(poggio)
    
    title='FACETIAE'
    language='LATIN'
    author='GIAN FRANCESCO POGGIO BRACCIOLINI'
    link='http://thelatinlibrary.com/poggio.html'
    
    verse=1
    chapter=0
    
    for passage in poggio:
        if re.match(r'^[0-9]|52 Alia',passage) is not None:
            chapter=chapter+1
            verse=1
        else:
            c.execute("Insert Into project1 (title,book,language,author,dates,chapter,verse,passage,link) values (?,?,?,?,?,?,?,?,?)",
                  (title,None,language,author,None,chapter,verse,passage,link))
            verse=verse+1
                                    
    conn.commit()
    
    
    ##########################get priapea
    
    priapea= (read_text('http://thelatinlibrary.com/priapea.html'))
    
    #clean out a bunch of junk 
    clean=re.sub('\x97','',priapea)
    clean=re.sub(r'(\d+\b)\.',r'\1',clean) #strip the period after the number on section headings
    clean=re.sub(r'([A-Z][A-Z])\n+',r'\1. ',clean) #add a period to tokenize after section heading
    clean=re.sub('\t+','',clean)
    clean=re.sub(r'[?|$|!|;|:|,|"|\*|]','',clean) # get rid of special charactars
    clean=re.sub(r'\(\)]','(?)]',clean) #put back the ? in the section numbers
    clean=re.sub(r'(I]|L]|X]|V]|C]|D]|M]|\)])',r'\1.',clean) #add a period to teh section headers to tokenize 
    clean=re.sub('\n',' ',clean) #stip extra spacing
    x=sent_tokenize(clean)
    priapea=[]
    priapea=list(map(lambda a: a.strip(r'\n'), x))
    priapea=priapea[1:] #to remove the first element that is the header information
    priapea.pop() #to remove the last element that is a footer
    
    #print(priapea)
    
    title='CARMINA PRIAPEA'
    language='LATIN'
    author='PRIAPEA'
    link='http://thelatinlibrary.com/priapea.html'
    
    verse=1
    chapter=0
    
    for passage in priapea:
        if re.match(r'^\[[A-Z].',passage) is not None:
            chapter=chapter+1
            verse=1
        else:
            c.execute("Insert Into project1 (title,book,language,author,dates,chapter,verse,passage,link) values (?,?,?,?,?,?,?,?,?)",
                  (title,None,language,author,None,chapter,verse,passage,link))
            verse=verse+1
                                    
    conn.commit()
    
    
    ##########################get arnulf
    
    arnulf= (read_text('http://thelatinlibrary.com/arnulf.html'))
    
    #clean out a bunch of junk 
    clean=re.sub('\xa0','',arnulf)
    clean=re.sub(r'(\w*[A-Z][A-Z]\b)\s+([A-Z][a-z]\w*\b)',r'\1. \2',clean) #add a period to tokenize after section heading
    clean=re.sub('\t+','',clean)
    clean=re.sub(r'[?|$|!|;|:|,|"|\*|]','',clean) # get rid of special charactars
    clean=re.sub('\n',' ',clean) #stip extra spacing
    x=sent_tokenize(clean)
    arnulf=[]
    arnulf=list(map(lambda a: a.strip(r'\n'), x))
    arnulf=arnulf[1:] #to remove the first element that is the header information
    arnulf.pop() #to remove the last element that is a footer
    
    #print(arnulf)
    
    title='DE NATIVITATE DOMINI'
    language='LATIN'
    author='ARNULF OF LISIEUX'
    link='http://thelatinlibrary.com/arnulf.html'
    
    verse=1
    
    for passage in arnulf:
        c.execute("Insert Into project1 (title,book,language,author,dates,chapter,verse,passage,link) values (?,?,?,?,?,?,?,?,?)",
                  (title,None,language,author,None,None,verse,passage,link))
        verse=verse+1
                                    
    conn.commit()
    
    
    #conn.close()    
    
    
def build_FTS():
    c.execute(''' Drop Table If Exists Latin_FTS''')
    c.execute("CREATE VIRTUAL TABLE Latin_FTS using fts4(title, book, language, author, dates, chapter, verse, passage, link);")
    c.execute("Insert into Latin_FTS (title, book, language, author, dates, chapter, verse, passage, link) Select title, book, language, author, dates, chapter, verse, passage, link from project1;")



#==============================================================================
# def Query_FTS(word_passed):
#     for row in c.execute ("select passage,link from Latin_FTS where passage match '(%s)'; " % word_passed):
#         print(row)
#==============================================================================


def Search():

    word_entered=''
    
    option=input("Enter English for English, Latin for Latin or Quit to Quit:")
    Title_of_Document=[]
    Frequency_of_Word=[]
    
    
    
    while option.strip() != 'Quit':
        
        if option.strip() == 'Latin':
            word_entered = input("Enter a word: ")
            #print(word_entered)
            #print(type(word_entered))
            for row in c.execute ("select title,count(DISTINCT passage) from Latin_FTS where passage match '(%s)' group by title order by count(DISTINCT passage) desc; " % word_entered):
                Title_of_Document.append(row[0])
                Frequency_of_Word.append(row[1])
            y_pos= np.arange(len(Title_of_Document))
            plt.bar(y_pos, Frequency_of_Word, align='center', alpha=0.5)
            plt.xticks(y_pos,Title_of_Document)
            plt.xticks(rotation=90)
            plt.ylabel('Frequency')
            plt.title('Frequency of word used in document')
            plt.show()
            Title_of_Document=[]
            Frequency_of_Word=[]
            for row in c.execute ("select passage,link from Latin_FTS where passage match '(%s)'; " % word_entered):
                print(row)
            #Query_FTS(word_entered)
            option=input("Enter English for English, Latin for Latin or Quit to Quit: ")
        
        if option.strip() == 'English':
            word_entered = input("Enter a word: ")
            Translator=requests.get("http://api.mymemory.translated.net/get?q=(%s)&langpair=en|lat" % word_entered)
            Translator=Translator.json()
            Translations=(re.findall(r'\'translatedText\': \'(.*?)\',',str(Translator))) 
            Translations=re.sub(r'["|\'|\]|\[|\}|,]','',str(Translations))
            print("Your word translates to: " + Translations)
            #print(type(Translations))
            word_entered=Translations
            #print(type(word_entered))
            for row in c.execute ("select title,count(DISTINCT passage) from Latin_FTS where passage match '(%s)' group by title order by count(DISTINCT passage) desc; " % word_entered):
                Title_of_Document.append(row[0])
                Frequency_of_Word.append(row[1])
            y_pos= np.arange(len(Title_of_Document))
            plt.bar(y_pos, Frequency_of_Word, align='center', alpha=0.5)
            plt.xticks(y_pos,Title_of_Document)
            plt.xticks(rotation=90)
            plt.ylabel('Frequency')
            plt.title('Frequency of word used in document')
            plt.show()
            Title_of_Document=[]
            Frequency_of_Word=[]
            for row in c.execute ("select passage,link from Latin_FTS where passage match '(%s)'; " % word_entered):
                print(row)
            #Query_FTS(word_entered)
            option=input("Enter English for English, Latin for Latin or Quit to Quit: ")
            
        if option.strip() != 'Quit' and option.strip() != 'English' and option.strip() != 'Latin':
            option=input("Enter English for English, Latin for Latin or Quit to Quit: ")
            
#==============================================================================
# 
# createdb()
#     
#     ####### Get and clean the data
# fetchdata()
#     
#     #######Create the FTS db
# build_FTS()
#     
#     #######Launch the search program
# Search()
# 
#==============================================================================

   

    
#Translations=(re.findall(r'\'translatedText\': \'(.*?)\',',str(Translator))) 
