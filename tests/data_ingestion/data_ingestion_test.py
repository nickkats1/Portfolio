from unittest.mock import patch





# test fetch all prices
def test_fetch_all_prices(data_ingestion_instance,sample_prices):
    """Test 'fetch_all_prices' from DataIngestion module"""
    
    with patch("yfinance.download", return_value=sample_prices) as mock_download:
        sample_prices = data_ingestion_instance.fetch_all_prices()
        assert not sample_prices.empty
        assert "^GSPC" in sample_prices.columns
        assert "AAPL" in sample_prices.columns
        assert "QQQ" in sample_prices.columns
        mock_download.assert_called_once()


# test fetch stock prices
def test_fetch_stock_prices(data_ingestion_instance,sample_prices):
    """Test fetch_stock_prices from DataIngestion class"""
    
    with patch("yfinance.download",return_value=sample_prices) as mock_download:
        sample_prices = data_ingestion_instance.fetch_stocks_prices()
        assert not sample_prices.empty
        assert "AAPL" in sample_prices.columns
        assert "NVDA" in sample_prices.columns
        mock_download.assert_called_once()
        







