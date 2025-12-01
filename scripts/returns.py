import pandas as pd
from tools.config import load_config

class Returns:
    """
    A utility class for computing percentage returns for various datasets 
    defined in the project's configuration file.
    """

    def __init__(self,config: dict):
        """
        Initialize the Returns object.

        Args:
            config (dict): Configuration file containing file paths and tickers.
        """
        self.config = load_config()


    def get_all_returns(self) -> pd.DataFrame:
        """
        Compute percentage returns for all assets listed in the
        'all_prices_path' in config.yaml.

        Returns:
            pd.DataFrame: DataFrame containing percent changes of all assets.
        """
        all_prices = pd.read_csv(self.config["all_prices_path"],delimiter=",")
        returns = all_prices.pct_change().dropna()
        return returns

    def get_stock_returns(self) -> pd.DataFrame:
        """
        Compute percentage returns for stocks listed in the 
        'stock_prices_path' in config.yaml.

        Returns:
            pd.DataFrame: DataFrame containing percent changes of stock prices.
        """
        stocks = pd.read_csv(self.config['stock_prices_path'],delimiter=",")
        stock_returns = stocks.pct_change().dropna()
        return stock_returns

    def get_etf_returns(self) -> pd.DataFrame:
        """
        Compute percentage returns for ETFs listed in the 
        'etf_prices_path' in config.yaml.

        Returns:
            pd.DataFrame: DataFrame containing percent changes of ETF prices.
        """
        etf = pd.read_csv(self.config['etf_prices_path'],delimiter=",")
        etf_returns = etf.pct_change().dropna()
        return etf_returns

    def get_sp500_returns(self) -> pd.DataFrame:
        """
        Compute percentage returns for the S&P 500 index listed in the 
        'sp500_prices_path' in config.yaml.

        Returns:
            pd.DataFrame: DataFrame containing percent changes of S&P 500 prices.
        """
        sp500 = pd.read_csv(self.config["sp500_prices_path"],delimiter=",")
        sp500_returns = sp500.pct_change().dropna()
        return sp500_returns
