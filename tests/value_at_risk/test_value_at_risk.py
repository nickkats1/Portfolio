import pytest
from src.models.value_at_risk import ValueAtRisk
import pandas as pd
import numpy as np

@pytest.fixture
def value_at_risk_instance(sample_config):
    return ValueAtRisk(config=sample_config)



def test_value_at_risk_instance(value_at_risk_instance,sample_config):
    """Test instance of value at risk"""
    assert value_at_risk_instance is not None

    

def test_run_var(sample_config,sample_returns,value_at_risk_instance):
    """Test 'run_var' from ValueAtRisk instance"""
    all_returns = sample_returns
    assert all_returns is not None
    assert isinstance(all_returns,pd.DataFrame)
    
    sample_var = np.percentile(all_returns,(1-0.99)*100)
    
    assert sample_var is not None
    
     
    tail_risk = all_returns[all_returns < sample_var]

    sample_cvar = np.mean(tail_risk)
    assert sample_cvar != sample_var
    assert sample_cvar is not None
    assert sample_cvar < sample_var
    
    
    


