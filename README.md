# citationFinder
Para aprender de maneira mais aprofundada sobre determinado assunto é comum que se procure artigos acadêmicos sobre o mesmo. O citationFinder surge da importância de obter mais de uma fonte de referência ao pesquisar sobre determinado tópico, posto que para se ter uma pesquisa rica é essencial que se estude diferentes perspectivas do assunto. 

Dessa maneira, o projeto tem como objetivo encontrar artigos com uma temática semelhante a uma determinada entrada do usuário, sendo essa, por exemplo, o resumo de outro artigo.

## Dataset

This dataset has articles from arXiv and BaseDoTom.

[ArXiv](https://arxiv.org/) is a free distribution service, and an open-access archive for scholarly articles in the fields of physics, mathematics, computer science, quantitative finance, economics, etc. The articles from this archive are from a [Kaggle dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv).

## Running the Project with Docker

```bash
docker build -t home .
docker run -d -p 2004:8888 home
```


## Authors
[Livia Tanaka](https://github.com/liviatanaka)
[Tomás Alessi](https://github.com/alessitomas)