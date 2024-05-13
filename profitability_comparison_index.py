import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['^GSPC', '^IXIC', '^GDAXI', '^FTSE']
index_name = {
    '^GSPC': 'S&P 500',
    '^IXIC': 'NASDAQ',
    '^GDAXI': 'DAX',
    '^FTSE': 'FTSE 100'
}

data = yf.download(tickers, start="1997-1-1")['Adj Close']

returns = data.pct_change()

plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(data.index,
             data[ticker], label=index_name[ticker])

plt.title('Indices de Mercado')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento Ajustado')
plt.legend()
plt.grid(True)
plt.show()