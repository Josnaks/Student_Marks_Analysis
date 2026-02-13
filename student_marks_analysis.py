import pandas as pd
data={
    "Name":["Asha", "Rahul", "Meena", "John"],
    "Maths":[80,65,90,70],
    "Science":[75,60,95,72],
    "English":[85,70,88,68]
}
df=pd.DataFrame(data)
df["Average"]=df[["Maths", "Science", "English"]].mean(axis=1)
print(df)
top_student=df.sort_values("Average", ascending=False).head(1)
print("\nTop Studen:")
print(top_student)
import matplotlib.pyplot as plt
plt.bar(df["Name"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average marks")
plt.title("Average Marks of Students")
plt.show()
df.to_excel("student_marks_output.xlsx", index=False)
