#py.test test_population.py

import sqlite3
from os.path import join, dirname ,abspath
db_path = join(dirname(dirname(abspath(__file__))),'project1.db')



def linecount():

    conn = sqlite3.connect(db_path)  
    c = conn.cursor() 
    lines=c.execute('Select count(distinct title) from project1 ')
    
    for row in lines:
        x=(row[0])
    return x

def test_population():
    assert linecount()==7
    


#print(db_path)

