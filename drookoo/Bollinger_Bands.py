"""Bollinger Bands for stock ticker symbol."""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_ticker():
    """Place Stock Ticker Symbol Here"""
    ticker = 'SQ'
    return ticker

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if get_ticker() not in symbols:  # add AMD for reference, if absent
        symbols.insert(0, get_ticker())

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == get_ticker():  # drop dates AMD did not trade
            df = df.dropna(subset=[get_ticker()])

    return df


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return pd.rolling_mean(values, window=window)


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    # TODO: Compute and return rolling standard deviation
    return pd.rolling_std(values, window=window)

def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    # TODO: Compute upper_band and lower_band
    upper_band = rm + rstd * 2
    lower_band = rm -rstd * 2
    return upper_band, lower_band


def test_run():
    # Read data
    dates = pd.date_range('2015-10-27', '2017-10-27')
    symbols = [get_ticker()]
    df = get_data(symbols, dates)

    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_AMD = get_rolling_mean(df[get_ticker()], window=20)

    # 2. Compute rolling standard deviation
    rstd_AMD = get_rolling_std(df[get_ticker()], window=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_AMD, rstd_AMD)

    # Plot raw AMD values, rolling mean and Bollinger Bands
    ax = df[get_ticker()].plot(title="Bollinger Bands", label=get_ticker())
    rm_AMD.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    test_run()
