import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import plotly.express as ex

credit = pd.read_csv("Bases_de_Dados/credit_data.csv")

print(credit.describe())

credit.dropna()

print(credit.info())

print(np.unique(credit['default'],return_counts=True))

