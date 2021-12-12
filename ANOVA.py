import pandas as pd
import os.path
import statsmodels.api as sm
from statsmodels.formula.api import ols


# Analysis of variance
count = 0
count_name = pd.Series(dtype='object')
resist = pd.Series(dtype='float64')
for i in sorted(os.listdir('E:\study\sdws\\result_test_1')):
    if count < 4:
        df_read = pd.read_csv(f'E:\study\sdws\\result_test_1\\{i}')
        count_name = count_name.append(pd.Series(len(df_read) * [i]), ignore_index=True)
        resist = resist.append(df_read['r_h_mean'], ignore_index=True)
        count += 1
        if count == 4:
            df_write = pd.DataFrame({'name': count_name,
                                     'resistance': resist})
            anova = ols('resistance ~ name', data=df_write).fit()
            table = sm.stats.anova_lm(anova)
            print(i[:-8])
            print(table)
            print()
            count_name = pd.Series(dtype='object')
            resist = pd.Series(dtype='float64')
            count = 0

# Based on the obtained values of the p-criterion, we can say that the correct alternative hypothesis
