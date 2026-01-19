from tools.config import load_config


from pypfopt import expected_returns, EfficientFrontier, risk_models


from scripts.data_ingestion import DataIngestion


from typing import Any, Dict

class MPT:
    """Modern Portfolio Theory class."""

    
    def __init__(self,config: dict, data_ingestion: DataIngestion | None = None):
        """
        Initializing class for Modern Portfolio Theory.
        
        Args:
            config (dict): configuration file.
            data_ingestion (DataIngestion): DataIngestion module to extract data from yfinance API.
        
        """
        self.config = config or load_config()
        self.data_ingestion = data_ingestion or DataIngestion(self.config)

    
    
    def portfolio_metrics(self) -> Dict[str,Any]:
        """
        Metrics for portfolio optimization using pyportfolioopt.

        Returns:
            Performance (Dict[str,Any]): a dictionary containing a list of items with weights, Expected Returns, Volatility,
            Efficient Frontier, and the sharpe ratio
        """
        # data from data ingestion
        all_prices = self.data_ingestion.fetch_all_prices()
        

        mu = expected_returns.mean_historical_return(all_prices)
        S = risk_models.sample_cov(all_prices)
        ef = EfficientFrontier(mu,S)
            

        weights = ef.max_sharpe()
        weights = ef.clean_weights()


            
        expected_annual_return, annual_volatility, sharpe_ratio = ef.portfolio_performance(verbose=True)
        performance = {
            "weights": weights,
            "expected_annual_return":expected_annual_return,
            "Annual Volatility":annual_volatility,
            "Sharpe Ratio":sharpe_ratio
        }
        return performance