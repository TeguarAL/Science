import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
from scipy.stats import norm


# test for null hypothesis zirconium-niobium alloy
# bar plot + normal distribution + real distribution
file = sorted(os.listdir('E:\study\sdws\\result_test_1'))
for k in file:
    if 'Э110' in k:
        data = pd.read_csv(fr'E:\study\sdws\\result_test_1\{k}')
        ax = sns.distplot(data['r_h_mean'], fit=norm)
        ax.set_xlabel('heat resist')
        ax.set_ylabel('count', rotation=0)
        ax.set(title=f'{k}')
        plt.show()


# for i in ['Э110 0,5 + Э110 0,5', 'Э110 0,5 + Э110 0,8', 'Э110 0,8 + Э110 0,8']:
#     for k in ['I', 'II', 'III', 'IV']:
#         df = pd.read_excel(fr'E:\study\sdws\Данные сопротивлений\{i} ({k})\{i} ({k}).xlsx')
#         ax = sns.distplot(df['Горячий'], fit=norm)
#         ax.set_xlabel('heat resist')
#         ax.set_ylabel('count', rotation=0)
#         ax.set(title=f'{i+k}')
#         plt.show()