# citationFinder

When delving deeper into a particular subject, it is common to search for academic articles on the topic. citationFinder addresses the importance of obtaining multiple sources of reference when researching a specific topic, as studying different perspectives on the subject is essential for conducting a rich and comprehensive study.

In this context, the project uses the TF-IDF (Term Frequency-Inverse Document Frequency) method to analyze the relevance of terms within publications abstract and, consequently, to find articles with a theme similar to a user-provided input.

## Dataset

This dataset available for search is a combination of the following data:

8398 publications extracted from [Springer](https://link.springer.com) that could be Research Articles or conference papers from 2025-2015

67,601 publications selected from the [arXiv Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv) from 2024-2015


[ArXiv](https://arxiv.org/) is a free distribution service, and an open-access archive for scholarly articles in the fields of physics, mathematics, computer science, quantitative finance, economics, etc. The articles from this archive are from a [Kaggle dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv).

### Test Cases

In this section, we provide examples of different types of search queries and their results. These examples demonstrate the functionality and behavior of the search engine under various conditions.

#### 1. Test that yields 10 results
**Query:** `neural network`  
**Link:** [http://10.103.0.28:2004/query?query=neural+network](http://10.103.0.28:2004/query?query=neural+network)  
**Comment:** Searching for "neural network" yields exactly 10 results.

#### 2. Test that yields less than 10 results
**Query:** `nlp`  
**Link:** [http://10.103.0.28:2004/query?query=nlp](http://10.103.0.28:2004/query?query=nlp)  
**Comment:** Searching for "nlp" returns fewer than 10 results, because there aren't enough relevant documents in the database (we are applying a minimum relevance filter).

#### 3. Test that yields something non-obvious
**Query:** `wolf`  
**Link:** [http://10.103.0.28:2004/query?query=wolf](http://10.103.0.28:2004/query?query=wolf)  
**Comment:** The search for "wolf" might initially suggest results related to the animal, but it yields articles on unexpected topics, such as `Wolf-Rayet`. This non-obvious result highlights the search engine's capability to identify and return documents that relate to lesser-known or niche interpretations of a query, beyond the immediately obvious meaning.

## Running the Project with Docker

```bash
docker build -t home .
docker run -d -p 2004:8888 home
```


## Authors
[Livia Tanaka](https://github.com/liviatanaka)
[Tomás Alessi](https://github.com/alessitomas)
