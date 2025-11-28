import pandas as pd
import numpy as np
from tools.config import load_config
from scripts.returns import Returns
from tools.logger import logger
import yfinance as yf

class ValueAtRisk:
    """
    A class for computing the Value at Risk(VaR) && Conditional Value at Risk(CVar).
    for multiple asset returns.
    """
    def __init__(self,config,returns: Returns | None = None):
        self.config = load_config()
        self.returns =returns or Returns(self.config)
        
        
    def get_returns(self) -> pd.DataFrame:
        """
        Fetches data from yfinance api.
        
        Returns:
            returns (pd.DataFrame): dataframe of all_returns from config.yaml from yfinance.
        """
        data = yf.download(self.config['all_prices'],start=self.config['start_date'],end=self.config['end_date'])['Close']
        returns = data.pct_change().dropna()
        return returns
    
    def run_var(self,ci=0.99):
        """
        the value at risk for all of the specified returns in configuration file.
        
        Args:
            ci (float): the confidence interval for the Value at Risk(VaR).
        
        Returns:
            var (float): Value at risk for the returns of the selected tickers.
        """
        returns = self.get_returns()

        value_at_risk = np.percentile(returns,(1 - ci)*100)
        return value_at_risk
    
    def run_cvar(self):
        """
        the conditional value at risk for all returns specified in config.yaml file.
        
        Returns:
            cvar (float): the conditional value at risk
        """

        returns = self.get_returns()

        value_at_risk = self.run_var()
        tail_risk = returns[returns < value_at_risk]
        cvar = np.mean(tail_risk)
        return cvar


