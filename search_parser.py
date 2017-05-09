import tweepy
from settings import *
import datetime


class Parser:
    tweets = []
    users = []
    count = 0

    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.date = datetime.date.today()

        print 'Initiated Retweet Parser for ' + str(self.date)

    def search(self):
        for x in range(0, len(KEYWORDS)):

            if len(self.tweets) >= THRESHOLD:
                break

            results = self.api.search(q=KEYWORDS[x], rpp=SEARCH_RETURN, since_id=self.date, lang=LANG)
            self.count += len(results)
            print 'Total search results: ' + str(self.count)
            print KEYWORDS[x]

            for y in range(0, len(results)):
                USER_ID = results[y].author.id
                ID = results[y].id


                print 'ID: ' + str(ID)
                retweets = len(self.api.retweets(ID))
                print 'Retweets: ' + str(retweets)

                if retweets >= RETWEET_POPULARITY:
                    self.tweets.append(ID)
                    print 'Retweet found.\n'
                    self.users.append(USER_ID)

                if len(self.tweets) >= THRESHOLD:
                    print 'Max Retweet Threshold met.'
                    break


    def retweet(self):
        retweeted = 0
        print 'Retweeting grabbed tweets...'
        for tweet in self.tweets:
                try:
                    self.api.retweet(tweet)
                    retweeted += 1
                except tweepy.TweepError:
                    print 'Oops! Already retweeted ' + str(tweet)
                    pass
        print str(retweeted) + ' made.\n'

    def follow(self):
        for user in self.users:
            try:
                self.api.create_friendship(user)
                print('Followed User: ' + str(user))
            except Exception as e:
                print(e)
                pass
        print('\n')


if __name__ == '__main__':
    run = Parser()
    run.search()
    run.retweet()
    run.follow()