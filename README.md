# Bukowski Bot v2

This project was inspired by a blog post in /r/learnpython by user /u/benrules2 on how to create a simple markov chain. [That post can be found here.] (http://cyber-omelette.blogspot.com.au/2017/01/markov.html)

Using that idea of a markov chain, this project scrapes a bunch of poetry written by Charles Bukowski, and then feeds his poetry into the markov chain to create nonsensical tweets. I've made an option in settings.py to choose between generating tweets from individual poems or a single .txt file encompassing all of Bukowski's poetry; the tweets tend to be more coherent when generated from individual poems (because of their smaller sequences of phrases that already make sense).

Bukowski Bot v2 has been expanded upon to be more of an active twitter bot; I've added in functionality to retweet tweets made by other Twitter users who mention Bukowski and follow them.

I've automated this bot to run throughout the day using Windows Task Scheduler. Hopefully, I would like to see the bot grow up a sizeable follower list over time.

Here's the twitter bot in all its glory: <https://twitter.com/Bukowski_Blurb>

The website I scraped Bukowski's poetry from is <http://www.poemhunter.com/charles-bukowski/poems/>
