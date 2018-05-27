import tweepy

consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print("Access:", auth.get_authorization_url())
verifier = input('Verifier:')
auth.get_access_token(verifier)
print("Access Token:", auth.access_token)
print("Access Token Secret:", auth.access_token_secret)
