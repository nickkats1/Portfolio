import numpy as np
from scripts.returns import Returns
from tools.config import load_config
import pandas as pd

class Utility:
    """
    A class to Maximize Utility of the Expected returns:
    u = E(r) - A * 1/2 * var(r)
    """
    def __init__(self,config: dict, returns: Returns | None = None):
        """
        Initialize Utility object.
        Args:
            config (dict): config.py file.
            data_ingestion(DataIngestion): class used to fetch data from yfinance API.
        
        Returns:
            U (float): utility of the investor.
        """
        self.config = config or load_config()
        self.returns = returns or Returns(config)
        
    def run(self) -> pd.Series:
        """
        Run utility module.
        
        Returns:
            u (pd.Series): the utility of the investor based on A, expected returns, and risk(var).
        """
        # closing prices
        returns = self.returns.get_stock_returns()
        
        # expected returns from pyportfolio library.
        
        er = np.mean(returns)
        
        # variance
        var = np.var(returns)
        
        # A is the investors level of risk aversion. if A > 0: Risk-Adverse, A == 0; Risk-Neutral, A < 0; Risk-Loving
        
        
        
        # set A == 3.0 for risk-adverse investors because most investors are risk-adverse
        A = 3.0
        
        
        # utility function
        u = er - (0.5) * A * var
        

        print(f"investors level of risk aversion: {u}")
        return u
