from tools.config import load_config

from scripts.data_ingestion import DataIngestion
from scripts.returns import Returns
from src.models.max_utility import MaxUtility
from src.models.mpt import MPT
from src.models.single_index_model import SingleIndexModel
from src.models.utility import Utility


def main():
    """Main function"""

    # config
    config = load_config()

    # data ingestion
    data_ingestion = DataIngestion(config)

    # all prices from DataIngestion
    all_prices = data_ingestion.fetch_all_prices()

    # etf prices from data ingestion
    etf_prices = data_ingestion.fetch_etf_prices()

    # stock prices from data_ingestion

    stock_prices = data_ingestion.fetch_stocks_prices()

    # sp500 prices
    sp500 = data_ingestion.fetch_sp500_prices()

    # returns

    returns = Returns(config)

    # all returns

    all_returns = returns.get_all_returns()

    # stock returns

    stock_returns = returns.get_stock_returns()

    # etf returns

    etf_returns = returns.get_etf_returns()

    # sp&500 returns

    sp500_returns = returns.get_sp500_returns()

    # Utility
    utility_obj = Utility(config)

    # run utility
    utility_obj.run()

    # max utility

    max_utility_obj = MaxUtility(config)

    # run max utility

    max_utility_obj.run()

    # MPT instance

    mpt_obj = MPT(config)
    mpt_obj.portfolio_metrics()

    # single index model

    sim_obj = SingleIndexModel(config)

    # run single index model to get dictionary of financial metrics
    sim = sim_obj.run()
    sim


if __name__ == "__main__":
    main()
