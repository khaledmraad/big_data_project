import pandas as pd

df = pd.read_csv("csv_result/part-00005-458a8eae-3796-4d7f-8471-ed368b48de64-c000.csv",on_bad_lines="skip")

# print(df.head()[1:])

print(len(df.columns))

print(df.dtypes)

# test="App Name,App Id,Category,Rating,Rating Count,Installs,Minimum Installs,Maximum Installs,Free,Price,Currency,Size,Minimum Android,Developer Id,Released,Last Updated,Content Rating,Ad Supported,In App Purchases,Editors Choice".split(",")


# for i in test:
    # print (f"row[\"{i}\"], ",end="")
for i,j in df.iterrows():
    print(j["App Name"])
    if i ==6:
        break