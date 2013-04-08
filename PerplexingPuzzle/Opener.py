""" 
Jiwei

The idea is to fetch the query result from amazon.com.

e.g. 
query: "wine"
related_searches: ["beer", "wine glasses", "wine rack"]
tranform to dict: {'beer': 1, 'glasses': 1, 'rack': 1, 'wine': 2}, for later use to check similarity

"""
import urllib2
from urllib import quote
from bs4 import BeautifulSoup

pattern_url = "http://www.amazon.com/s/url=search-alias%3Daps&field-keywords="

class Opener(object):
    def __init__(self, name):
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        _url = pattern_url + quote(name)
        self.content = self.opener.open(_url).read()
        self.related_searches = []
        self.name = name
        self.dict = {}

    def get_name(self):
        return self.name

    def get_related_searchs(self):
        if self.related_searches:
            return self.related_searches
        soup = BeautifulSoup(self.content)
        link = soup.find('div', id="relatedSearches")
        if link:
            link = link.find_all('a')
        if link:
            for key in link:
                self.related_searches.append(key.contents[0].encode('ascii', 'ignore'))
        return self.related_searches

    def get_dict(self):
        if self.dict:
            return self.dict
        vec = self.get_related_searchs()
        for item in vec:
            item = item.split()
            for key in item:
                self.dict[key] = (self.dict.get(key,0) + 1)

        return self.dict

# Test
def main():
    while True:
        a = Opener(raw_input())
        print a.get_related_searchs()
        print a.get_name()
        print a.get_dict()

if __name__ == "__main__":
    main()
