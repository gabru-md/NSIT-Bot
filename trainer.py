"""
NSIT-Bot
--------
training class for NSIT Bot
"""
import sys

import os

from pandas import DataFrame

import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB



class trainer(object):
    """
    A Trainer class which contains methods
    to train the NSIT Bot on the training
    dataset as provided with the module.
    
    The training dataset can also be created
    depending upon the user.
    """
    
    def __init__(self,name):

        """
        initialize the trainer with a name.
        """
        self.train = True
        
        
        """
        'path' variable must be the path to some 
        folder which contains the .trainer files
        with appropriate names.
        """
        
        #path = kwargs.get('path','trainer')
        

        """
        now we will call the training data.
        in simple terms : we will now train.
        """
        
               
    
    def getTrainingData(self,path):
        """
        function to fetch training data from 
        .trainer files located inside folder
        
        Checking for each training file 
        """
        #os.chdir('C:\Users\Manish\Desktop\NSIT-Bot\Bot')
        self.old_loc = os.getcwd()
        
        new_loc = os.getcwd() + "/" + path
        
        os.chdir(new_loc)
        list_trainer_files = os.listdir(new_loc)
        dataList = []
        
        for files in list_trainer_files:

            chk_extension = files.split('.')
            if len(chk_extension) > 1 and chk_extension[-1] == 'trainer':
                with open(files) as trainer_file:
                    data = trainer_file.readlines()
                for line in data:
                    dataList.append({'message':line.replace('\n',''),'class':chk_extension[0]})
        
        return dataList
                
                
        
    def trainWith(self,path):
        """
        method to take the path to .trainer
        files.
        Basically the 'trainer' folder that
        containes the .trainer files to be trained.
        
        Finally a pandas.core.frame.DataFrame object 
        is returned
        """
        dataList = self.getTrainingData(path)
        return DataFrame(dataList)
        
        

    def getClassifier(self,**kwargs):
        """
        returns a vectorizer to predict the query
        """

        self.path = kwargs.get('path','trainer')
        self.df = self.trainWith(self.path)
        
        
        self.vectorizer = CountVectorizer() 

        counts = self.vectorizer.fit_transform(self.df['message'].values)

        self.classifier = MultinomialNB()
        
        targets = self.df['class'].values
        self.classifier.fit(counts, targets) 
        

        os.chdir(self.old_loc)
        return self.classifier,self.vectorizer

