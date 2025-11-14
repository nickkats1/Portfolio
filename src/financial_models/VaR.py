import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tools.config import load_config
import yfinance as yf
import numpy as np
from tools.logger import logger


class Var:
    def __init__(self,config):
        self.config = config


        
    def load_returns(self):
        """ read in returns from path """
        try:
            returns  = pd.read_csv(self.config['returns_path'],delimiter=",")
            return returns
        except FileNotFoundError as fnfe:
            logger.exception(f"File Not Found Error: {fnfe}")
        except ExceptionGroup as e:
            logger.exception(f"Other Exception which was not called: {e}")
        raise None

    
    def get_var(self,ci=0.95):
        """
        value at risk
        """
        #returns
        returns = self.load_returns()

        value_at_risk = np.percentile(returns,(1 - ci)*100)
        return value_at_risk
    
    def get_cvar(self):
        """
        Conditional Value at Risk
        """

        returns = self.load_returns()

        value_at_risk = self.get_var()
        tail_risk = returns[returns < value_at_risk]
        cvar = np.mean(tail_risk)
        return cvar






