from tweepy import OAuthHandler
from tweepy.streeming import StreemListener 
Consumer_Key ='whNUhg5NcrmJyTRa6dSipOMq2'
Consumer_Secret='eACzXRYOySCouGzMDfbKI7d1lFNyavXagmmxD1tY6gf8XVhLZP'
Access_Token='2677399741-UJrzodzbUn1HoEobo6T9mSq2tWxnmP37otu8MMw'
Access_TokenSecret='kLe3XbfjKV9uDdgp1iB08XqIkbEeMyUmrIjzRivvyF7RF'
     
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
