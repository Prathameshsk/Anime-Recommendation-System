# -*- coding: utf-8 -*-
"""Anime recom.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15grAVi5gqqw7JXXs-8uSSrksY4UGCpt0
"""



"""Importing Libraries

"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""Data collection and Pre-processing"""

anime_data=pd.read_csv('/content/Alldata.csv')

anime_data.head()

# Number of rows and coloumns

anime_data.shape

# Choose specific required features only

selected_features = ['anime_id','name','genre','type','episodes','rating','members','indexx']

# replacing the missing values with null
for feature in selected_features:
    anime_data[feature] = anime_data[feature].fillna('')

# Combining all the selected featues

combined_features = anime_data['anime_id'].astype(str)+' '+anime_data['name']+' '+anime_data['genre']+' '+anime_data['type']+' '+anime_data['episodes'].astype(str)+' '+anime_data['rating'].astype(str)+' '+anime_data['members'].astype(str)+' '+anime_data['indexx'].astype(str)

print(combined_features)

# Converting the text data into feature vectors

vectorizer = TfidfVectorizer()

# Replace missing values with an empty string
combined_features_filled = combined_features.fillna('')

# Vectorize the filled features
feature_vectors = vectorizer.fit_transform(combined_features_filled)

print(feature_vectors)

"""Cosine similarity"""

# Getting similarity score using cosine similarity

similarity = cosine_similarity(feature_vectors)

print(similarity)

print(similarity.shape)

# Getting anime name from user

anime_name = input('Enter your favourite anime name: ')

# Creating a list of all anime names in the data set present

list_of_all_names = anime_data['name'].tolist()
print(list_of_all_names)

# Finding the close match for the anime name given by the user

find_close_match = difflib.get_close_matches(anime_name,list_of_all_names)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

# Finding the index of the anime with name

index_of_anime = anime_data[anime_data['name'] == close_match]['indexx'].values[0]
print(index_of_anime)

# Getting list of similar anime

similarity_score = list(enumerate(similarity[index_of_anime]))
print(similarity_score)

# Sorting based on the similarity score

sorted_similar_anime = sorted(similarity_score,key = lambda x:x[1], reverse = True)
print(sorted_similar_anime)

# Printing the names of most similar movies based on the index

print('Anime suggested for you : \n')

print('******************************************************************************** \n')

i=1
for anime in sorted_similar_anime:
  indexx=anime[0]
  name_from_anime=anime_data[anime_data.indexx==indexx]['name'].values[0]
  if(i<16):
    print(i,'-',name_from_anime)
    i+=1
print('\n')
print('******************************************************************************** \n')
print('Enjoy watching')

"""ANIME RECOMMENDATION SYSTEM

"""

anime_name = input('Enter your favourite anime name: ')

list_of_all_names = anime_data['name'].tolist()

find_close_match = difflib.get_close_matches(anime_name,list_of_all_names)

close_match = find_close_match[0]

index_of_anime = anime_data[anime_data['name'] == close_match]['indexx'].values[0]

similarity_score = list(enumerate(similarity[index_of_anime]))

sorted_similar_anime = sorted(similarity_score,key = lambda x:x[1], reverse = True)

print('Anime suggested for you : \n')

print('******************************************************************************** \n')

i=1
for anime in sorted_similar_anime:
  indexx=anime[0]
  name_from_anime=anime_data[anime_data.indexx==indexx]['name'].values[0]
  if(i<16):
    print(i,'-',name_from_anime)
    i+=1
print('\n')
print('******************************************************************************** \n')
print('Enjoy watching')