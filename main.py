import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import gspread

gc = gspread.service_account()

sh = gc.open("Measurements Over Time")

# print(sh.sheet1.get('A1'))

df = pd.DataFrame(sh.get_worksheet(0).get_all_records())

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

# print(df.keys())

# table = df.pivot(index='Date', columns=df.keys()[1::])

# table.head()

# table.plot()

# print(table)

# # dates = df['Date']

print(df)

df.plot()
plt.show()


# plt.rcParams["figure.figsize"] = [7.50, 3.50]

# df = pd.read_csv(url_1, encoding='unicode_escape', header=1)
# print(df)

# df.plot()

# plt.show()

# # # X axis parameter:
# # xaxis = np.array([2, 8])

# # # Y axis parameter:
# # yaxis = np.array([4, 9])

# # plt.plot(xaxis, yaxis)


# # x = df['1']
# # y = df['2']

# # # plot
# # plt.plot(x,y)
# # plt.savefig("mygraph.png")
