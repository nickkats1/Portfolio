import pytest
from unittest.mock import patch
import pandas as pd
from src.data_acquisition.LoadData import LoadData

SAMPLE_CONFIG = {
    "start_date": "2020-10-10",
    "end_date": "2020-10-20",
    "stock_tickers": ["AAPL", "MSFT", "TGT"],
    "etf_tickers": ["QQQ", "SPY", "VTI"],
    "crypto_tickers": ["BTC-USD", "ETH-USD", "SOL-USD"],
    "combined_assets": ["AAPL", "MSFT", "TGT", "QQQ", "SPY", "VTI", "BTC-USD", "ETH-USD", "SOL-USD"],
    "risk_free_rate": 0.0005
}

@pytest.fixture
def load_data_instance():
    return LoadData(SAMPLE_CONFIG)



            

def test_fetch_data(load_data_instance):
    """ mock fetch data """
    mock_all_prices = pd.DataFrame({
        "AAPL": [100, 120, 130],
        "^GSPC": [30, 23, 235],
        "QQQ": [54, 452, 245],
        "BTC-USD":[325523,325235,2365],
        
    }, index=pd.to_datetime(pd.date_range(start=SAMPLE_CONFIG['start_date'], periods=3)))
    mock_all_prices = pd.concat({"Close": mock_all_prices}, axis=1)

    with patch("yfinance.download", return_value=mock_all_prices) as mock_download:
        all_prices = load_data_instance.fetch_data()
        assert not all_prices.empty
        assert "^GSPC" in all_prices.columns
        assert "AAPL" in all_prices.columns
        assert "BTC-USD" in all_prices.columns
        assert "QQQ" in all_prices.columns
        mock_download.assert_called_once()




    

    
    
    




