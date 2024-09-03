from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class Database:
    def __init__(self, name):
        
        self.df = pd.read_csv(f"../cleaned_data/{name}.csv")
        self.name = name 
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.df['abstract'])

class FinderModel:

    def __init__(self):
        self.data = Database('merged_publications')

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

        json = df_final.to_json(orient="records")

        
        return json


