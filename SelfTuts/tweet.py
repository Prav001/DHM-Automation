from twython import Twython
import string, json, pprint
import urllib
from datetime import timedelta
from datetime import date
from time import *
import string, os, sys, subprocess, time
# probably wasteful imports, but in this case, who cares?
import pymssql

conn = pymssql.connect(host='localhost',  user='notsa', password='notsayly', database='TallicaTweets')

#conn = connect(DRIVER={SQL Server Native Client 10.0};SERVER=dagger;DATABASE=test;UID=user;PWD=password)

cur = conn.cursor()
# connect to our database and create a cursor to do some work

harvest_list = ['metallica', 'james hetfield', 'lars ulrich', 'kirk hammett', 'rob trujillo', 'jason newsted', 'cliff burton']
# my aforementioned harvest list, use as many as you want, 
# they will all be separated in the database by keyword


cur.execute("select max(isnull(batchid,0)) from tweetlog")
batch_id_cur = cur.fetchall()
# updated 3-8-2012
if batch_id_cur[0][0] is None:
    batch_id = 0
else:
    batch_id = batch_id_cur[0][0]+1
# grabbing the last "batch id", if it exists so we
# can make log entries that make SOME sense



for tweet_keyword in harvest_list: # for each keyword, do some shit

        cur.execute("""delete from tweetbanktemp where tweet_keyword = '"""+str(tweet_keyword)+"""'""")
        conn.commit()
        # whack the temp table in case we didn't exit cleanly

        twitter = Twython()
        search_results = twitter.searchTwitter(q=tweet_keyword, rpp="100")
        # our search for the current keyword

        #pp = pprint.PrettyPrinter(indent=3)
        # uncomment for debugging and displaying pretty output

        for tweet in search_results["results"]:
                # some me the tweet, jerry!
                print "        Tweet from @%s Date: %s" % (tweet['from_user'].encode('utf-8'),tweet['created_at'])
                print "        ",tweet['text'].encode('utf-8'),"\n"

                try:
                        # lets try to to put each tweet in our temp table for now
                        cur.execute("""insert into TweetBankTemp (tweet_id, tweet_datetime, tweet_keyword, tweet, tweeter, lang)
                                        values ('"""+str(tweet['id_str'].encode('utf-8').replace("'","''").replace(';',''))+"""',
                                                cast(substring('"""+str(tweet['created_at'].encode('utf-8'))+"""',5,21) as datetime),
                                                '"""+str(tweet_keyword)+"""',
                                                '"""+str(tweet['text'].encode('utf-8').replace("'","''").replace(';',''))+"""',
                                                '"""+str(tweet['from_user'].encode('utf-8').replace("'","''").replace(';',''))+"""',
                                                '"""+str(tweet['iso_language_code'].encode('utf-8').replace("'","''").replace(';',''))+"""'
                                        ) """)
                except:
                        print "############### Unexpected error:", sys.exc_info()[0], "##################################"
                        # just in case something heinous happens we don't lose 
                        # ALL the tweets in this run, just the error one


        cur.execute("""insert into tweetbank (tweet_id, tweet_datetime, tweet_keyword, tweet, tweeter, lang)
        select * from tweetbanktemp where tweet_id NOT in
        (select distinct tweet_id from tweetbank)""")
        # take all the tweets that we DIDNT already have
        # and put them in the REAL tweet table

        cur.execute("""delete from tweetbanktemp where tweet_keyword = '"""+str(tweet_keyword)+"""'""")
        # take all THESE out of the temp table to not
        # interfere with the next keyword

        cur.execute("""insert into tweetlog (BatchId, keyword, RunDate, HarvestedThisRun, TotalHarvested) values
        (
        '"""+str(batch_id)+"""',
        '"""+str(tweet_keyword)+"""',
        getdate(),
        ((select count(*) from tweetbank where tweet_keyword = '"""+str(tweet_keyword)+"""')-(select top 1 isnull(TotalHarvested,0) from tweetlog where keyword = '"""+str(tweet_keyword)+"""' order by RunDate desc)),
        (select count(*) from tweetbank where tweet_keyword = '"""+str(tweet_keyword)+"""')
        )""")
        # add a record to the log table saying what we did!

        conn.commit()
        # hot soup!
