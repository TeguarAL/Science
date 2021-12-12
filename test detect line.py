import pandas as pd


pd.set_option('display.max_rows', 1200)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

#test model for formation data set
data_r = pd.DataFrame(columns=['u', 'i'])
df = pd.read_excel(r'E:\study\sdws\Данные сопротивлений\Э110 0,5 + Э110 0,5 (I)\\1\NewFile1.xlsx',
                   header=None, sheet_name='1')
df_u = pd.read_excel(r'E:\study\sdws\Данные сопротивлений\Э110 0,5 + Э110 0,5 (I)\\1\NewFile1.xlsx',
                     header=None, sheet_name='u')
df_i = pd.read_excel(r'E:\study\sdws\Данные сопротивлений\Э110 0,5 + Э110 0,5 (I)\\1\NewFile1.xlsx',
                     header=None, sheet_name='i')
data = pd.DataFrame()
data_end = pd.DataFrame(columns=['r_h_mean', 'r_h_min', 'r_h_max', 'r_h_std', 'r_h_mad'])

data = data.assign(u=df_u[1].values, i=df_i[1].values)

data = data.dropna()
while data['i'].iloc[-1] < 900.:
    data = data[:-1]


data = data.drop(data[(data['i'] < (data['i'][-100:-50].mean())*0.97) |
                      (data['i'] > (data['i'][-100:-50].mean())*1.03)].index)
while data.shape[0] > 1:
    if (data.index[1] - data.index[0]) != 1:
        data = data[1:]
        data_r = pd.DataFrame(columns=['u', 'i'])
    else:
        data_r = data_r.append(data[:1], ignore_index=False)
        data = data[1:]


data_r = data_r.append(data[-1:], ignore_index=False)
data_r = data_r.assign(r=(data_r['u'] / data_r['i'] * 1000).values)
data_end = data_end.append({'r_h_mean': data_r.mean(),
                            'r_h_min': data_r.min(),
                            'r_h_max': data_r.max(),
                            'r_h_std': data_r,
                            'r_h_mad': data_r}, ignore_index=True)
print(data_end)
data_end.to_csv('E:\study\sdws\\result_test_1\Data_set.csv', sep=',')