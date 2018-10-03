import client
import indicators
import utils

import pandas as pd
import matplotlib.pyplot as plt

# %%
# retrieve history
symbol = "SECB"
df = client.get_history(symbol, days=800)
df2 = client.get_history("GLO", days=800)
# %%
# calculate the indicators
xlimit = [220, 300]
ylimit = [210, 270]
df = indicators.heiken_ashi(df)
df['ha_strength'] = (df['ha_high'] - df['ha_open']) - (df['ha_close'] - df['ha_low'])
df['ha_cd'] = (df['ha_close'] - df['ha_open'])
df['ha_cd_s'] = (df['ha_strength'] + df['ha_cd'])

df[['ha_open', 'ha_close', 'ha_high', 'ha_low']].plot(style='.-', alpha=0.6, figsize=(20,10))
plt.xlim(xlimit)
plt.ylim(ylimit)
# plt.grid('on', which='minor', axis='x' )
# plt.grid('off', which='major', axis='x' )
plt.show()


df[['ha_strength', 'ha_cd', 'ha_cd_s']].plot(style='.-', alpha=0.6, figsize=(20,10))
plt.axhline(y=0, color='black', linestyle='--', alpha=0.2)
plt.xlim(xlimit)
plt.show()

# %%
df2 = indicators.heiken_ashi(df2)
df2['ha_strength'] = (df2['ha_high'] - df2['ha_open']) - (df2['ha_close'] - df2['ha_low'])
df2['ha_cd'] = (df2['ha_close'] - df2['ha_open'])

df2[['ha_open', 'ha_close', 'ha_high', 'ha_low']].plot(style='.-', alpha=0.6, figsize=(10,5))
plt.xlim([240,300])
plt.show()

df2[['ha_strength', 'ha_cd']].plot(style='.-', alpha=0.6, figsize=(10,5))
plt.axhline(y=0, color='black', linestyle='--', alpha=0.2)
plt.xlim([240,300])
plt.show()
