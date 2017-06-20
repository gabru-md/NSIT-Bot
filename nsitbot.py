
from trainer import trainer as Train

"""
NSIT Bot main class
"""

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
        
        return self.prediction
        
    

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


