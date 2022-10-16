import sys
import json
import requests
import dewiki

def wiki_request():
    if len(sys.argv) != 2:
        return print('wrong argument')
    response = requests.get(
        'https://fr.wikipedia.org/w/api.php',
        params={
            'action': 'query',
            'prop': 'revisions',
            'rvprop': 'content',
            'titles': sys.argv[1],
            'format': 'json',
            'redirects' : '1'
        }
    )
    try:
        response_json = json.loads(response.content)
        pages = response_json['query']['pages']
        for query, page in pages.items():
            text = dewiki.from_string(page['revisions'][0]['*'])
            break
    except Exception as e:
        return print(f'Error : {e}')
    file = open(sys.argv[1].replace(' ', '_')+'.wiki', 'w')
    file.write(text)
    file.close()

if __name__ == '__main__':
    wiki_request()
