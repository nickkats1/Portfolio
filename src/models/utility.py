import numpy as np


from scripts.returns import Returns


from tools.config import load_config


import pandas as pd


class Utility:
    """A class to Maximize Utility of the Expected returns:
    U = E(r) - A * 1/2 * var(r).
    """
    
    
    def __init__(self, config: dict, returns: Returns | None=None):
        """__init__ Utility class.

        Args:
            config (dict): config.py from config.yaml consisting of tickers and file paths.
            returns (Returns | None, optional): Returns module to fetch market returns from yfinance.
        
        Returns:
            U (pd.Series): Utility of the individuals risk-aversion.
        """
        
        self.config = config or load_config()
        self.returns = returns or Returns(self.config)
        
        
    def run(self, A=3.0) -> pd.Series:
        """Run Utility class.
        
        Args:
            A (float): The level of the investors risk-aversion.
        
        
        Returns:
            U (pd.Series): A series of Utility values based on expected returns, risk, risk-aversion and scaling factor.
        """
        
        # returns from 'Returns' object
        returns = self.returns.get_all_returns()
        
        # Expected Returns
        
        er = np.mean(returns)
        
        # Variance (Volatility) or returns.
        
        var = np.var(returns)
        
        # Utility function
        
        U = er - (0.5) * A * var
        
        print(f"Utility derived from returns and risk: {U}")
        
        return U