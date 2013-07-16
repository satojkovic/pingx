#-*- encoding: utf-8 -*-

"""Usage: pingx <-t title> <-m media> [-c <comment>]

Options:
    -t title   specify a title
    -m media   specify a media
    -c <comment> your review comment
"""

from docopt import docopt
import itunes
from pit import Pit
import twitter
import googl

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
    return titles[0], urls[0] if len(items)!=0 else None

def main():
    args = docopt(__doc__, version="1.0")
    title = args['-t'].decode('utf-8')
    media = args['-m']
    comment = args['-c'].decode('utf-8')

    # search content and get URL
    full_title, url = search_itunes_store(title, media)

    if url is None:
        print "No result..."

    # shorten URL
    g = googl.Googl()
    short_url = g.shorten(url)
    print "%s -> %s" %(url, short_url['id'])

    # post to Twitter
    auth = Pit.get("twitter.com")
    api = twitter.Api(consumer_key = auth['ConsumerKey'],
                      consumer_secret = auth['ConsumerSecret'],
                      access_token_key = auth['AccessToken'],
                      access_token_secret = auth['AccessTokenSecret'])

    status = comment + " " + title + " - " + "[" + short_url['id'] + "]"
    print status

    api.PostUpdate(status)

if __name__ == '__main__':
    main()
