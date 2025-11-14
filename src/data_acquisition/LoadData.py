from tools.config import load_config
import yfinance as yf
import pandas as pd
from tools.logger import logger




class LoadData:
    def __init__(self,config):
        self.config = config



    def fetch_data(self):
        """
        fetches 'combined assets' from yfinance api using ticker from .yaml
        """
        try:
            all_prices = yf.download(tickers = self.config['combined_assets'],start=self.config['start_date'],end=self.config['end_date'])['Close']
            
            #drop null values and duplicated values and save to .csv
            all_prices = all_prices.dropna()
            all_prices.drop_duplicates(inplace=True)
            return all_prices
        except ValueError as ve:
            logger.exception(f"value error: {ve}")
        except FileNotFoundError as e:
            raise e
        
    
    def fetch_stock_data(self) -> pd.DataFrame:
        """ fetches all stock data from yfinance """
        try:
            stocks = yf.download(tickers=self.config['stock_tickers'],start=self.config['start_date'],end=self.config['end_date'])['Close']
            #drop null values,duplicates, and save to .csv
            stocks = stocks.dropna()
            stocks.drop_duplicates(inplace=True)
            return stocks
        except ValueError as ve:
            logger.exception(f"Value error: {ve}")
        except FileExistsError as fe:
            logger.exception(f"could not find file: {fe}")
        except Exception as e:
            logger.exception(f"another exception that was not defined: {e}")
        raise None
    
    def fetch_etf_data(self):
        """ fetches etf data from yfinance api"""
        try:
            etfs = yf.download(tickers=self.config['etf_tickers'],start=self.config['start_date'],end=self.config['end_date'])['Close']
            etfs = etfs.dropna()
            etfs.drop_duplicates(inplace=True)
            #save etfs to .csv file
            return etfs
        except ValueError as ve:
            logger.exception(f"Value Error With ETF class: {ve}")
        except FileNotFoundError as fnfe:
            logger.exception(f"file not found error: {fnfe}")
        except Exception as e:
            logger.exception(f"all other error: {e}")
        raise None
        
    
    def fetch_crypto_data(self):
        """
        fetches crypto data from yfinance api
        """
        try:
            crypto = yf.download(tickers=self.config['crypto_tickers'],start=self.config['start_date'],end=self.config['end_date'])['Close']
            crypto = crypto.dropna()
            crypto.drop_duplicates(inplace=True)
            return crypto
        except ValueError as ve:
            logger.exception(f"value error: {ve}")
        except FileNotFoundError as fnfe:
            logger.exception(f"could not find file: {fnfe}")
        except Exception as e:
            logger.exception(f"Other error occured that was not specified: {e}")
        raise None
    
    def fetch_sp500_data(self):
        """Fetches SP&500 data from yfinance api """
        try:
            # ^GPSC is the ticker for SP&500
            sp500 = yf.download(tickers="^GSPC",start=self.config['start_date'],end=self.config['end_date'])['Close']
            #drop duplicates, NAN's, to.csv file
            sp500 = sp500.dropna()
            sp500.drop_duplicates(inplace=True)
            return sp500
        except FileNotFoundError as fnfe:
            logger.exception(f"Could Not Find requested file: {fnfe}")
        except ValueError as ve:
            logger.exception(f"value error occured: {ve}")
        except Exception as e:
            logger.exception(f"other error occured: {e}")
        raise None





