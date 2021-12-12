import pandas as pd
import os.path
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

# записываю файлы в csv формат, делаю свой расчёт, пытаюсь всзять диапазон теплового сопротивление
data_end = pd.DataFrame(columns=['name', 'r_h_mean', 'r_h_min', 'r_h_max', 'r_h_std', 'r_h_mad'])
for k in sorted(os.listdir('E:\study\sdws\Данные сопротивлений\\')):
    data_r_h = pd.DataFrame(columns=['r_h_mean'])
    for i in sorted(os.listdir(f'E:\study\sdws\Данные сопротивлений\{k}\\')):
        if '.xlsx' in i:
            continue
        num_files = sum(
            os.path.isfile(os.path.join(f'E:\study\sdws\Данные сопротивлений\{k}\\{i}', f))
            for f in os.listdir(f'E:\study\sdws\Данные сопротивлений\{k}\\{i}'))
        for j in os.listdir(f'E:\study\sdws\Данные сопротивлений\{k}\\{i}\\'):
            df = pd.read_excel(f'E:\study\sdws\Данные сопротивлений\{k}\{i}\\{j}',
                               header=None, sheet_name='1')
            df_u = pd.read_excel(f'E:\study\sdws\Данные сопротивлений\{k}\{i}\\{j}',

                                 header=None, sheet_name='u')
            df_i = pd.read_excel(f'E:\study\sdws\Данные сопротивлений\{k}\{i}\\{j}',
                                 header=None, sheet_name='i')
            data_r = pd.DataFrame(columns=['u', 'i'])
            data = pd.DataFrame()

            data = data.assign(u=df_u[1].values,
                               i=df_i[1].values)

            data = data.dropna()
            while data['i'].iloc[-1] < 900.:
                data = data[:-1]

            data = data.drop(data[(data['i'] < (data['i'][-100:-50].mean()) * 0.97) | (
                        data['i'] > (data['i'][-100:-50].mean()) * 1.03)].index)
            while data.shape[0] > 1:
                if (data.index[1] - data.index[0]) != 1:
                    data = data[1:]
                    data_r = pd.DataFrame(columns=['u', 'i'])
                else:
                    data_r = data_r.append(data[:1], ignore_index=True)
                    data = data[1:]

            data_r = data_r.append(data[-1:], ignore_index=False)
            data_r = data_r.assign(r=(data_r['u'] / data_r['i'] * 1000).values)
            data_r_h = data_r_h.append({'r_h_mean': data_r['r'].mean()}, ignore_index=True)
    data_end = data_end.append({'name': f'{k}',
                                'r_h_mean': data_r_h['r_h_mean'].mean(),
                                'r_h_min': data_r_h['r_h_mean'].min(),
                                'r_h_max': data_r_h['r_h_mean'].max(),
                                'r_h_std': data_r_h['r_h_mean'].std(),
                                'r_h_mad': data_r_h['r_h_mean'].mad()}, ignore_index=True)
    data_r_h.to_csv(f'E:\study\sdws\\result_test_1\{k}.csv', sep=',')
data_end.to_csv('E:\study\sdws\Data_set.csv', sep=',')
print(data_end)

