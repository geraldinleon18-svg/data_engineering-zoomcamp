import sys
import pandas as pd

month=int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df["month"] = month

df.to_parquet(f"output_{month}.parquet")
print(df.head())

print("Hello pipeline!")
print("argument:", sys.argv[1])
print("the month is:", month)

