import random
import requests
from fastapi import FastAPI
app = FastAPI()

memleket_db = {
    'kazakhstan': {
        'halyq_sany': '19mln',
        'prezidenti': 'Kasymzhomart Tokaev',
        'astanasy': 'Nur-sultan'
    },
    'france': {
        'halyq_sany': '67mln',
        'prezidenti': 'Emmanuel Macron',
        'astanasy': 'Paris'
    },
    'russia': {
        'halyq_sany': '146mln',
        'prezidenti': 'Vladimir Putin',
        'astanasy': 'Moscow'
    }
}

@app.get('/')
def home():
    return 'Bul ui paraqshasy!'

@app.get('/memleket')
def memleket():
    return memleket_db

@app.get('/memleket/{name}')
def info_memleket(name):
    if name in memleket_db:
        return memleket_db[name]
    else:
        return 'Qate'

@app.get('/quotes/{name}')
def quotes_for_name(name):
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote = response.json()
        result = 'Досым %s, менің саған кеңесім: %s' % (name.capitalize(), quote['content'])
        return result
    else:
        return 'Qate'