import pytest
from unittest.mock import patch,MagicMock
from src.models.single_index_model import SingleIndexModel
import pandas as pd
import statsmodels.api as sm
import numpy as np


    
    
@pytest.fixture
def single_index_model_instance(sample_config):
    """Instance of SingleIndexModel class"""
    return SingleIndexModel(config=sample_config)



def test_single_index_model_instance(single_index_model_instance):
    """Test single_instance_model instance"""
    assert single_index_model_instance is not None





@pytest.fixture
def mock_sm_ols():
    """Mock OLS model from statsmodels"""
    with patch("src.models.single_index_model.sm.OLS") as mock_ols:
        yield mock_ols


# test 'run' single index model
def test_run(mock_sm_ols,returns_instance,sample_config,sample_returns,sample_prices,data_ingestion_instance):
    """Test 'run' portfolio of SingleIndexModel"""
    
    sample_returns = returns_instance.get_all_returns()
    assert not sample_returns.empty
    
    # dummy tickers for tickers and SP&500 ticker
    
    dummy_sp500_ticker = sample_config["sp500_ticker"]
    
    dummy_tickers = sample_config["all_prices"]
    
    dummy_all_returns = sample_returns[dummy_tickers]
    
    
    assert dummy_sp500_ticker is not None
    assert dummy_tickers is not None
    
    assert not dummy_all_returns.empty
    
    
    # betas, alphas, adjusted betas, error_terms ect
    
    dummy_betas = {}
    dummy_alphas = {}
    dummy_error_terms = {}
    dummy_adjusted_betas = {}
    dummy_systematic_risks = {}
    dummy_firm_specific_risk = {}
    dummy_total_risks = {}
    
    dummy_results = []
    
    for ticker in dummy_tickers:
        dummy_excess_returns = dummy_all_returns[ticker]
        dummy_market_returns = dummy_all_returns[dummy_sp500_ticker]
        
        assert dummy_excess_returns is not None
        assert dummy_market_returns is not None

        # mock single index model
        fake_model = MagicMock()
        fake_model.fittedvalues = pd.Series(
        [101, 103, 106, 104, 108],
        index=pd.date_range("2022-11-24", periods=5)
    )
    fake_model.summary.return_value = "Mocked OLS Summary"
    
    mock_sm_ols = fake_model
    
    X = sm.add_constant(dummy_market_returns)
    y = dummy_excess_returns
    
    fake_model(X,y).fit()
    assert fake_model is not None
    assert fake_model.results is not None
    
    dummy_betas[ticker] = fake_model.params.iloc[1]
    dummy_alphas[ticker] = fake_model.const
    dummy_error_terms[ticker] = fake_model.resid
    dummy_adjusted_betas[ticker] = (2/3) * dummy_betas[ticker] + (1/3) * 1
    
    # fake market risk. Ignore Future warning
    import warnings as w
    warnings = w.simplefilter(action="ignore",category=FutureWarning)
    fake_market_risks = np.var(dummy_market_returns)
    dummy_firm_specific_risk = np.var(sample_returns)
    
    try:
        for warning in warnings:
            if fake_market_risks or dummy_firm_specific_risk == FutureWarning:
                pass
    except Exception as e:
        print(f"other warning or none: {e}")


    dummy_systematic_risks[ticker] = (dummy_betas[ticker]**2) * fake_market_risks
    dummy_total_risks[ticker] = dummy_systematic_risks[ticker] + dummy_firm_specific_risk[ticker]
    model_results = fake_model.summary()
    
    
    # test all dummy dictionaries
    
    assert dummy_betas is not None
    assert dummy_alphas is not None
    assert dummy_error_terms is not None
    assert dummy_adjusted_betas is not None
    assert fake_market_risks is not None
    assert dummy_firm_specific_risk is not None
    assert dummy_total_risks is not None
    assert model_results is not None
    
    dummy_results = ({
    "alphas":dummy_alphas,
    "betas":dummy_betas,
    "adjusted_betas": dummy_adjusted_betas,
    "systematic_risks": dummy_systematic_risks,
    "firm_specific_risks": dummy_firm_specific_risk,
    "market_index_risk": fake_market_risks,
    "total_risks": dummy_total_risks
    })
    
    assert dummy_results is not None
    assert "alphas" in dummy_results.keys()
    assert dummy_alphas in dummy_results.values()
    assert dummy_alphas in dummy_results.values() is not None
    
    # testing if betas are in dummy_results
    assert "betas" in dummy_results.keys()
    assert dummy_betas in dummy_results.values()
    assert dummy_betas in dummy_results.values() is not None
    
    assert "adjusted_betas" in dummy_results.keys()
    assert dummy_adjusted_betas in dummy_results.values()
    assert dummy_adjusted_betas in dummy_results.values() is not None
    
    assert "systematic_risks" in dummy_results.keys()
    assert dummy_systematic_risks in dummy_results.values()
    assert dummy_systematic_risks in dummy_results.values() is not None
    mock_sm_ols.assert_called_once()
    

    

    
    
    



    
    
    




    
    




    

