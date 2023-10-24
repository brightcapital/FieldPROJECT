from datetime import datetime
import pandas as pd
from xbbg import blp


def fetch_price_from_bloomberg(ticker_symbols, equities, currency, start_date, end_date):
    price_data = blp.bdh(tickers=ticker_symbols, flds=['last_price'],start_date=start_date, end_date=end_date, Per='M')
    # to delete the empty rows which are the end days of month but not the working days
    price_data.dropna(inplace=True, thresh=3,axis=0)
    price_data.columns = price_data.columns.droplevel(-1)
    header = [ticker_symbols, equities, currency]
    price_data.columns = header

    # Save the data to a CSV file
    price_data.to_csv('bloomberg_price.csv')


if __name__ == "__main__":
    # Read ticker symbols, equities and currency from the CSV file
    bloomberg_equities = pd.read_csv('tickers_equities.csv', index_col=False)
    bloomberg_equities = bloomberg_equities.sort_values(by=['BBG Ticker'], ignore_index=True)

    ticker_symbols = bloomberg_equities['BBG Ticker']
    equities = bloomberg_equities['Equities']
    currency = bloomberg_equities['Currency']


    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

    # Determine today's date
    end_date = datetime.today()

    fetch_price_from_bloomberg(ticker_symbols, equities, currency, start_date, end_date)
