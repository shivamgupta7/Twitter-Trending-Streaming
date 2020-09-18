import socket
import sys
import requests
import requests_oauthlib
import json
import os

# Replace the values below with yours
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
# print(ACCESS_TOKEN)
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)


def send_tweets_to_spark(http_resp, tcp_connection):
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text'] + '\n' # pyspark can't accept stream, add '\n'
            print("Tweet Text: " + tweet_text)
            print ("------------------------------------------")
            tcp_connection.sendall(tweet_text.encode('utf-8'))
        except:
            e = sys.exc_info()[0]
            print("Error: %s" % e)


def get_tweets():
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    query_data = [('language', 'en'), ('locations', '68.11,8.06,97.41,37.10'), ('track', '#')]  # this location value for india
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=my_auth, stream=True)
    print(query_url, response)
    return response


TCP_IP = "127.0.0.1"
TCP_PORT = 9009
conn = None
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((TCP_IP, TCP_PORT))
soc.listen(1)
print("Waiting for TCP connection...")
conn, addr = soc.accept()
print("Connected... Starting getting tweets.")
resp = get_tweets()
send_tweets_to_spark(resp,conn)