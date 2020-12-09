import pandas as pd
import numpy as np
import copy

df = pd.read_csv('score.csv')

names = list(df.columns[1:])
subjects = list(df.iloc[:, 0])

df_grade = copy.deepcopy(df)
df_gpa = copy.deepcopy(df)

for row_index, row in df_grade.iterrows():
    for column_index, column in row.iteritems():
        if column_index == 'Unnamed: 0':
            continue
        if int(df_grade.loc[row_index, column_index]) >= 90:
            df_grade.loc[row_index, column_index] = 'A'
            df_gpa.loc[row_index, column_index] = 4.00
        elif int(df_grade.loc[row_index, column_index]) >= 80:
            df_grade.loc[row_index, column_index] = 'B'
            df_gpa.loc[row_index, column_index] = 3.00
        elif int(df_grade.loc[row_index, column_index]) >= 70:
            df_grade.loc[row_index, column_index] = 'C'
            df_gpa.loc[row_index, column_index] = 2.00
        elif int(df_grade.loc[row_index, column_index]) >= 60:
            df_grade.loc[row_index, column_index] = 'D'
            df_gpa.loc[row_index, column_index] = 1.00
        else:
            df_grade.loc[row_index, column_index] = 'F'
            df_gpa.loc[row_index, column_index] = 0.00

print("Grades for each students: ")
print(df_grade)

gpas = df_gpa.iloc[:, 1:].values

average_gpas = np.average(gpas, axis=0)

class_gpa = np.average(average_gpas)

print("")

for i in range(len(average_gpas)):
    print("{} {:.2f}".format(df.columns[i + 1], average_gpas[i]))

print("The class GPA is {:.2f}".format(class_gpa))