# -*- coding: utf-8 -*-
"""
Created on Sun May 21 10:21:49 2017

@author: David Holdaway
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
%matplotlib inline

# create a Series with an arbitrary list
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
s
