import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

ticker_symbol = 'AAPL'
stock_data=yf.download(ticker_symbol, start='2020-01-01', end='2024-12-31')

plt.figure(figsize=(10, 5))
plt.plot(stock_data['Close'])
plt.title('Stock price of ' + ticker_symbol)
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()

# Calculate the 50-day moving average
stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()

# Plot the closing prices and the moving average
plt.figure(figsize=(10, 5))
plt.plot(stock_data['Close'], label='AAPL Close')
plt.plot(stock_data['50_MA'], label='50-Day MA', linestyle='--')
plt.title('Apple Inc. (AAPL) Stock Price with 50-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.legend()
plt.grid(True)
plt.show()






