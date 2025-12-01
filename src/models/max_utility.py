from tools.config import load_config
from scripts.returns import Returns
from typing import List
import numpy as np

class MaxUtility:
    """
    Class for maximizing utility.
    Max (u) = rf + y*[E(rp) - rf] - (1/2) * A * y**2 * var(portfolio)
    """
    def __init__(self,config,returns: Returns | None = None):
        self.config = load_config()
        self.returns = returns or Returns(self.config)
        
        
    def run(self) -> List[float]:
        """
        The utility of the investor with optimized utility.
        
        Returns:
            U (List[float]): list of investors utility level for each asset class.
        """
        stock_returns = self.returns.get_all_returns()
        
        # expected returns
        er = np.mean(stock_returns)
        
        # risk-free-rate
        risk_free_rate = self.config['risk_free_rate']
        
        # variance of returns
        var = np.var(stock_returns)
        
        # set A = 3.0
        A = 3.0
        
        y_star = (er - risk_free_rate) / (A * var)
        
        # maximize U
        
        max_u = risk_free_rate + y_star * (er - risk_free_rate) - (0.5) * A * y_star**2 * var
        print(f"Max Utils: {max_u}")
        
        
        return max_u
        
        

