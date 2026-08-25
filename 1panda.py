import pandas as pd

data = {
    "Name": ["Aniket", "Rahul", "Aman", "Raj"],
    "Marks": [85, 72, 91, 65]
}

df = pd.DataFrame(data)

print("All Students:")
print(df)

print("\nStudents who scored more than 80:")
print(df[df["Marks"] > 80])