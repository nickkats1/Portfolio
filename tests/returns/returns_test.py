from scripts.returns import Returns
import pandas as pd



def test_get_all_returns(sample_returns,sample_config,returns_instance):
    """Test all returns."""
    
    mock_all_returns = sample_returns
    print(mock_all_returns.head(10))
    assert not mock_all_returns.empty
    assert isinstance(mock_all_returns,pd.DataFrame)

 


