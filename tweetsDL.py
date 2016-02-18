import tweepy
from tweepy import OAuthHandler
import json
import simplejson
from tweepy import Stream
from tweepy.streaming import StreamListener

with open("twitter_secrets.json.nogit") as fh:
    secrets = simplejson.loads(fh.read())


consumer_key =  secrets["api_key"]
consumer_secret = secrets["api_secret"]
access_token = secrets["access_token"]
access_secret = secrets["access_token_secret"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                #print json.loads(data)['entities']['hashtags']
                print json.loads(data)['text']
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['tequila','vodka'])    


#getTimeLine()

#for tweet in islice(tweet_generator(), 100):
   # print tweet
