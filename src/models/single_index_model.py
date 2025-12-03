from scripts.returns import Returns
from tools.config import load_config
import numpy as np
import statsmodels.api as sm
from scripts.returns import Returns
from typing import Any,Dict,List



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
        self.config = config or load_config()
        self.returns = returns or Returns(self.config)
        
    def run(self) -> List[Dict[str, Dict[str, np.float64]]]:
        """
        OLS of returns between individual assets and the SP&500.
        
        Returns:
            results (List[Dict[str, Dict[str, np.float64]]]): a list the appends the alphas, betas, systematic risks ect. for all firms against the SP&500.
        """
        # all_returns and market_returns
        
        all_returns = self.returns.get_all_returns()
        tickers = self.config['all_prices']
        sp500_ticker = self.config['sp500_ticker']
        
        #betas,alpha,residuals
        
        betas = {}
        alphas = {}
        error_terms = {}
        adjusted_betas = {}
        systematic_risks = {}
        firm_specific_risks = {}
        total_risks = {}


        results = []

        for ticker in tickers:
            asset_returns = all_returns[ticker]
            market_returns = all_returns[sp500_ticker]
            X = sm.add_constant(market_returns)
            y = asset_returns
            model = sm.OLS(exog=X,endog=y).fit()
            alphas[ticker] = model.params.const
            betas[ticker] = model.params.iloc[1]
            error_terms[ticker] = model.resid
    
            # adjusted betas
            adjusted_betas[ticker] = (2/3) * betas[ticker] + (1/3) * 1
    
    
            # market index risk
            market_index_risk = np.var(market_returns)
    
            # firm-specific risk
            firm_specific_risks[ticker] = np.var(asset_returns)
    
            # Systematic Risk
            systematic_risks[ticker] = (betas[ticker]**2) * market_index_risk
    
            # total risk
            total_risks[ticker] = systematic_risks[ticker] + firm_specific_risks[ticker]
    
            results.append({
                "betas":betas,
                "alphas":alphas,
                "adjusted betas": adjusted_betas,
                "systematic risk's": systematic_risks,
                "Firm-Specific Risk's": firm_specific_risks,
                "market-index-risk":market_index_risk,
                "total-risks":total_risks
            })
    
        
        return results

    
