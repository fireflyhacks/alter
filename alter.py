#[v0.9.6]

########################################################################################
#               PYTHON-TWITTER-NLP MODULE "ALTER" -- PRELIMINARY CODE                  #
########################################################################################

import tweepy
import os
import re
from itertools import chain
from textblob import TextBlob


'''get environment variables to access Twitter API'''
TWTAPIKEY = os.environ['TWTAPIKEY']
TWTAPISEC = os.environ['TWTAPISEC']
TWTACCTOK = os.environ['TWTACCTOK']
TWTACCSEC = os.environ['TWTACCSEC']


'''gets the rest of the word following the capital letter it begins with'''
def finder(string):
	ret = []
	for i in string:
		if i.islower():
			ret.append(i)
		else:
			break
	return ret;


'''gets the word by splitting at uppercase and calling finder(str) to get the rest'''
def splitter(trend):
    tmp = []
    ret = []
    for i in trend:
        index = trend.index(i)
        if i.isupper():
            tmp.append(i)
            tmp.append(finder(trend[index+1:]))
            newList = list(chain.from_iterable(tmp))
            listStr = ''
            listStr = listStr.join(newList)
            ret.append(listStr)
    return ret;
    
    
'''gets average trend polarity over the whole list of tokenized trends'''
def getAvgPolarity(l1):
    polarityValue = 0
    polarityList = []
    for i in l1:
        listStr = ' '.join(i)
        blob = TextBlob(listStr)
        polarityList.append(blob.sentiment.polarity)
    for p in polarityList:
        polarityValue += p
    return polarityValue/len(l1)


'''returns global sentiment of Trends'''
def allTrends():

	#Twitter OAuth
	auth = tweepy.OAuthHandler(TWTAPIKEY, TWTAPISEC)
	auth.set_access_token(TWTACCTOK, TWTACCSEC)
	api = tweepy.API(auth)
	trends = api.trends_place(1)
	
	#atomize trends from the returned list
	regex = r"(#[a-zA-Z]+)"
	joined = str(trends)
	trends = re.findall(regex, joined)
	
	#print list of captured trends and remove hashtags
	print("TRENDS:")
	print("-----------------------------------------")
	formatted_trends = []
	for t in trends:
	    print(t)
	    t_format = t.replace("#", "")
	    formatted_trends.append(t_format)
	    
	#break apart individual trends into their components for sentiment analysis
	tokenized_trends = []
	for f in formatted_trends:
		tokenized_trends.append(splitter(f))
	final_trends = []
	for t in tokenized_trends:
		if len(t) > 0:
			final_trends.append(t[len(t)-1])
	
	#get average polarity
	pVal = getAvgPolarity(final_trends)

	print('\n')
	print("pVal:", pVal)
	
	if pVal > 0:
		print('Twitter is upbeat!')
	elif pVal == 0:
		print('Twitter is content.')
	else:
		print('Twitter is ANGRY.')

	print("-----------------------------------------")
	print("[alter -- v0.9.6]")
	
	
#def likenessGroup():

	#TODO: read in Trends and perform various methods of subjective grouping
	

class Singul:

	#TODO:def1(tweepick)
		#print available trends, numbered
		#allow selection of one based on number or name match
		#analysis
		
	def tweepick(): 
	
		#Twitter OAuth
		auth = tweepy.OAuthHandler(TWTAPIKEY, TWTAPISEC)
		auth.set_access_token(TWTACCTOK, TWTACCSEC)
		api = tweepy.API(auth)
		trends = api.trends_place(1)
		
		#atomize trends from the returned list
		regex = r"(#[a-zA-Z]+)"
		joined = str(trends)
		trends = re.findall(regex, joined)
	
		#print list of captured trends and remove hashtags
		print("TRENDS:")
		print("-----------------------------------------")
		formatted_trends = []
		for t in trends:
			if trends.index(t) >= 10:
				print(trends.index(t), "--", t)
			else:
				print(str('0') + str(trends.index(t)), "--", t)
			t_format = t.replace("#", "")
			formatted_trends.append(t_format)
	
		#get user input and store specific trend at that index for analysis
		
		tpkQuit = False
		print("select Trend for analysis [ENTER NUMBER] or 'q' to quit")
		while(not tpkQuit):
			userIndex = input()
			if userIndex is "q":
				tpkQuit = True
				break
			singulton = trends[int(userIndex)]
			components = splitter(singulton)
			print(components)
		print("exiting Singul...")
		
########################################################################################
#                  AUTHOR: ALEC GOLDSTEIN, FIREFLY HACKS -- 2019                       #
########################################################################################
