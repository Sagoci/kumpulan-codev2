from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

df1 = pd.read_csv('five_star_reviews.csv')
df1.head()
