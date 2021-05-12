import requests
def get_page(link):
    code_page = requests.get(link)
    return code_page.text



#get_page('https://fr.wikipedia.org/wiki/Python_(langage)')

import requests
import re
def get_emails(link):
    text = get_page(link)
    result = re.compile('([\w\.\-]+@[\w\.\-]+)').findall(text)
    return result


#get_emails('https://fr.wikipedia.org/wiki/Python_(langage)')

import requests
import re
def get_urls(link):
        text = get_page(link)
        result = re.compile('(\w+)://([\w\-\.]+)/(\w+).(\w+)').findall(text)
        return result


#get_urls('https://fr.wikipedia.org/wiki/Python_(langage)')



import requests
import re
def get_tables(link):
    text = get_page(link)
    liste = []
    balise = '<table>'
    if balise in text:
        liste.append(balise)
        return liste


#get_tables('https://fr.wikipedia.org/wiki/Table_(base_de_donn%C3%A9es)')





