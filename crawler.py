import time
import urllib

import bs4
import requests


start_url = "https://en.wikipedia.org/wiki/Special:Random" # change your start
target_url = "https://en.wikipedia.org/wiki/Philosophy"
visited_urls = [start_url]

def find_first(url): # Doesn't work on countries, returns null
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    article_link = None
    article_links=[]

    # Inspect the wiki page to see the DOM tree and the name of id, classs.
    # Find all the direct children of content_div that are paragraphs
    for p in soup.find(id="mw-content-text").find(class_="mw-parser-output").findAll('p', recursive=False):
        # print(len(p.findAll('a'))==0,'\n',p.findAll('a')) #see all links
        if len(p.findAll('a'))==0: #skip paragraphs without links
            pass
        elif p.find('a', class_='mw-selflink selflink', recursive=False): # wiki page of Greek Language gave a dead end bec, there was a class with the link tag.
            pass #skip
        else:
            # get the first link that isn't italic and that doesn't have any other classes
            if p.find('a', recursive=False):
                article_link = p.find("a", recursive=False).get('href')
                break
   
    if not article_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

def continue_crawl(search_history, target_url, max_steps=100):
    if search_history[-1] == target_url:
        print("We've found the target article! It only took us {} times".format(len(search_history)))
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search")
        return False
    elif search_history[-1] in search_history[:len(search_history)-1]:
        print("We've arrived at an article we've already seen, aborting search at {}".format(search_history[-1]))
        return False
    else:
        return True



if __name__ == '__main__':
    print('Starting...')
    while continue_crawl(visited_urls, target_url, 100):
        print(visited_urls[-1])

        first_link = find_first(visited_urls[-1])
        if not first_link:
            print("We've arrived at a dead end at {}, aborting search".format(visited_urls[-1]))
            break

        visited_urls.append(first_link)

        time.sleep(0.5) # wait between requests to avoid wiki server blocking

