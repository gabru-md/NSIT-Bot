import pandas as pd
from fuzzywuzzy import fuzz
import warnings
import urllib2

import json
import sys
sys.path.append('..//')
from nsitbot import NSITBot

url = "https://api.telegram.org/bot416198684:AAEsDGr1xM0-gQH2aN8cWVDpsGt2ryaCipI/getupdates"

page = urllib2.urlopen(url)

data = json.load(page)

incoming = data["result"][-1]['message']['text']
chatid = data["result"][-1]['message']['chat']['id']
print chatid

print "incoming : ",incoming

bot = NSITBot(
    name="My Bot",
    owner="Manish Devgan",
    version="0.0.1/Testing"
)


a = bot.predict(incoming.lower())

_ttype  = str(a[0])

print _ttype

warnings.filterwarnings("ignore")

def sim(str1,str2):
    return fuzz.token_sort_ratio(str1,str2) * 0.01



def something(incoming,_type):
    if incoming.endswith('?'):
        incoming = incoming.replace('?','')
    
    df = pd.read_csv("..//examples/responses.csv")
    
    df = df[df.class_name == _type]
    
    for index,message in zip(df['message'].index,df['message'].values):
        
        df.set_value(index,'percentage_match',sim(message,incoming))
        

    ndf = df.sort_values('percentage_match',ascending=False)
    return ndf['response1'].iloc[0]
 

url = "https://api.telegram.org/bot416198684:AAEsDGr1xM0-gQH2aN8cWVDpsGt2ryaCipI/sendmessage?chat_id="+str(chatid)+"&text="

new_url = url + str(something(incoming,_ttype))

print new_url

urllib2.urlopen(new_url)
print "sent"