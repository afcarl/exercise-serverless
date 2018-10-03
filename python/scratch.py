import client
import indicators
import utils

import pandas as pd
import matplotlib.pyplot as plt

def plot(df, xlim=[0,1000], ylim=[0,1000]):
    fig, ax = plt.subplots()
    df[['ha_open', 'ha_close', 'ha_high', 'ha_low']].plot(style='.-', alpha=0.6, figsize=(10,6), grid=True, ax=ax)
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.4', color='black')
    ax.grid(which='minor', linestyle=':', linewidth='0.4', color='black')
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    # plt.grid('on', which='minor', axis='x' )
    # plt.grid('off', which='major', axis='x' )
    plt.show()

    fig, ax = plt.subplots()
    df[['ha_strength', 'ha_cd']].plot(style='.-', alpha=0.6, figsize=(10,6), grid=True, ax=ax)
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.4', color='black')
    ax.grid(which='minor', linestyle=':', linewidth='0.4', color='black')
    plt.axhline(y=0, color='black', linestyle='--', alpha=0.2)
    plt.xlim(xlimit)
    plt.show()

# %%
# retrieve history
symbol = "SECB"
df = client.get_history(symbol, days=800)
df2 = client.get_history("GLO", days=800)
# %%
df = indicators.heiken_ashi(df)
df['ha_strength'] = (df['ha_high'] - df['ha_open']) - (df['ha_close'] - df['ha_low'])
df['ha_cd'] = (df['ha_close'] - df['ha_open'])
df['ha_cd_s'] = (df['ha_strength'] + df['ha_cd'])

# calculate the indicators
df.set_index('date', inplace=True)

# %%
xlimit = [200, 800]
ylimit = [0, 270]
plot(df, xlim=xlimit, ylim=ylimit)
# %%
# df2 = indicators.heiken_ashi(df2)
# df2['ha_strength'] = (df2['ha_high'] - df2['ha_open']) - (df2['ha_close'] - df2['ha_low'])
# df2['ha_cd'] = (df2['ha_close'] - df2['ha_open'])
#
# df2[['ha_open', 'ha_close', 'ha_high', 'ha_low']].plot(style='.-', alpha=0.6, figsize=(10,5))
# plt.xlim([240,300])
# plt.show()
#
# df2[['ha_strength', 'ha_cd']].plot(style='.-', alpha=0.6, figsize=(10,5))
# plt.axhline(y=0, color='black', linestyle='--', alpha=0.2)
# plt.xlim([240,300])
# plt.show()
