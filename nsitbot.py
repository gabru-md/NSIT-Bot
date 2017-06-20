
from trainer import trainer as Train

"""
NSIT Bot main class
"""

class NSITBot(object):
    def __init__(self,**kwargs):
        
        self.__name__ = kwargs.get('name','NSITBot')
        
        self.__owner__ = kwargs.get('owner','NSIT 2020')
        
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
        
        



