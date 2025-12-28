import numpy as np

from tools.config import load_config

from scripts.returns import Returns


class ValueAtRisk:
    """
    A class for computing the Value at Risk(VaR) && Conditional Value at Risk(CVar).
    for multiple asset returns.
    """
    def __init__(self, config: dict, returns: Returns | None = None):
        self.config = config or load_config()
        self.returns = returns or Returns(self.config)
        
        

    def run_var(self,ci=0.99) -> float:
        """
        the value at risk for all of the specified returns in configuration file.
        
        Args:
            ci (float): the confidence interval for the Value at Risk(VaR).
        
        Returns:
            var (float): Value at risk for the returns of the selected tickers.
        """
        all_returns = self.returns.get_all_returns()

        value_at_risk = np.percentile(all_returns,(1 - ci)*100)
        print(f"Value at Risk (VaR): {value_at_risk:.4f}")
        return value_at_risk
    
    def run_cvar(self) -> float:
        """
        the conditional value at risk for all returns specified in config.yaml file.
        
        Returns:
            cvar (float): the conditional value at risk
        """

        all_returns = self.returns.get_all_returns()

        value_at_risk = np.percentile(all_returns,(1-.99)*100)
        tail_risk = all_returns[all_returns < value_at_risk]
        cvar = np.mean(tail_risk)
        return cvar



