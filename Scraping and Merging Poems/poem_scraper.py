import requests
import bs4
import os

def setup():
    path = 'bukowski poems'
    if path in os.listdir("."):
        pass
    else:
        os.makedirs(path)

def get_title():
    title = str(soup.select('h1'))
    length = len(title)
    junk = len(r'[<h1 class="title w-660" itemprop="name">')
    endjunk = len((r'</h1>]'))
    title = title[junk:(length-endjunk)]
    return title

def get_text():
    poem = soup.select('p')
    fill = '                             '
    poem = str(poem[1])
    poem = poem[29:]
    poem = poem.replace("<br/>", "\n")
    poem = poem.replace("</p>", " ")
    return poem

def next_poem():
    link = soup.select('a')[28]
    next = link.get("href")
    return next

def write_file(filename, message, count):
    try:
        with open(str(count) + ') ' + filename, "w") as file:
            file.write(message)
    except:
        with open(str(count) + ') ' + '.txt', "w") as file:
            file.write(message)

if __name__ == '__main__':
    setup()
    os.chdir('bukowski poems')
    base_url = r"http://www.poemhunter.com"
    start_poem = '/poem/16-bit-intel-8088-chip/'
    url = base_url + start_poem
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    count = 0

    for x in range(151):
        try:
            title = get_title()
            text = get_text()
            count += 1
            write_file(title + '.txt', text, count)
            if count < 2:
                link = soup.select('a')[26]
                next = link.get("href")
            else:
                next = next_poem()
            print count

        except requests.exceptions.InvalidURL:
                next_poem()

        url = base_url + next
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "lxml")


