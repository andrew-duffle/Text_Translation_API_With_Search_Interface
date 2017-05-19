#!/usr/bin/env python
#-*- coding: utf-8 -*-

import project1
from project1 import project1
import nltk


def main():
    ##### Createing the database to insert data into 
    project1.createdb()
    
    ####### Get and clean the data
    project1.fetchdata()
    
    #######Create the FTS db
    project1.build_FTS()
    
    #######Launch the search program
    project1.Search()
    
if __name__=='__main__':
    main()
