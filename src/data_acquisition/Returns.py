from src.data_acquisition.LoadData import LoadData
import pandas as pd
from tools.logger import logger
from tools.config import load_config

class Returns:
    def __init__(self,config):
        self.config = config
        
    def get_returns(self) -> pd.DataFrame:
        """ Returns from all assets combined """
        try:
            returns = pd.read_csv(self.config['all_data_path'],delimiter=",")
            returns = returns.pct_change().dropna()
            returns.to_csv(self.config['returns_path'],index=0)
            return returns
        except ValueError as ve:
            logger.exception(f"Value Error Occured: {ve}")
        except Exception as e:
            raise e
        
    def get_market_returns(self) -> pd.DataFrame:
        """ Returns from SP&500 """
        try:
            sp500 = pd.read_csv(self.config['sp500_data_path'],delimiter=",")
            market_returns = sp500.pct_change().dropna()
            market_returns.to_csv(self.config['market_returns'],index=0)
            return market_returns
        except FileNotFoundError as fnfe:
            logger.exception(f"Could not find file: {fnfe}")
        except Exception as e:
            raise e
        
        

