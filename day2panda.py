import pandas as pd

data = {
    "Name": ["aniket","rahul","abhishek"],
    "Age" :["21","19","23"],
    "Marks" : ["32","23","20"],
}
df = pd.DataFrame(data)
print (df)