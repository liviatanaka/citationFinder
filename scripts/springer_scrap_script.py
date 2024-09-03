import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_springer_data(base_url):
    """Scrapes data from Springer website across multiple pages.

    Args:
        base_url (str): The URL of the first page of Springer search results.

    Returns:
        list: A list of dictionaries, each containing data for a single article.
    """

    all_data = []
    page_num = 1
    erros = 0

    while True:
        # Construct the URL for the current page
        url = f"{base_url}&page={page_num}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find articles on the current page
        articles = soup.find_all('a', class_='app-card-open__link') 
        if not articles:  # Stop if no more articles are found
            break

        # Process articles on the current page
        for article in articles:
            article_link = article['href'] 
            
            # Construct the full URL if it's relative:
            if not article_link.startswith("http"):
                article_link = "https://link.springer.com" + article_link

            # Try to access the URL:
            try:
                article_response = requests.get(article_link)
                
                article_response = requests.get(article_link)
                article_soup = BeautifulSoup(article_response.content, 'html.parser')

                title = article_soup.find('h1', class_='c-article-title').text.strip()
                abstract_element = article_soup.find('div', id='Abs1-content')
                abstract = abstract_element.find('p').text.strip() if abstract_element else ""

                
                article_data = {
                    'title': title,
                    'abstract': abstract,
        
                }

                all_data.append(article_data)
                print(len(all_data))
            except:
                print("ERROR")
                erros += 1

        # Move to the next page
        page_num += 1
        if page_num > 1:
            break
    
    return all_data




def web_scrap(year):
    # Example usage (same base URL):
    url = f"https://link.springer.com/search?new-search=true&query=&content-type=research&content-type=conference+paper&date=custom&dateFrom={year}&dateTo={year}&sortBy=newestFirst"
    results = scrape_springer_data(url)
    df = pd.DataFrame(results)
    df.to_csv(f"df_{year}.csv", index=False)


year = [2025]

for y in year:
    web_scrap(y)