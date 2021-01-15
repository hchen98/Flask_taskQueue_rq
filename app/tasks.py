from urllib import request
from bs4 import BeautifulSoup
import lxml
import time

def cound_wrds(url):
    print(f"Counting words at {url}")

    start = time.time()

    r = request.urlopen(url)
    soup = BeautifulSoup(r.read().decode(), "lxml")
    paragraphs = " ".join(p.text for p in soup.find_all("p"))

    wrd_count = dict()

    for item in paragraphs.split():
        if not item in wrd_count:
            wrd_count[item] = 1
        else:
            wrd_count[item] += 1
        
    end = time.time()

    time_elapsed = end - start

    print(f"Word count: {wrd_count}")
    print(f"Total words: {len(wrd_count)}")
    print(f"Time elapsed: {time_elapsed} ms")

    return len(wrd_count)