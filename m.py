import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./databases/Salary_Data.csv')
veri = data.copy()

print(veri["Age"])

x = veri["YearsExperience"]
Y = veri["Salary"]

# datamızı aldık. şimdi, aralarındaki ilişkiye göz atalım

plt.scatter(Y,x)

plt.show()