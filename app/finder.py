from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pathlib

DATA_DIR= pathlib. Path.cwd() / "cleaned_data"
DATA_FILE_PATH = DATA_DIR / 'merged_publications.csv'

class Database:
    def __init__(self, data_path):
        
        self.df = pd.read_csv(data_path)
        self.df['title'] = self.df['title'].str.replace('\n', ' ')
        self.df['abstract'] = self.df['abstract'].str.replace('\n', ' ') 
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.df['abstract'])

class FinderModel:
    DATA_DIR= pathlib. Path.cwd() / "cleaned_data"
    DATA_FILE_PATH = DATA_DIR / 'merged_publications.csv'
    
    def __init__(self):
        self.data = Database(DATA_FILE_PATH)

    def predict(self, query):

        query = query.lower()
        X_query = self.data.vectorizer.transform([query])

        R = self.data.X @ X_query.T

        df_ = self.data.df.copy()

        relevance =  R.toarray().flatten() 
        df_["relevance"] = relevance

        df_filtered = df_[relevance > 0.1]
        df_final = df_filtered.sort_values("relevance", ascending=False)

        df_final = df_final[['title', 'abstract', 'relevance']]
        df_final = df_final.iloc[:10, :]
        json = df_final.to_json(orient="records")

        
        return json


