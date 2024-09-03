# citationFinder

When delving deeper into a particular subject, it is common to search for academic articles on the topic. citationFinder addresses the importance of obtaining multiple sources of reference when researching a specific topic, as studying different perspectives on the subject is essential for conducting a rich and comprehensive study.

In this context, the project uses the TF-IDF (Term Frequency-Inverse Document Frequency) method to analyze the relevance of terms within publixations abstract and, consequently, to find articles with a theme similar to a user-provided input.

## Dataset

This dataset available for search is a combination of the following data:

8398 publications extracted from [Springer](https://link.springer.com) that could be Research Articles or conference papers from 2025-2015

67,601 publications selected from the [arXiv Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv) from 2024-1025


[ArXiv](https://arxiv.org/) is a free distribution service, and an open-access archive for scholarly articles in the fields of physics, mathematics, computer science, quantitative finance, economics, etc. The articles from this archive are from a [Kaggle dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv).



## Running the Project with Docker

```bash
docker build -t home .
docker run -d -p 2004:8888 home
```


## Authors
[Livia Tanaka](https://github.com/liviatanaka)
[Tomás Alessi](https://github.com/alessitomas)
