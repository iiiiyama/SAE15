import pandas as pd

for i in range (1,6):
    lecture = pd.read_csv(f"netflix-{i}.csv", header=None)
    test = lecture.drop(lecture.columns[11], axis=1)
    test.to_csv(f"output{i}.csv")

df = pd.concat(
    map(pd.read_csv, ['output1.csv', 'output2.csv','output3.csv','output4.csv','output5.csv']), ignore_index=True)
print(df)
df.to_csv("test.csv", index=False)