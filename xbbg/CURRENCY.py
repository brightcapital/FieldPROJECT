from datetime import datetime
import pandas as pd
from xbbg import blp


def fetch_data_from_bloomberg(ticker_symbols):
    data = blp.bdp(tickers=ticker_symbols, flds=['CRNCY'])
    data = data.T

    # Save the data to a CSV file
    data.to_csv('bloomberg_curr.csv')

    return data.head()


if __name__ == "__main__":
    # Read ticker symbols from the CSV file
    ticker_symbols_df = pd.read_csv('tickersymbols.csv')
    ticker_symbols = ticker_symbols_df['Ticker'].tolist()


    retrieved_data = fetch_data_from_bloomberg(ticker_symbols)
    print(retrieved_data)