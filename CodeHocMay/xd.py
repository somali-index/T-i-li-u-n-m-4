import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Name": [
        "An", "Binh", "Chi", "Dung", "Em",
        "Giang", "Hoa", "Hung", "Khanh", "Lan",
        "Minh", "Nam", "Oanh", "Phong", "Quan",
        "Son", "Trang", "Tuan", "Vy", "Yen"
    ],
    "Age": [
        18, 19, 20, 18, 21,
        20, 19, 22, 18, 21,
        20, 19, 22, 18, 21,
        20, 19, 22, 18, 21
    ],
    "Gender": [
        "Male", "Male", "Female", "Male", "Female",
        "Female", "Female", "Male", "Female", "Female",
        "Male", "Male", "Female", "Male", "Male",
        "Male", "Female", "Male", "Female", "Female"
    ],
    "Major": [
        "IT", "IT", "Business", "IT", "Data Science",
        "Data Science", "Business", "IT", "Business", "Data Science",
        "IT", "Data Science", "Business", "IT", "Business",
        "Data Science", "IT", "IT", "Business", "Data Science"
    ],
    "Math": [
        8, 7, 9, 6, 8, 9, 7, 5, 8, 9,
        6, 7, 8, 5, 9, 7, 8, 6, 9, 10
    ],
    "English": [
        7, 6, 8, 5, 9, 8, 7, 4, 9, 8,
        6, 8, 7, 5, 8, 6, 9, 7, 8, 10
    ],
    "GPA": [
        3.2, 2.8, 3.8, 2.4, 3.6,
        3.9, 3.1, 2.0, 3.5, 3.8,
        2.7, 3.3, 3.6, 2.1, 3.9,
        3.0, 3.7, 2.9, 3.8, 4.0
    ]
}

df = pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.columns)


# 1
# sns.histplot(data=df,x="GPA")
# plt.show()

# 3
# sns.barplot(data=df,x="Major",y="Math")
# plt.xlabel("các nghành học")
# plt.ylabel("Điểm môn toán")
# plt.show()

# 8
# sns.countplot(data=df,x="Major")
# plt.show()

# 2
# sns.boxplot(data=df,x="Major",y="GPA")
# plt.show()