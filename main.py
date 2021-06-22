"""
Provides main system to run.
"""

import random
from Resources.quotes_fetch import Quotes
from bots.config import create_api
from post import posting
from bots.tags import check_mentions
from bots.direct_message import direct_message_initial
from bots.retweet_fav import retweet_fav_post


api = create_api()
quote_class = Quotes()
quote_author = random.choice([quote_class.quotes_fav(),quote_class.quotable()])
quote = "\"" + quote_author[0] + "\" " + "- " + quote_author[1]


def tags():
    """
    Checks for tags, if any.
    """
    last_id = 1
    last_id = check_mentions(api,last_id,quote)

def message():
    """
    Sends a direct message.
    """
    direct_message_initial(api)

def tweet_quote():
    """
    Updates Tweet Quotes at scheduled interval.
    """
    api.update_status(quote)

def post():
    """
    Posts the image quotes.
    """
    posting(api)

def retweet_fun():
    """
    Retweets if there are any particular hastags.
    """
    retweet_fav_post(api)
