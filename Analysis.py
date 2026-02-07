import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [78, 85, 62, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())

# Visualization
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.show()
