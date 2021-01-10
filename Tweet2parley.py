#Bot to forward tweets from Twitter to Parler
#This should effectively make this account a Twitter client
#NOTE: I initially made some typos spelling "parley" as "parlay." I intend to fix them soon. Look out for them!
from parler import Parler
import tweepy
import time
import datetime
import pickle
import re

#Parler authentication
mst = ''
jst = ''

#Parler api used through `paClient`
paClient = Parler(mst,jst)

#Twitter authentication
api = 'sorry!'
api_secret = 'no'
bearer = 'keys'

access = 'for'
access_secret = 'you'

auth = tweepy.OAuthHandler(api,api_secret)
auth.set_access_token(access, access_secret)

#Twitter api used through 'twClient'
twClient = tweepy.API(auth)

scrapeUsers = ['WheresDaVaccine','RocketLeague','cfm_miku_en','NintendoAmerica','Xbox','PlayStaion','GregAbbott_TX','Minecraft','Wendys','dbrand']
ignoreParlay = [] #List of Tweets already found, to prevent spam. May also help filter out Twitter spam as well.
followList = {} #Reimplement Twitter follwoing by responding to the Parley with a list of Parler user mentions
def saveToFile(listName,fileName):
    with open(fileName, 'wb') as handle:
        pickle.dump(listName, handle, protocol=pickle.HIGHEST_PROTOCOL)

def postNewParley(body): #Currently does not support Parler features such as sensitivity or state. Links are (hopefully) included in body.
    paClient.post(body,[],sensitive=False,state=4)
"""
def getPostId(value):
    post = paClient.getPostsOfUserId('Tweet2Parley',limit=10000,startKey=False)
    for i in range(0,len(post['posts'])):
        print('Info:')
        print(post['posts'][i]['_id'])
        print(post['posts'][i]['body'])
        twUsername = post['posts'][i]['body']
        twUsername = re.search('\*#(.*)\: ',twUsername)
        print(f'USERNAME: {twUsername.group(1)}')
"""

def findTweets():
    for i in range (0, len(scrapeUsers)):
        user = twClient.get_user(scrapeUsers[i])
        #NOTE: Implement time check to allow for multiple tweets to be forwarded
        tweet = twClient.user_timeline(screen_name=scrapeUsers[i], count=25, include_rts = False, tweet_mode= 'extended')
    for status in tweet:
        newParlay=(f'@#{status.user.screen_name} tweeted:\n{status.full_text} \n(Tweeted on {status.created_at.date()} at {status.created_at.time()})\nhttps://twitter.com/{status.user.screen_name}/status/{status.id}')
        if status.created_at.date() == datetime.date.today() and newParlay not in ignoreParlay:
            print(f'Parleying:\n{newParlay}\n')
            postNewParley(newParlay)
            ignoreParlay.append(newParlay)
            print(f'Saving to {ignoreParlaydb}...')
            saveToFile(ignoreParlay,ignoreParlaydb)
            print('Waiting 15 seconds...')
            time.sleep(15)

#CONFIG:
VERSION = '1.0-alpha'
WAIT_TIME = 1800
scrapeUsersdb = 'scrapeUsersdb.pickle'
ignoreParlaydb = 'ignoreParlaydb.pickle'
#END CONFIG

#Main code:
print(f'Tweet2Parlay version {VERSION}')
print(f'Loading {scrapeUsersdb}...')
try:
    with open(scrapeUsersdb, 'rb') as handle:
        scrapeUsers = pickle.load(handle)
        print(f'{scrapeUsersdb} loaded successfully!')
except:
    print(f'ERROR: Failed to load {scrapeUsersdb}. Generating a new one.')
    with open(scrapeUsersdb, 'wb') as handle:
        pickle.dump(scrapeUsers, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('Done!')
print(f'Loading {ignoreParlaydb}...')
try:
    with open(ignoreParlaydb, 'rb') as handle:
        ignoreParlay = pickle.load(handle)
        print(f'{ignoreParlaydb} loaded successfully!')
except:
    print(f'ERROR: Failed to load {ignoreParlaydb}. Generating a new one.')
    with open(ignoreParlaydb, 'wb') as handle:
        pickle.dump(ignoreParlay, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('Done!')
while True:
    print("Finding tweets...")
    findTweets()
    print(f'Taking a {WAIT_TIME} second break to prevent overloading Parler servers')
    time.sleep(WAIT_TIME)


