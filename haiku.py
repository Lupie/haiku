# Generate a haiku with punctuation for emphasis in and between lines
#
from lxml import html
import requests

page = requests.get('http://www.dictionary.com/browse/enigma?s=t')
tree = html.fromstring(page.content)



#This will create a list of buyers:
buyers = tree.xpath('//*[@id="source-luna"]/div[1]/section/header/div[2]/div[1]')
#This will create a list of prices
prices = tree.xpath('//*[@id="source-luna"]/div[1]/section/header/div[2]/div[1]/span[1]/span[2]')

print 'Buyers: ', buyers
print 'Prices: ', prices

from bs4 import BeautifulSoup as bs
import re
from requests import get

class dictionary:
  def remove_non_ascii(self,text):
    return re.sub(r'[^\x00-\x7F]+','', text)

  def get_soup(self,url):
    raw = self.remove_non_ascii(get(url).content)
    soup = bs(raw)
    return soup.select("#MainTxt")[0].select('.ds-single')[0].text.strip()

  def lookup(self,word):
    base_url  = "http://www.thefreedictionary.com/"
    query_url = base_url + word
    return self.get_soup(query_url)