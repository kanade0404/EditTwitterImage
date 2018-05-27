import os
import tweepy
import urllib.request
import datetime


def get_oauth():
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_key = os.environ["ACCESS_TOKEN_KEY"]
    access_secret = os.environ["ACCESS_TOKEN_SECRET"]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.in_reply_to_screen_name == 'py_kanade':
            print(status.author.screen_name)
            if 'media' in status.entities:
                medias = status.entities['media']
                m = medias[0]
                media_url = m['media_url']
                try:
                    urllib.request.urlretrieve(media_url, 'icon.jpg')
                except IOError:
                    print("保存に失敗しました")
                now = datetime.datetime.now()
                time = now.strftime("%H:%M:%S")
                message = '@' + status.author.screen_name + ' アイコンを変更しました(' + time + ')'
                try:
                    api.update_profile_image('icon.jpg')
                    api.update_status(status=message, in_reply_to_status_id=status.id)
                except tweepy.error.TweepError as e:
                    print("error response code: " + str(e.response.status))
                    print("error message: " + str(e.response.reason))


auth = get_oauth()
api = tweepy.API(auth)
stream = tweepy.Stream(auth, StreamListener(), secure=True)
stream.userstream()
