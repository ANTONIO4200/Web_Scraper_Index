import requests
from bs4 import BeautifulSoup
import io


def get_site(URL_with_querry, noPages, html_filename):
    all_items = []

    for noPage in range(noPages):
        URL_to_scrape = URL_with_querry + str(noPage+1)

        page = requests.get(URL_to_scrape)
        soup = BeautifulSoup(page.content, 'html.parser')
        items_per_site = soup.find_all('a', class_='result')
        for item in items_per_site:
            all_items.append(item)
            all_items.append('\n')

    with io.open(html_filename, 'w', encoding='utf-8') as f:
        f.truncate(0)
        for item_html in all_items:
            f.write(str(item_html))
