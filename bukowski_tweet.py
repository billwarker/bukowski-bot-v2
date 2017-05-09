from settings import *
import os
import random
import tweepy
import datetime
from markov import read_file
from markov import build_chain
from markov import generate_message
from markov import write_file

class BukowskiTweet:
    poems = []

    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.date = datetime.date.today()

        print 'Initiated Bukowski Tweet for ' + str(self.date)

    def pickPoem(self):
        [self.poems.append(poem) for poem in os.listdir(PATH)]
        pick = random.choice(self.poems)
        print pick
        return pick

    def tweet(self, message):
        self.api.update_status(message)

if __name__ == '__main__':

    tweet = BukowskiTweet()

    if MERGE == True:
        print 'Tweeting from bukowski_merge.txt'
        message = read_file(r'Scraping and Merging Poems/bukowski_merge.txt')

    else:
        message = read_file(PATH + tweet.pickPoem())

    chain = build_chain(message)
    message = generate_message(chain)
    write_file('output.txt', message)
    print message
    tweet.tweet(message)
    print '-'*10
    print 'Done'

