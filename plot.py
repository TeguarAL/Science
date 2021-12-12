import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 80)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)


# graphs for visual analysis and search for obvious dependencies and errors
df = pd.read_csv(r'E:\study\sdws\Data_set.csv')
for i in range(1, 24):
    df1 = df.loc[i*4:i*4+3]
    df1.plot(x='name', y=['r_h_min', 'r_h_mean', 'r_h_max'],
            kind='bar')
    plt.suptitle((df['name'].iloc[i * 4]), fontsize=12, color='black')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(.6, .9))
    plt.grid(True)
    plt.show()






















# for i in range(1, 20):
#     df1 = df.loc[i*4:i*4+3]
#     df1.plot(x='Current modes', y=['RBE preheated (min), mΩ', 'RBE preheated (mean), mΩ', 'RBE preheated (max), mΩ'],
#             kind='bar')
#     plt.suptitle((df['Material 1'].iloc[i * 4], df['Thickness 1, mm'].iloc[i * 4], df['Material 2'].iloc[i * 4],
#                   df['Thickness 2, mm'].iloc[i * 4]), fontsize=12, color='black')
#     plt.xticks(rotation=0)
#     plt.legend(bbox_to_anchor=(.6, .9))
#     plt.grid(True)
#     plt.show()

# df_ch = df.iloc[68:,0:7]
# df_min = df['RBE preheated (min), mΩ']
# df_ch = df_ch.assign(min=(df['RBE cold (min), mΩ']),
#                      mean=(df['RBE cold (mean), mΩ']),
#                      max=(df['RBE cold (max), mΩ']))
# df_ch = df_ch.loc[df['Current modes'] == 4]
# print(df_ch)
#
# df_ch.plot(x='Current modes', y=['min'], kind='bar')
# plt.xticks(rotation=0)
# plt.grid(True)
# df_ch.plot(x='Current modes', y=['mean'], kind='bar')
# plt.xticks(rotation=0)
# plt.grid(True)
# df_ch.plot(x='Current modes', y=['max'], kind='bar')
# plt.xticks(rotation=0)
# plt.grid(True)
# plt.show()
