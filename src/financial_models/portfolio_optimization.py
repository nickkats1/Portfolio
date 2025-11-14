import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from tools.config import load_config
import numpy as np
from pypfopt import expected_returns,EfficientFrontier,risk_models
from src.financial_models.VaR import Var

class EfficientDiversification:
    def __init__(self,config):
        self.config = config


        
    def fetch_data(self) -> pd.DataFrame:
        """Loads in data from yfinance using config.yaml"""
        try:
            all_prices = pd.read_csv(self.config['all_data_path'],delimiter=",")
            return all_prices
        except Exception as e:
            raise e 
        
    
    def get_portfolio_returns(self) -> pd.DataFrame:
        """ returns from portfolio from yfinance download """
        try:
            # load in all prices
            all_prices = self.fetch_data()
            returns = all_prices.pct_change().dropna()
            return returns
        except Exception as e:
            raise e
        

    
    
    def portfolio_metrics(self):
        """
        args:
            (mu) -> Expected Returns (using pyportfolio)
            (S) -> Risk(Volatility);
            (Ef) -> Efficient Frontier;
        """

        #all prices
        all_prices = self.fetch_data()

        mu = expected_returns.mean_historical_return(all_prices)
        S = risk_models.sample_cov(all_prices)
        ef = EfficientFrontier(mu,S)
        
        # save mu,S, Efficient Frontier to .csv
        
        mu.to_csv(self.config['expected_returns_path'],index=0)
        S.to_csv(self.config['volatility_path'],index=0)


        weights = ef.max_sharpe()
        weights = ef.clean_weights()
    

            
        expected_annual_return, annual_volatility, sharpe_ratio = ef.portfolio_performance(verbose=False)
        performance = {
            "Expected Annual Return":expected_annual_return,
            "Annual Volatility":annual_volatility,
            "Sharpe Ratio":sharpe_ratio
        }
        
        return mu,S,weights,performance
