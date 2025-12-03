import yfinance as yf
import pandas as pd
from tools.config import load_config

class DataIngestion:
    """
    A class for downloading data from yfinance api
    and saving it to a .csv files as defined in config.yaml file.
    """
    
    def __init__(self,config: dict):
        """
        Initialize the DataIngestion object.
        
        Args:
            config (dict): configuration file containing dates, tickers, and file paths
        """
        self.config = config or load_config()
        
    def fetch_all_prices(self) -> pd.DataFrame:
        """
        Fetch all price data as defined in the configuration file
        under the name 'all_prices'.
        
        Returns:
            pd.Dataframe consisting of cleaned closing price data from yfinance  
        """

        all_prices = yf.download(tickers=self.config['all_prices'],start=self.config['start_date'],end=self.config['end_date'])['Close']
        all_prices = all_prices.dropna()
        all_prices.drop_duplicates(inplace=True)
        return all_prices
        
    def fetch_stocks_prices(self) -> pd.DataFrame:
        """
        Fetch all closing prices for 'stock tickers'
        as defined in config.yaml file
        
        Returns:
            pd.Dataframe: Dataframe containing cleaned closing prices
        """
        stocks = yf.download(tickers=self.config['stock_tickers'],start=self.config['start_date'],end=self.config['end_date'])['Close']
        stocks = stocks.dropna()
        stocks.drop_duplicates(inplace=True)
        return stocks
        
    def fetch_etf_prices(self) -> pd.DataFrame:
        """
        Fetch all closing prices for 'etf_tickers'
        as defined in the configuration file.
        
        Returns:
            pd.Dataframe: Dataframe containing closing etf prices.
        """
        etfs = yf.download(tickers=self.config['etf_tickers'],start=self.config['start_date'],end=self.config['end_date'])['Close']
        etfs = etfs.dropna()
        etfs.drop_duplicates(inplace=True)
        return etfs

        
        
    def fetch_sp500_prices(self) -> pd.DataFrame:
        """
        Fetches closing prices for 'sp500_tickers'
        as defined in the configuration file.
        
        Returns:
            pd.Dataframe: Dataframe consisting of sp500 closing prices.
        """
        sp500 = yf.download(tickers=self.config['sp500_ticker'],start=self.config['start_date'],end=self.config['end_date'])['Close']
        sp500 = sp500.dropna()
        sp500.drop_duplicates(inplace=True)
        return sp500
