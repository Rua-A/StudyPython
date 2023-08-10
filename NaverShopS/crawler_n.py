import requests
from bs4 import BeautifulSoup
import urllib.parse

def encode_to_utf8(input_string):
    encoded_string = urllib.parse.quote(input_string)
    return encoded_string

class Crawler():
    def naver_shop_search(self, query: str):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        text = []
        query = encode_to_utf8(query)
        try:
            response = requests.get(f'https://msearch.shopping.naver.com/search/all?query={query}&prevQuery={query}',headers=headers)

            content = response.text
            soup = BeautifulSoup(content,'html.parser')
            list = soup.find(class_='relatedTag_scroll_area__NG5Gs')
            lists = list.find_all('li')
            for content in lists:
                text.append(content.text)

        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        
        data = {
        'keyword':query,
        'result':text
        }
        return data

