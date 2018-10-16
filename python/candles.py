import client
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
ali = client.get_last("JGS", bars=3)


# drop the date
# ali = ali.drop("date", axis=1)

# open dont change, close is close of the last, high and low are max
ali['dopen'] = ali['open']

ali['dhigh'] =  pd.Series(np.array([ali['high'].tail(3).max(), ali['high'].tail(2).max(), ali['high'].tail(1).max()]))

ali['dlow'] =  pd.Series(np.array([ali['low'].tail(3).min(), ali['low'].tail(2).min(), ali['low'].tail(1).min()]))

ali['dclose'] = pd.Series(np.repeat(ali.loc[2]['close'], 3))
ali = ali.drop("date", axis=1)
ali = ali.drop("volume", axis=1)
plt.show()
