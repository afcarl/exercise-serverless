# %%
import quandl as qd
import matplotlib.pyplot as plt

# %%
mydata = qd.get('WIKI/AMZN')

# %%
def bema_6(x):
    return ((x[0] + (5 * x[1]) + (10 * x[2]) + (10 * x[3]) + (5 * x[4]) + x[5]) / 32)

# %%
mydata['Binomial MA 6'] = mydata['Adj. Close'].rolling(6).apply(bema_6).shift(-2)


# %%
mydata[['Adj. Close', 'Binomial MA 6']].plot(figsize=(18,9),xlim=['2017-01-01','2018-01-01'], ylim=[700,1200])
plt.show()
