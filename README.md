# Text_Translation_API_With_Search_Interface
README Project1

Project1.py
The required packages for the code are urllib.request, beautiful soup, nltk, re, and sqlite3.

NOTE: when installing the program depending on if you have nltk installed using sudo. If you do not already have it universally you can uncomment line 4 and download nltk(‘book’). This will provide the  tokenizer I used to breakup sentences. If you already have it installed no need for this line. I did this to save space on the program from downloading every time. 

Function creatdb():
	Title: this is the title of each text as recorded in the page details. Each text has a variable I set
	associated with it.

	Book: I made books relate to texts that had more than a chapter and verse structure. The only text I had that this relates to was the Williama Pulia text. It is debatable if these should have just 		been treated like chapters since there is no chapter structure in the text. The translations would translate to beginning and end of books so I went ahead and used this field instead of 		chapter.       

	Language: The language is difficult to tell in some cases it was assumed that all the texts were in Latin. There were certainly some that lacked proper punctuation and consistency. The 		language was not documented in the page documentation. 

	Author: Author was taken directly from the page documentation returned using urllib. After I located them I just added the variable to each text to keep the formatting consistent in the 		database.  

	Dates: Same as Author tried to capture as many as I could from the page meta. Where I could find them it is recorded in a variable. Most did not have dates recorded. 

	Chapter: Chapters are indicative of section headers and count accordingly.  Most texts have some type of section headings. I started out saving that text to the database, the heading are so 		different text to text I made the decision to number the sections for consistency. Still straight forward and associated with a section header. 

	Verse: Verse is the token entered from nltk tokenization. In most texts this is associated to a period. The use of other punctuation in  most text was not indicative of a verse. There are rare 	occasions where other punctuation can be used for tokenization.     

	Passage: The tokenized sentence returned. In many cases this is based on sentences ending with a period. I found multiple instances in the Latin language where ? Or ! Were not indicative of 		sentence structure. Because of this I selected to remove them in texts where I had certain instance of this.

	Link: the URL link to the text




Function read_text():
	Uses urllib.request.urlopen() to return the webpage of the passed in URL. We then read the the 	returned data. This is where we try to decode as much as possible. There was no documentation 	for 		the encoding on the page (not standard) there were multiple special characters. What I found was that most aligned with iso-8859-1 a Latin based encoding. I used this to decode  but most texts 	still end up with non translatable characters I end up stripping. Then I used beautiful soup to get a text variable stored and used for processing each text. 

Function fetchdata():
	 fetchdata() is just one big wrapper that holds the processing for the seven different texts. Within this each section had its own code that uses the read_text(). After we return each URL text 		there is multiple lines of regular expression clean up. The regex in each section refers to corrections for inconstancy in each text. You will see some that are very general in nature and almost 		always used and then you will see very targeted corrects for typo or anomalies in that text. After we have clean text the insertion is pretty straight forward. The only thing that really changes 		is dentifying what constitutes a section or chapter in for the insert. I also set some variable per text for information like author, url or title.


TESTS
The test folder contains two tests. They can be run using python3 setup.py test in the command line.

test_extraction.py:
	The test_extraction.py is an assertion comparing the length of the returned data to the documented length in the page. It uses urllib to return the content length form the meta data and 		compares that to the data we get by reading the the text. If the assertion passes we can conclude that our reader function works accurately.

test_population.py:
	test_population.py is also an assertion test. You have to have a populated project1.db database. The test tests that the database has been successfully populated with 7 distinct titles. If the 	test is successful we know that at a minimum we have populated the database with 7 texts.



Poject1 Part B

Function build_FTS()
	Pretty straight forward if there is a Latin_FTS table already in existence we start by dropping the table. Next we create the FTS table and copy over the data form the project1 table.

Function Search()
	This is the search interface intended to run from the command line.  The first prompt will ask for input of English, Latin, or Quit. Quit pretty straight forward, this will break the loop and exit 		the program. If you select Latin you will be prompted for a Latin term to search for. The assumption is made that we are only searching for individual words not phrases. Every time you search a 		bar graph will pop up displaying the frequency within documents for a term. When you exit this model the passage and web links for every time we found the word will be printed to screen. After 		that you will receive the original prompt asking for input of English, Latin, or Quit. When English is selected it works very similar to the Latin option. You will enter an English term again 	single word. We run it through the translation service. After a lot of trial an error I found about the only usable translation it the first one the API returns. It turns out that the first one 		returned also has the highest rating of translation.   There are some rare cases when the API out put has changed on me and it returns an extra comma  or bracket. I have tried to code in every 		extra characters that I have got thus far and strip it off. There is the remote possibility that you could have add one to the strip list if the API changes again. When you select English the 	first line returned is the translation the API returned. Then exactly the same as the Latin option you will get a graph of the frequency and when you click off the graph you will get the print out 		of the passage and links. After this you will be prompted again with the original prompt asking for input of English, Latin, or Quit.   






 
         
