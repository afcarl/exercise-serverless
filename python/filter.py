import sys, getopt
import pandas as pd

df = pd.read_pickle('./equities.pkl')
print(df.query().to_string(justify='left'))
