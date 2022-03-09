import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['1','2','3', '4', '5', '6', '7', '8', '9', '10']
df = pd.read_csv('/home/dillonestrada/Documents/Development/measurements/SampleCSVFile.csv', encoding='unicode_escape')
print(df)

df.plot()

plt.show()

# # X axis parameter:
# xaxis = np.array([2, 8])

# # Y axis parameter:
# yaxis = np.array([4, 9])

# plt.plot(xaxis, yaxis)


# x = df['1']
# y = df['2']

# # plot
# plt.plot(x,y)
# plt.savefig("mygraph.png")
