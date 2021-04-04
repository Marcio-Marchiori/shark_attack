import re
import pandas as pd
import numpy as np


shark_data = pd.DataFrame(pd.read_csv('data/attacks.csv'))
shark_data.dropna(axis=0, how='all',inplace=True)
shark_data.columns
