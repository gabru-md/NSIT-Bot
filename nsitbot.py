from fuzzywuzzy import fuzz
import pandas as pd
import os
from trainer import trainer as Train

"""
NSIT Bot main class
"""

"""
method to find similarity in the strings
"""
def sim(str1,str2):
    return fuzz.token_sort_ratio(str1,str2) * 0.01
    

class NSITBot(object):
    def __init__(self,**kwargs):
        
        self.__name__ = kwargs.get('name','NSITBot')
        
        self.__owner__ = kwargs.get('owner','NSIT 2020')
        
        self.__version__ = kwargs.get('version','Test')
        
        
        """
        creating an instance of trainer inside NSITBot
        """
        
        self.trainer = Train(
        name = 'TrainerBot' 
        )
        
        self.hello_bot = ['bot_action','bot_author','bot_name','bot_version','hello']
        
        """
        fetching the classifier and vectorizer that 
        the NSITBot will use to predict the 
        classes of the recieved messaged from 
        the user end.
        """
        
        self.classifier,self.vectorizer = self.trainer.getClassifier()
        
    def predict(self,message):
        """
        take the message fromt the user and transform it.
        1.  convert the message into lower case so
            that the vectorizer can perfomr operations
            on it.
        2.  convert it into a LIST of message
            '[message]'.
        3.  transform the list using the vectorizer.transform()
            function so that further predictions can be 
            carried out on the message string.
        """
        self.message = message
        self.message_toLower = self.message.lower()
        self.messageList = [self.message_toLower]
        
        self.transformed_message = self.vectorizer.transform(self.messageList)
        
        self.prediction = self.classifier.predict(self.transformed_message)
        
        """
        the function will now return the prediction as a list
        """
        
        return [self.message_toLower,self.prediction[0]]
   
    def generateResponse(self,botPredict):
        """
        method to generate responses based on the query/
        message and the type of message
        """
        message_tolower = botPredict[0]
        prediction = botPredict[1]
        if prediction in self.hello_bot:
            self.response = self.getBotResponse(message_tolower,prediction)
        else:
            self.response = "idk"
        
        return self.response
            
    def getBotResponse(self,message_tolower,prediction):
        """
        method to predict the response if the prediction
        of the incoming message was among the following:
        self.hello_bot = ['bot_aciton','bot_author','bot_name','bot_version','hello']
        
        the response will be generated using the responses,csv
        or the hello_bot.csv
        """
        if message_tolower.endswith('?'):
            message_tolower = message_tolower.replace('?','')
        
        df = pd.read_csv("PATH TO 'hello_bot.csv'")
        
        df = df[df.class_name == prediction]
        
        for index,message in zip(df['message'].index,df['message'].values):
            df.set_value(index,'percentage_match',sim(message,message_tolower))
        
        ndf = df.sort_values('percentage_match',ascending=False)
        
        apt_response = ndf['response1'].iloc[0]
        
        return apt_response
        

""" 
There is no need to train the bot as the bot is trained automatically before 
the prediction phase starts.

prediction function can be found inside the trainer.py file and may be changed
depending upon the user.

the 'getClassifier' function inside the main class automatically invokes
the trainer to train our bot on all previously available data in form of 
.TRAINER files
"""

bot = NSITBot(
    name="My First Bot",
    owner="Manish Devgan",
    version="0.0.1" 
)
