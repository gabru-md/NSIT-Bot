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
        
        self.hello_bot = ['bot_action','bot_author','bot_name','bot_version','hello','endings']
        
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
        if message_tolower:
            message_tolower = message_tolower.replace('?','')
        
        df = pd.read_csv("responses\\hello_bot.csv")
        
        df = df[df.class_name == prediction]
        
        for index,message in zip(df['message'].index,df['message'].values):
            df.set_value(index,'percentage_match',sim(message,message_tolower))
        
        ndf = df.sort_values('percentage_match',ascending=False)
        
        apt_response = ndf['response1'].iloc[0]
        
        return apt_response
        
    def getBest_QueryID(self,message_topredict):
        """
        getBest_QueryID() will return the query ID,
        i.e., the best possible match from the csv.
        
        the 'status_id' field inside the csv contains
        the unique id for every status.'status_id' has 
        data in format GROUP_ID + '_' + STATUS_ID
        
        each and every status will be checked and
        compared with the 'message'. 
        a unique score or 'percentage_match' will
        determine the match %.
        
        the onw with the best match will be returned.
        """
        queryDataFrame = pd.read_csv('Path to CSV')
        
        status_queryDataFrame = queryDataFrame[queryDataFrame.status_type == 'status']
        
        """
        status_queryDataFrame now contains all the 
        posts with TYPE = 'status'
        
        this sorting is done to only get written
        messages from the csv file.
        """
        
        for index,message in zip(status_queryDataFrame['status_message'].index,status_queryDataFrame['status_message'].values):
            status_queryDataFrame.set_value(index,'percentage_match',sim(message,message_topredict))
        
        finalFrame = status_queryDataFrame.sort_values('percentage_match',ascending=False)
        
        apt_id = finalFrame['status_id'].iloc[0]
        apt_author = finalFrame['status_author'].iloc[0]
        
        return [apt_id,apt_author]
               
            
    
    def getBest_Response(self,queryID,queryAuthor):
        """
        method for generating the best possible 
        response for the incoming message using the 
        queryID generated by matching the incoming
        message with each and every message.
        """
        
        commentDataFrame = pd.read_csv('PATH TO COMMENT CSV')
        
        newDF = commentDataFrame[commentDataFrame.status_id == queryID and commentDataFrame.comment_author != queryAuthor]
        
        """
        newDF is the new DF which 
        contains all the comments for the queryID.
        all the comments from the queryAuthor are 
        removed in order to get the comments from others
        only. as the author's comments may contains questions
        and will definitely not contain the answer to his/her
        query. XD
        """
    
        """
        the dataframe must have a field called 'rating'.
        'rating' will be used to rate each and every 
        comment and then the best of all will be chosen.
        """
        for index,likes,loves,wows,hahas,sads,angrys in zip(newDF['comment_likes'].index,newDF['num_likes'].values,newDF['num_loves'].values,newDF['num_wows'].values,newDF['num_hahas'].values,newDF['num_sads'].values,newDF['num_angrys'].values):
            rating = float(1*int(likes) + 0.5*int(loves) + 1.5*(wows) - (int(angrys) + int(sads)) - 1.5*int(hahas))
            newDF.set_value(index,'rating',rating)
        
        """
        now the dataFrame 'newDF' contains
        the rating for all the comments in response 
        to the queryID.
        """
        
        sortedDF = newDF.sort_values('rating',ascending=False)
        apt_comment = sortedDF['comment_message'].iloc[0]
        
        return apt_comment
                
            
        
        
    
    def getStreamBasedResponse(self,message_tolower,prediction):
        """
        test method for StreamBasedResponse
        """
        message_topredict = message_tolower
        if message_topredict:
            message_topredict = message_topredict.replace('?','')
        
        """
        Two csv files are used.
        
        first file is used to match with the best query
        pertaining in the group.
        
        second file contains the comments to all the 
        queries and will be used to predict the
        apt_response for the particular message.
        """
        
        best_query = self.getBest_QueryID(message_topredict)
        queryID = best_query[0]
        queryAuthor = best_query[1]
        
        best_Response = self.getBest_Response(queryID,queryAuthor)
        
        return best_Response
        
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
    version="0.0.3" 
)
