# Literary-Twitterbot
A Twitterbot that randomly generates first lines of novels using Markov chains. Uploaded as a proof-of-concept.
Credit me if you want to use it as a base for your bot or some other purpose.
Feel free to use the corpus for other first line-based projects, but credit me as well.

 Requirements
1) A Twitter account with developer privileges

# Instructions
Create a twitter_credentials.py file (or something like that) and define four variables:
1) consumer_key
2) consumer_secret
3) access_token
4) access_token_secret

In order for the bot to work these must have the same values as the keys given to you when you received developer privileges on your
Twitter account. The main .py file is set up to read these in as external variables for use. Obviously, it is not safe to post your
access keys to the Internet, so don't do that. Another option for running is to just type them in at run-time.
