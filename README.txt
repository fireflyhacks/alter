#########################################################################################
#                                    ALTER: README                                      #
#########################################################################################

   {7/7/19}

>> alter.py is preliminary code which currently only contains the function
   allTrends(). This function gathers a global collection of Trends, prints them, and
   returns the global sentiment by calculating average polarity of the atomized words
   composing each of the Trends.
   
   In the future, as described in "module.md", alter will be a
   fully fleshed-out package for many NLP functions using the tweepy Twitter API and
   various Python NLP tools such as Textblob. Additionally, "module.md" will be disposed
   of and its contents will be transferred to this readme.
   
>> alter.py expects four environmental variables:
   :: "TWTAPIKEY" [Twitter API Key]
   :: "TWTAPISEC" [Twitter API Secret Key]
   :: "TWTACCTOK" [Twitter Access Token]
   :: "TWTACCSEC" [Twitter Secret Access Token]
   
   Access to these keys can be granted by applying for a Twitter developer account.

#########################################################################################
#                  AUTHOR: ALEC GOLDSTEIN, FIREFLY HACKS -- 2019                        #
#########################################################################################
