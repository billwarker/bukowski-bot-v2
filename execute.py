from settings import *
from markov import *
from bukowski_tweet import BukowskiTweet
from search_parser import Parser
import time

if __name__ == '__main__':
    print 'starting...'

    # Retweets & Follow
    search_parser = Parser()
    search_parser.search()
    search_parser.retweet()
    search_parser.follow()


    # Original Markov Tweet
    tweet = BukowskiTweet()

    if MERGE:
        print 'Tweeting from bukowski_merge.txt'
        message = read_file(r'C:\PythonScripts\Bukowski Bot\Scraping and Merging Poems\bukowski_merge.txt')

    else:
        message = read_file(PATH + tweet.pickPoem())

    chain = build_chain(message)
    message = generate_message(chain)
    # write_file('output.txt', message)
    print message
    tweet.tweet(message)
    print '-' * 10
    print 'Done'
    time.sleep(5)
