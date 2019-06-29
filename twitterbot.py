import tweepy
from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret
import markovify
from time import sleep
import random

"""
class authorBot
A Twitterbot that Tweets a randomly generated first line from a book
By Patteron Jaffurs
"""
class authorBot:

    #init
    # loads the corpus, establishes the API connection to Twitter
    def __init__(self, corpus):
        self.load_corpus(corpus)

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    #load_corpus()
    # loads the corpus into Markovify and builds the Markov Chain
    def load_corpus(self, corpus):
        with open(corpus) as corpusFile:
            corpusText = corpusFile.read()
        self.model = markovify.Text(corpusText, state_size=2)

    #tweet()
    # randomly selects an option and tweets a generated sentence
    def tweet(self):
        random.seed()
        for i in range(20):
            r = random.randint(0,5)
            if r == 0:
                str = self.model.make_short_sentence(70)
                #print(len(str))
            elif r == 1:
                str = self.model.make_short_sentence(70)
            elif r == 2:
                str = self.model.make_sentence_with_start('It')
            elif r == 3:
                str = self.model.make_sentence_with_start('The')
            elif r == 4:
                str = self.model.make_sentence_with_start('In')
            elif r == 5:
                str = self.model.make_sentence_with_start('I')
            #extra case for failed generation
            while str == None:
                str = self.model.make_short_sentence(70)
            print(str)

        if len(str) > 140:
            self.tweet()
            return

        try:
            self.api.update_status(str)
            print('Tweeting: {}'.format(str))

        except tweepy.TweepError as error:
            print(error.reason)

    #automate()
    # sends a tweet and then pauses
    def automate(self, delay):  
        #for i in range(20):
        self.tweet()
        sleep(delay)

if __name__ == '__main__':
    bot = authorBot('corpus.txt')
    bot.automate(900)
