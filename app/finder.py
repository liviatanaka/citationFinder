from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class Database:

    def __init__(self, name):
        self.df = pd.read_csv(f"../data/{name}.csv", nrows=1000)
        self.name = name 
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.df['abstract'])


class FinderModel:

    def __init__(self):
        self.arxiv = Database('arxiv')

    def predict(self, query):

        query = query.lower()
        X_query = self.arxiv.vectorizer.transform([query])

        # compute the relevance between the query and the documents in the dataset
        R = self.arxiv.X @ X_query.T

        # create a copy of the original df
        df_ = self.arxiv.df.copy()

        # convert the relevance matrix into one-dimensional array
        relevance =  R.toarray().flatten() 
        df_["relevance"] = relevance

        # filter and sort by relevance
        df_filtered = df_[relevance > 0.1]
        df_final = df_filtered.sort_values("relevance", ascending=False)

        # filter important columns
        df_final = df_final[['title', 'abstract', 'relevance']]

        json = df_final.to_json(orient="records")

        results = {'results': json, 'message': 'OK'}
        print(json)
        return results


a = FinderModel()
a.predict("machine learning")

# title
# authors
# abstract
# journal-ref
# doi
