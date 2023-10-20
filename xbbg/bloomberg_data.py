from datetime import datetime
import pandas as pd
from xbbg import blp


def fetch_price_from_bloomberg(ticker_symbols, start_date, end_date):
    price = blp.bdh(tickers=ticker_symbols, flds=['last_price'],start_date=start_date, end_date=end_date, Per='M')
    price.dropna(inplace=True, thresh=3,axis=0)

    # Save the data to a CSV file
    price.to_csv('bloomberg_price.csv')


def fetch_currency_from_bloomberg(ticker_symbols):
    currency = blp.bdp(tickers=ticker_symbols, flds=['CRNCY'])
    currency = currency.T

    # Save the data to a CSV file
    currency.to_csv('bloomberg_curr.csv')


def merge_price_currency():
    price_data = pd.read_csv('bloomberg_price.csv')
    currency_data = pd.read_csv('bloomberg_curr.csv')

    data_combined = pd.concat([currency_data,price_data],axis=0)

    data_combined.to_csv('bloomberg_data.csv',index=False)

if __name__ == "__main__":
    # Read ticker symbols from the CSV file
    ticker_symbols_df = pd.read_csv('tickersymbols.csv')
    ticker_symbols = sorted(ticker_symbols_df['Ticker'].tolist())

    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

    # Determine today's date
    end_date = datetime.today()

    fetch_price_from_bloomberg(ticker_symbols, start_date, end_date)
    fetch_currency_from_bloomberg(ticker_symbols)
    merge_price_currency()
