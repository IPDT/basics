#for python 3
#cache decorator example
#by aw
import sys
import urllib.request as request

# define a decorator
def cache(func):
    saved = {}

    def wrapper(url):
        if url in saved:
            print("cached version...")
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            print("new version...")
            return page
    return wrapper

# use docorator
@cache
def web_lookup(url):
    return request.urlopen(url).read()

#test
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "https://www.bing.com/"

for _ in(range(2)):
    web_lookup(url)

