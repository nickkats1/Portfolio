from tools.config import load_config
from src.data_acquisition.LoadData import LoadData
from src.financial_models.portfolio_optimization import EfficientDiversification
from src.financial_models.VaR import Var
from src.financial_models.sim import Sim


if __name__ == "__main__":
    config =load_config()
    
    # Load data config
    load_data_config = LoadData(config)
    
    # fetch all prices
    load_data_config.fetch_stock_data()
    
    # Value at Risk Config
    var_config = Var(config)
    # VaR and CVaR
    var = var_config.get_var()
    cvar = var_config.get_cvar()

    
    # Efficient Diversification config
    ef_config = EfficientDiversification(config)
    data = ef_config.fetch_data()
    pf_returns = ef_config.get_portfolio_returns()
    portfolio_metrics = ef_config.portfolio_metrics()

    # single index model config
    sim_config = Sim(config)

    # sp&500 data
    sim_config.fetch_yfinance_data()
    sim_config.single_index_model()
