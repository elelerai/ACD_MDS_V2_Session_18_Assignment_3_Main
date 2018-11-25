# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:27:57 2018

@author: Eliud Lelerai
"""

import numpy as pd
import pandas as pd
from scipy import stats
import math

# Computing the z score

score=1100

mean_score=1026

stdev=209

#How well did the student score?

z=(score-mean_score)/stdev
  
import scipy.stats as st

z_prob=st.norm.cdf(z)

print(z_prob)  

# The student score 63.8%