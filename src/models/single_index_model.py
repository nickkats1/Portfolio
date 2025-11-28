import statsmodels.api as sm
import pandas as pd
from tools.config import load_config
import numpy as np

class SingleIndexModel:
    """
    Single Index Model (SIM) implementation:
    r_i = alpha_i + beta_i * r_m + ε_i
    """
    def __init__(self,config):
        self.config = config
    
    def run(self):
        """
        Run the single index model for all assets.
        
        Returns:
            A OLS model of all assets compared against SP&500
        """
        # all asset returns
        all_returns = pd.read_csv(self.config['all_returns'],delimiter=",")
        
        tickers = self.config['all_prices']
        sp500_ticker = self.config['sp500_ticker']
        results = []
        
        for ticker in tickers:
            returns = all_returns[ticker]
            market_returns = all_returns[sp500_ticker]
            
            model = sm.OLS(exog=sm.add_constant(market_returns),endog=returns).fit()
            
            
            # dictionary to store beta, alpha, systematic risk, total risk, etc
            results.append({
                "model":model,
                "alpha": model.params.const,
                "beta": model.params.iloc[1],
                "residuals":model.resid,
                "adjusted beta":(2/3) * model.params[1] + (1/3) * 1,
                "firm-specific risk": np.var(model.resid),
                "market_index_risk": np.var(market_returns)
            })
            
            
    
                
            
            
        return results