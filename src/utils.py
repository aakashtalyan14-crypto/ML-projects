import os 
import sys 
import numpy as np 
import pandas as pd

from sklearn.metrics import r2_score

import dill

from src.exception import CustomException
from src.logger import logging


def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    
    except Exception as e :
        logging.error("Error in saving object")
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        
        for i in range(len(models)):
            model=list(models.values())[i]  # get the model 
            model.fit(X_train,y_train) # Train Model
            
            y_train_pred=model.predict(X_train) # predict on training data
            y_test_pred = model.predict(X_test) # predict on test data
            
            train_model_score=r2_score(y_train,y_train_pred) # evaluate model on training data
            test_model_score=r2_score(y_test,y_test_pred) # evaluate model on test data
            
            report[list(models.keys())[i]]=test_model_score # add the model score to report 
        
        return report 
    except Exception as e:
        logging.error("Error in evaluating model")
        raise CustomException(e,sys)
        
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        logging.error("Error in loading object")
        raise CustomException(e,sys)