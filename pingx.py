#-*- encoding: utf-8 -*-

"""Usage: pingx.py [-t TITLE] [-c COMMENT]

-t TITLE   specify a title
-c COMMENT your review comment
"""

from docopt import docopt
import itunes
from pit import Pit
import twitter

def main():
    args = docopt(__doc__, version="1.0")
    title = args['-t']
    comment = args['-c']
    
    auth = Pit.get("twitter.com")
    api = twitter.Api(consumer_key = auth['ConsumerKey'],
                      consumer_secret = auth['ConsumerSecret'],
                      access_token_key = auth['AccessToken'],
                      access_token_secret = auth['AccessTokenSecret'])

    print api.VerifyCredentials()
    
if __name__ == '__main__':
    main()
