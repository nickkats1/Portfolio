import pandas as pd
from pypfopt import expected_returns,EfficientFrontier,risk_models


class MPT:
    """
    A class for portfolio optimization using Modern
    Portfolio Theory.
    """
    def __init__(self,config):
        """
        Initialize Markowitz object.
        
        Args:
            config (yaml): a configuration file containing paths to CSV
            files with needed data.
        """
        self.config = config
        

    def run(self):
        """Run Markowitz portfolio optimization."""
        data = pd.read_csv(self.config['all_prices_path'],delimiter=",")
        
        # Expected Returns, Volatility, Sharpe Ratio
        mu = expected_returns.mean_historical_return(data)
        S = risk_models.sample_cov(data)
        ef = EfficientFrontier(mu,S)
        
        # save mu,S, Efficient Frontier to .csv
        



        weights = ef.max_sharpe()
        weights = ef.clean_weights()
    

            
        expected_annual_return, annual_volatility, sharpe_ratio = ef.portfolio_performance(verbose=False)
        performance = {
            "Expected Annual Return":expected_annual_return,
            "Annual Volatility":annual_volatility,
            "Sharpe Ratio":sharpe_ratio
        }
        
        return mu,S,weights,performance