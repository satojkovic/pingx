#-*- encoding: utf-8 -*-

"""Usage: pingx.py [-t TITLE] [-m MEDIA] [-c COMMENT]

-t TITLE   specify a title
-m MEDIA   specify a media
-c COMMENT your review comment
"""

from docopt import docopt
import itunes
from pit import Pit
import twitter

def search_itunes_store(title, media):
    """
    search for content within iTunes store
    """
    items = itunes.search(query=title, media=media, store='JP')
    titles = []
    urls = []
    for item in items:
        print '[' + item.type + ']', item.get_name(), item.get_url(), item.get_release_date()
        titles.append(item.get_name())
        urls.append(item.get_url())

    # return top hits
    return titles[0], urls[0] if len(items)!=0 else ""

def main():
    args = docopt(__doc__, version="1.0")
    title = args['-t']
    media = args['-m']
    comment = args['-c']
    
    auth = Pit.get("twitter.com")
    api = twitter.Api(consumer_key = auth['ConsumerKey'],
                      consumer_secret = auth['ConsumerSecret'],
                      access_token_key = auth['AccessToken'],
                      access_token_secret = auth['AccessTokenSecret'])

    full_title, url = search_itunes_store(title, media)
    print "%s [%s]" %(full_title, url)

if __name__ == '__main__':
    main()
