from datetime import datetime
import pandas as pd
from xbbg import blp


def fetch_data_from_bloomberg(ticker_symbols, start_date, end_date):
    data = blp.bdh(tickers=ticker_symbols, flds=['last_price', 'NAV_CRNCY'],start_date=start_date, end_date=end_date, Per='M')
    data.dropna(inplace=True, thresh=3,axis=0)
    # Save the data to a CSV file
    data.to_csv('bloomberg_data.csv')

    return data.head()


if __name__ == "__main__":
    # Read ticker symbols from the CSV file
    ticker_symbols_df = pd.read_csv('tickersymbols.csv')
    ticker_symbols = ticker_symbols_df['Ticker'].tolist()

    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

    # Determine today's date
    end_date = datetime.today()

    retrieved_data = fetch_data_from_bloomberg(ticker_symbols, start_date, end_date)
    print(f"Monthly data fetched from {start_date_str} to {end_date.strftime('%Y-%m-%d')}:")
    print(retrieved_data)