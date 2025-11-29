from scripts.returns import Returns
from tools.config import load_config
import numpy as np
import statsmodels.api as sm
from scripts.returns import Returns
import matplotlib.pyplot as plt
from typing import Any
import seaborn as sns


class SingleIndexModel:
    """
    Single Index Model (SIM) implementation:
    r_i = alpha_i + beta_i * r_m + ε_i
    """
    def __init__(self,config, returns: Returns | None = None):
        """
        initializing SingleIndexModel class.
        
        Args:
            config(dict): configuration.py.
            returns (Returns): Returns module.
        """
        self.config = load_config()
        self.returns = returns or Returns(self.config)
        
    def single_index_model(self) -> Any:
        """
        OLS of returns between individual assets and the SP&500.
        
        Returns:
            model (sm.OLS): a statsmodels object consisting of every ticker in the config.yaml
            compared against the SP&500.
        """
        # all_returns and market_returns
        
        all_returns = self.returns.get_all_returns()
        tickers = self.config['all_prices']
        sp500_ticker = self.config['sp500_ticker']
        
        #betas,alpha,residuals
        
        betas = {}
        alphas = {}
        error_terms = {}
        
        
        
        # market risk
    
        
        
        for ticker in tickers:
            asset_returns = all_returns[ticker]
            market_returns = all_returns[sp500_ticker]

            X = sm.add_constant(market_returns)
            y = asset_returns
            model = sm.OLS(exog=X,endog=y).fit()
            alphas[ticker] = model.params.const
            betas[ticker] = model.params.iloc[1]
            error_terms[ticker] = model.resid
            # market risk
            market_risk = np.var(market_returns)
            systematic_risk = (betas[ticker]**2) * market_risk
            
            firm_specific_risk = np.var(error_terms[ticker])
            total_risks = firm_specific_risk + systematic_risk
            
            
            print(f"\n ticker: {ticker}")
            print(model.summary())
            print(f"Alphas: {alphas}")
            print(f"Betas: {betas}")
            print(f"market_risk: {market_risk}")
            print(f"Total Risks: {total_risks}")
            print(f"systematic_risk: {systematic_risk}")
            
            # plot of Single Index Model
            plt.figure(figsize=(12,6))
            sns.scatterplot(x=market_returns, y=asset_returns, label=ticker)
            sns.lineplot(x=market_returns, y=model.fittedvalues, color='red', label='Security Market Line')
                
            plt.title(f'Single Index Model for {ticker}')
            plt.xlabel('Market Excess Return')
            plt.ylabel(f'{ticker} Excess Return')
            plt.legend()
            plt.show()

            

            
        return model

            
    
    
