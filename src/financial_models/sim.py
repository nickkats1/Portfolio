import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
from tools.config import load_config
import numpy as np
from pypfopt import expected_returns
import os
import yfinance as yf

class Sim:
    RISK_FREE_RATE = 0.0005
    def __init__(self,config):
        self.config = config


    def fetch_yfinance_data(self) -> pd.DataFrame:
        """ Fetch Data from yfinance API """
        
        # all prices include SP&500
        all_prices = yf.download(tickers=self.config['combined_assets'],start=self.config['start_date'],end=self.config['end_date'])['Close']
        all_prices = all_prices.dropna()
        all_prices.drop_duplicates(inplace=True)

        return all_prices


    def single_index_model(self,output_dir="images/sim/"):

        #tickers to turn data into correct frame
        all_prices = self.fetch_yfinance_data()

        sp500_ticker = self.config['sp500_ticker']
        tickers = self.config['combined_assets']


        # sp500 data
        sp500_data = all_prices[sp500_ticker]
        # Market Returns(sp500) and Market Excess Returns
        market_returns = sp500_data.pct_change().dropna()
        #market index risk is of the sp500(variance(sp500))
        market_index_risk = np.var(market_returns)
        print(f'Market Index Risk: {market_index_risk}')




        # alphas, betas, total risk, covariance, market index risk,firm specific risk,product of betas
        alphas = {}
        betas = {}
        error_terms = {}
        adjusted_betas = {}
        firm_specific_risks = {}
        systematic_risks = {}
        total_risks = {}
        risk_premiums = {}
        Expected_Returns = {}
    







        for ticker in tickers:
            asset_data = all_prices[ticker]
            returns = asset_data.pct_change().dropna()
            Excess_Returns = asset_data.pct_change().dropna() - self.RISK_FREE_RATE
            print(f'Returns for: {ticker}, {returns}')
            print(f'Excess Returns: {Excess_Returns}')
            print(f'Market Returns: {sp500_ticker},{market_returns};-----')
            
            # CAPM expected returns
            capm_returns = expected_returns.capm_return(asset_data,market_prices=sp500_data,risk_free_rate=self.config['risk_free_rate'])
            


            model = sm.OLS(exog=sm.add_constant(market_returns),endog=returns).fit()
            

            # alpha, beta, error-term (e), firm-specific risk(variance(e)), market risk(variance of sp500 in this case).
            # risk premium: E(R) - Rf
            alpha = model.params.const
            beta = model.params.iloc[1]
            residuals = model.resid
            




            # adjusted beta: 2/3 * beta + 1/3 * 1
            adj_beta = (2/3) * beta + (1/3) * 1


            # Systematic risk is (Beta**2) * Market Index Risk (defined above)
            systematic_risk = (beta**2) * market_index_risk

            #  firm-specific risk is the variance of the "Unanticipated surprises" (the variance of the residuals for the asset)
            firm_specific_risk = np.var(residuals)

            # total risk = systematic Risk + Firm Specific Risk
            total_risk = systematic_risk + firm_specific_risk






            alphas[ticker] = alpha
            betas[ticker] = beta
            error_terms[ticker] = residuals
            adjusted_betas[ticker] = adj_beta
            systematic_risks[ticker] = systematic_risk
            firm_specific_risks[ticker] = firm_specific_risk
            total_risks[ticker] = total_risk
            
            # values to .csv


            print(f"CAPM Returns: {capm_returns}")
            print(f'Alpha Value: {alpha:.4f}')
            print(f'Beta Value: {beta:.4f}')
            print(f'Adjusted Beta: {adj_beta:4f}')
            print(f'Firm Specific Risk: {firm_specific_risk:.4f}')
            print(f'Systematic Risk: {systematic_risk:.4f}')
            print(f'Total Risk: {total_risk}')
            print(f'Error Term: {residuals}')

            


        

            # E(r) -> The Expected Return using pyportfolio & Risk Premiun = E(r) - rf 
            Expected_Return = expected_returns.mean_historical_return(asset_data)
            risk_premium = Expected_Return - self.RISK_FREE_RATE

            Expected_Returns[ticker] = Expected_Return
            risk_premiums[ticker] = risk_premium
            

            
            # for the individual betas and alphas

            print(f'ANOVA Table: {model.summary()}')
            print(f'R2 Score: {model.rsquared*100:.2f}')
            print(f"Risk-Premium: {risk_premium}")
            plt.figure(figsize=(12,6))
            sns.scatterplot(x=market_returns, y=returns, label=ticker)
            sns.lineplot(x=market_returns, y=model.fittedvalues, color='red', label='Security Market Line')
            plt.title(f'Single Index Model for {ticker}')
            plt.xlabel('Market Excess Return')
            plt.ylabel(f'{ticker} Excess Return')
            plt.legend()
            os.makedirs(output_dir, exist_ok=True)
            plt.savefig(os.path.join(output_dir, f"single_index_model_{ticker}.png"))
            plt.show()



