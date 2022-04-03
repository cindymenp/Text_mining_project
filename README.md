# Text_mining_project

## Summary


This study will examine different strategies that may improve the NPS comment filters and performance within X company. For this, different text mining techniques will be used, such as language identification, stemming, tokenization, data cleaning and the merging of two different csvs in order to find different keywords from one into the other. The study will use  NER and NEL. 

The Central Question in this research is: Could creating a csv file with different keywords while making use of the NLP,NER, NEL and Sentiment Analysis techniques in python improve the NPS comment filtering within the company?

The goal of the research is using knowledge and insight about text mining and different NLP techniques and creating  a strategy that can be used in future for filtering comments in the company. First, a literature review on text mining, artificial intelligence and different NLP techniques, then a strategy based on the knowledge collected is going to be devised and quantitatively examined by backtesting and live-testing in two main tasks from the company.

Text mining, or text analytics,  is known as an artificial intelligence (AI) technology that uses natural language processing (NLP) to transform unstructured text  from different sources (csv files, excel documents, websites, databases, etc) into  structured data suitable for analysis or to drive machine learning (ML) algorithms. 

In order to do so there will be used the following techniques: NER (Named entity recognition) which is referred to as an chunking, extraction, or identification entity which has as its main task to identify and categorize key information in text. Every detected key is classified into a predetermined category. Therefore, it will be possible to download into a csv different kinds of comments from Tableau. Afterwards, NER will be used in Python by having another csv file with the most important keywords, which consists of different tags for glasses or other products within the marketing department. Afterward, Python will be used to apply NEL (Named entity linking) and link and loop every keyword with all the rows from the comment. Afterwards, a sentiment analysis code will be created in order to filter positive, neutral or negative comments within any tag.  Finally, the information will be processed and connected with Tableau. Therefore it will be easier to filter multiple comments by specific tags and sentiments associated with it.


## Intructions

### pandas

```` 
#read csv file

csv = pd.read_csv ('/Users/cindy/Documents/Text mining project/csv_data.csv', encoding="utf8", on_bad_lines='skip', delimiter = ';')
csv

#expand lenght in the future from3 to 4+ comment_filter
```` 
```` 
#dictionary of keywords: from dataframe to list 

dictionary = pd.read_csv ('/Users/cindy/Documents/Text mining project/NPS_NLP categories.csv', on_bad_lines='skip', delimiter = ',')
dictionary = dictionary.fillna(method='ffill')
dictionary = dictionary.values.tolist()
dictionary  = [val for sublist in dictionary for val in sublist]
dictionary = [item.lower() for item in dictionary]
#dictionary = str(dictionary)

dictionary
```` 
### numpy
```` 
#Remove stop words and special characters

stop = stopwords.words('english')
csv["Improvement comment"] = csv["Improvement comment"].apply(lambda x: " ".join(x.lower() for x in str(x).split() if x not in stop))
csv["Improvement comment"] = csv["Improvement comment"].fillna('').astype(str).str.replace(r'[^A-Za-z ]', '', regex=True).replace('', np.nan, regex=False)

csv
```` 

### deep_translator 
```` 
#Translation

translated = []
for row in csv["Improvement comment"]:
    try:
        translated.append(GoogleTranslator(source='auto', target='en').translate(row))
    except:
        translated.append('')
        
csv["Improvement comment"]=translated

csv_2 = csv
```` 

### nltk 

```` 
#Remove stop words and special characters

stop = stopwords.words('english')
csv["Improvement comment"] = csv["Improvement comment"].apply(lambda x: " ".join(x.lower() for x in str(x).split() if x not in stop))
csv["Improvement comment"] = csv["Improvement comment"].fillna('').astype(str).str.replace(r'[^A-Za-z ]', '', regex=True).replace('', np.nan, regex=False)

csv
```` 
```` 
#Tokenize comment

csv["Improvement comment"] = csv["Improvement comment"].apply(word_tokenize)

#csv["Improvement comment"] = csv.apply(lambda row:word_tokenize(csv["Improvement comment"]),axis=1)

```` 

### trrex

```` 
#Comment column and dictionary comparison

query = tx.make(dictionary, r"\b(", r")\b")

csv["Word"] = csv["Improvement comment"].str.findall(r'{}'.format(query))
```` 

## Instructions

pandas

Terminal:

Python 2: pip install pandas //Python 3 : pip3 install pandas

Jupyter Lab:

Python 2: %pip install pandas //Python 3 : %pip3 install pandas

deep-translator

Terminal:

Python 2: pip install deep-translator //Python 3: pip3 install deep-translator

Jupyter Lab:

Python 2: %pip install deep-translator //Python 3: %pip3 install deep-translator

trrex

Terminal:

Python 2: pip install trrex //Python 3 : pip3 install trrex

Jupyter Lab:

Python 2: %pip install trrex //Python 3 : %pip3 install trrex

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
