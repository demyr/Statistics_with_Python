import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")

da["marital_status"] = da.DMDMARTL.replace({1: "Unmarried", 2: "Married", 3: "Widow", 4: "Divorced",
                                            5: "Separated", 6: "Registered partner", 7: "Separated partner"})

da["gender"] = da.RIAGENDR.replace({1: 'Male', 2: 'Female'})
da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])

da_male = da.loc[(da.gender == 'Male') & da.agegrp.isin([30, 40])]
da_female = da.loc[(da.gender == 'Female') & da.agegrp.isin([30, 40])]
print(da.marital_status.value_counts())
print(da_male.marital_status.value_counts())
print(da_female.marital_status.value_counts())