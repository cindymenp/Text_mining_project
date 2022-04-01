# installing packages

%pip install pandas
%pip install deep-translator
%pip install google_trans_new 
%pip install google-cloud-translate==2.0.1
%pip install trrex


#Importing libraries

import glob
import pandas as pd
import numpy as np
from pandas import read_csv
from deep_translator import GoogleTranslator
from nltk import word_tokenize
import re
import nltk
import csv
nltk.download('vader_lexicon')
nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd
import trrex as tx

#read csv file

csv = pd.read_csv ('/Users/cindy/Documents/Text mining project/csv_data.csv', encoding="utf8", on_bad_lines='skip', delimiter = ';')
csv

#expand lenght in the future from3 to 4+ comment_filter

#drop columns

csv.drop(csv.columns[2], axis=1, inplace=True)

#Remove stop words and special characters

stop = stopwords.words('english')
csv["Improvement comment"] = csv["Improvement comment"].apply(lambda x: " ".join(x.lower() for x in str(x).split() if x not in stop))
csv["Improvement comment"] = csv["Improvement comment"].fillna('').astype(str).str.replace(r'[^A-Za-z ]', '', regex=True).replace('', np.nan, regex=False)

#dictionary of keywords: from dataframe to list 

dictionary = pd.read_csv ('/Users/cindy/Documents/Text mining project/NPS_NLP categories.csv', on_bad_lines='skip', delimiter = ',')
dictionary = dictionary.fillna(method='ffill')
dictionary = dictionary.values.tolist()
dictionary  = [val for sublist in dictionary for val in sublist]
dictionary = [item.lower() for item in dictionary]


#Translation

translated = []
for row in csv["Improvement comment"]:
    try:
        translated.append(GoogleTranslator(source='auto', target='en').translate(row))
    except:
        translated.append('')
        
csv["Improvement comment"]=translated

csv_2 = csv

csv = csv_2

import nltk
nltk.download('punkt')
  

#Tokenize comment

csv["Improvement comment"] = csv["Improvement comment"].apply(word_tokenize)


#csv["Improvement comment"] = csv.apply(lambda row:word_tokenize(csv["Improvement comment"]),axis=1)

#convert imporvement list into str

csv["Improvement comment"] = [','.join(map(str, l)) for l in csv["Improvement comment"]]

#Comment column and dictionary comparison

query = tx.make(dictionary, r"\b(", r")\b")

csv["Word"] = csv["Improvement comment"].str.findall(r'{}'.format(query))

#drop comment columns

csv.drop(csv.columns[1], axis=1, inplace=True)

csv = csv[csv['Word'].map(lambda d: len(d)) > 0]

#Save socument

#csv.to_csv("data_edited_2.csv", sep='\t', encoding='utf-8')

