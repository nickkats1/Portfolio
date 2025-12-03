import pytest

import pandas as pd

from scripts.data_ingestion import DataIngestion

from scripts.returns import Returns





@pytest.fixture
def sample_config():
    return {
    "start_date":"2020-11-24",
    "end_date": "2020-12-01",
    "all_prices": ["^GSPC","AAPL","QQQ"],
    "stock_tickers": ["AAPL","NVDA"],
    "etf_tickers": ["QQQ","SPY"],
    "sp500_ticker":"^GSPC",
    "all_prices_path": "data/raw/all_prices.csv",
    "risk_free_rate": 0.001
    }


@pytest.fixture
def sample_prices(sample_config):
    """Sample Prices DataFrame"""
    mock_all_prices = pd.DataFrame({
    "^GSPC": [3635.41,3629.65,3638.35,3621.63,3662.45],
    "AAPL": [112.11,112.95,113.95,115.89,119.46],
    "QQQ": [285.61,287.37,290.02,290.61,294.33],
    "NVDA": [12.76, 23.01, 26.11, 31.01, 44.11],
    "SPY": [338.093689,338.615753,339.035278,337.534363,341.226074]
  }, index=pd.to_datetime(pd.date_range(start=sample_config['start_date'], periods=5)))
    mock_all_prices = pd.concat({"Close": mock_all_prices}, axis=1)
    return mock_all_prices


@pytest.fixture
def sample_returns(sample_config):
    """Sample Returns dataframe"""
    mock_all_returns = pd.DataFrame({
        "^GSPC": [0.16121,-0.001584,0.002397,-0.004596,0.01271],
        "AAPL": [0.011594,0.007467,0.004826,0.02100,0.030827],
        "QQQ": [0.014050,0.006147,0.009214,0.002040,0.012816],
        "NVDA": [0.002002,0.010576,-0.000858,0.003992,0.011539],
        "SPY": [-0.001542,0.002785,-0.004427,0.010937,0.002104]
    },index=pd.to_datetime(pd.date_range(start=sample_config['start_date'],periods=5)))
    mock_all_returns = pd.concat({"Close": mock_all_returns}, axis=1)
    return mock_all_returns





@pytest.fixture
def data_ingestion_instance(sample_config):
    """DataIngestion Instance"""
    return DataIngestion(config=sample_config)


@pytest.fixture
def returns_instance(sample_config):
    """Returns Instance"""
    return Returns(config=sample_config)










