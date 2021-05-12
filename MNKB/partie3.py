#!/usr/bin/env python
# coding: utf-8

# ***PROJET PYTHON***
# 

# **Partie 3**

# In[5]:


import requests
def get_page(link):
    code_page = requests.get(link)
    return code_page.text


# In[14]:


get_page('https://fr.wikipedia.org/wiki/Python_(langage)')


# In[13]:


import requests
import re
def get_emails(link):
    text = get_page(link)
    result = re.compile('([\w\.\-]+@[\w\.\-]+)').findall(text)
    return result


# In[11]:


get_emails('https://fr.wikipedia.org/wiki/Python_(langage)')


# In[18]:


import requests
import re
def get_urls(link):
        text = get_page(link)
        result = re.compile('(\w+)://([\w\-\.]+)/(\w+).(\w+)').findall(text)
        return result


# In[19]:


get_urls('https://fr.wikipedia.org/wiki/Python_(langage)')


# In[20]:


import requests
import re
def get_tables(link):
    text = get_page(link)
    liste = []
    balise = '<table>'
    if balise in text:
        liste.append(balise)
        return liste


# In[22]:


get_tables('https://fr.wikipedia.org/wiki/Table_(base_de_donn%C3%A9es)')


# In[ ]:




