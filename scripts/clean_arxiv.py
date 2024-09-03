import pandas as pd


def main():
    df = pd.read_json("../data/arxiv-metadata-oai-snapshot.json", lines=True, nrows=300000)

    df.dropna(subset=['title', 'abstract', 'update_date'],inplace=True)

    # revelant columns
    revelant_columns = ['title', 'authors', 'journal-ref', 'doi', 'abstract', 'update_date']
    df = df[revelant_columns]

    # filter data (last 10 years)
    df['update_date']=df['update_date'].astype("datetime64[ns]")
    df = df[df["update_date"].dt.year >= 2015]


    # print(df.info())
    print('-'*50)
    print(df.index.size)
    print('-'*50)


    # # print(df['update_date'])
    # print(df.iloc[0])

    df.to_csv('../data/arxiv.csv')

main()