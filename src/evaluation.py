import logging
from abc import ABC, abstractmethod
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd 
from zenml import step

class Evaluate(ABC):


    @abstractmethod
    def calculate_score(self, y_true:np.ndarray, y_pred: np.ndarray):
        pass


class MSE(Evaluate):

    
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating MSE")
            mse = mean_squared_error(y_true, y_pred)
            logging.info("The mean squared error value is: " + str(mse))
            return mse
        except Exception as e:
            logging.error("Error in calculating MSE: {}".format(e))
            raise e 

class R2(Evaluate):

    def calculate_score(self, y_true:np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating R2 Score")
            r2= r2_score(y_true, y_pred)
            logging.info("R2 Score: {}".format(r2))
            return r2
        except Exception as e:
            logging.error("Error in calculating R2 Score: {}".format(e))
            raise e 
        

class RMSE(Evaluate):
    def calculate_score(self,y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating RMSE")
            rmse = mean_squared_error(y_true, y_pred, squared=False)
            logging.info("RMSE:{}".format(rmse))
            return rmse
        except Exception as e:
            logging.error("Error in calculating RMSE: {}".format(e))
            raise e 