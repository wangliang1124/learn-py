import sys
import requests
import json
from bs4 import BeautifulSoup

search_query = sys.argv[1]
 
def get_results(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'html5lib')
    def_blocks = bs.find_all('div', class_="def-block ddef_block")
   

    search_results = []
    for def_block in def_blocks:
       
        explanation =  BeautifulSoup(str(def_block),'html5lib').find(class_='def ddef_d db')
        example = BeautifulSoup(str(def_block),'html5lib').find(class_='examp dexamp')

        if example is None:
            example = ""
        else:
            example = example.text

        search_results.append({
            'explaination': explanation.text,
            'example': example
        })

    return search_results;

def get_alfred_items(search_results):
    formatted_results = []
    for item in search_results:
        result = {
            "title": item["explaination"],
            "subtitle": item["example"],
            "arg": "",
            "autocomplete": "",
            "icon": {
                "path": ""
             }
        }
        formatted_results.append(result)

    return formatted_results

if __name__ == "__main__":
    search_results = get_results('https://dictionary.cambridge.org/dictionary/english/' + search_query)
    
    alfred_json = json.dumps({
        "items": get_alfred_items(search_results)
    }, indent=2)

    sys.stdout.write(alfred_json)
