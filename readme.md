
# web crawler: Getting to Philosophy :snail:

## Overview
A script to reach the philosophy wiki page starting from a random wiki page. The search continues until the goal has been reached, visiting an already visited page or reaching a dead end page with no outgoing links. Learn more [here](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy).
**requests** and **Beautiful Soup** for scraping and parsing data.

## How to run the project
- In you code editor's terminal run the following:
1. Install requests and Beautiful Soup through `pip install requests` and `pip install beautifulsoup4`.
2. Navigate into the project's directory `cd 'Philosphy crawler'`.
3.  Run the project `python crawler.py`.
## Test Run
- You can leave the starting url to random or choose a wiki page youself.
`Starting...`  
`https://en.wikipedia.org/wiki/The_Beatles`  
`https://en.wikipedia.org/wiki/Rock_music`  
`https://en.wikipedia.org/wiki/Popular_music`  
`https://en.wikipedia.org/wiki/Music`  
`https://en.wikipedia.org/wiki/The_arts#Music`  
`https://en.wikipedia.org/wiki/Creativity`  
`https://en.wikipedia.org/wiki/Idea`  
`We've found the target article! It only took us 8 times`  
### Note
- I ran into a dead end with the [Greek Language](https://en.wikipedia.org/wiki/Greek_language) wiki page as there was an additional class associated with first link tag. I added a condition to avoid that. Refer [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters) for examples for filtering.
- Make sure to check the DOM tree of the page if you run into any unexpected behavior.
