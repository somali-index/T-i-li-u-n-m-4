from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt


data=load_iris()
x=data.data
df=pd.DataFrame(x,columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])

plt.plot(df["SepalLengthCm"],df["SepalWidthCm"],"ro")

plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Biểu đồ Sepal length và witdh')


plt.show()